#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import glob
import logging
import pickle

import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from selenium_automation.drivers import driver

# from selenium_automation.javascript import JSFunctions  # noqa


def _get_log_file(path, extension):
    return path + "-{}-{}.{}".format(
        datetime.date.today().isoformat(), time.time(), extension
    )


def _filepath(name, extension):
    return _get_log_file("../data/trace/" + name, extension)


def init():
    driver.delete_all_cookies()
    # driver.fullscreen_window()


def restart():
    driver.start_client()


def clean():
    driver.quit()


def get_cookies(_file):
    logging.info("get Cookies")
    cookies = driver.get_cookies()
    pickle.dump(cookies, open(_file, "wb"))


def source():
    return driver.page_source


def set_cookies(_file):

    logging.info("set Cookies")
    cookies = pickle.load(open(_file, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)


def open_page(url):
    logging.info("Open: %s", url)
    driver.get(url)


def download_src(javascript):  # TODO: make it work

    time.sleep(1)
    image_src = driver.execute_script(javascript)
    # check if there is http/https in the front.
    # yes go
    # no:
    # # add first part of the url
    # run content = requests.get(image_src)
    # extract filename with file utils
    # save content
    # file with name like the image
    contents = "<img src='{}' />"
    image_filename = _filepath("file", "html")

    _file = open(image_filename, "w")
    _file.write(contents.format(image_src))
    _file.close()


def download_known_file(prefix, suffix):
    query = "/".join([driver.download_dir, "%s*%s" % (prefix, suffix,)])

    while True:
        files = glob.glob(query)
        if len(files):
            return files[0]
        time.sleep(1)


def download_file():
    """This works like this:
        - first there is set acceptance for downloading all
        - second, files are downloaded
        - third, code checks for files with chrome extension
          (when the file with extension is, the file is downloaded)
        - fourth,return path of the file
        """
    """ download a file that is somewhere """
    chrome_download = "crdownload"
    extension = "." + chrome_download
    download = None
    query = "/".join([driver.download_dir, "*" + extension])
    while True:
        if download is None:
            files = glob.glob(query)
            if len(files):
                download, _ = files[0].split(extension)

        if download:
            files = glob.glob(download)
            if len(files):
                return download
        time.sleep(1)


def take_screenshoot():
    image_filename = _filepath("screenshoot", "png")
    driver.save_screenshot(image_filename)


def accept_alert():
    Alert(driver).accept()


def dismiss_alert():
    Alert(driver).dismiss()


def alert_text():
    return Alert(driver).text


def execute_script(script, *args):

    driver.execute_script(script, *args)


def find(element):
    return driver.find_element(*element)


def click(element):

    logging.info("Click: %s", repr(element))
    el = driver.find_element(*element)

    actions = ActionChains(driver)
    actions.move_to_element(el)
    actions.click(el)
    actions.perform()


def type_text(text):
    """Type text to last focused element"""
    logging.info("Enter text: %s", text)

    actions = ActionChains(driver)
    actions.send_keys(text)
    actions.perform()


def click_on_link_with_text(text):

    logging.info("Click on link with text: %s", text)
    element = driver.find_element_by_link_text(text)
    actions = ActionChains(driver)
    actions.click(element)
    actions.perform()


def check_page_url(url, page):

    logging.info("Check if page: %s", url)
    page = url == driver.current_url
    print(page)


def wait(seconds):

    logging.info("Wait: %ss", seconds)
    driver.implicitly_wait(seconds)


def wait_for(condition, seconds):

    try:
        element = WebDriverWait(driver, seconds).until(condition)
        return element
    except Exception as e:
        raise e


def title_contains(string):
    return ec.title_contains(string)


def element_contains(string, element):
    return ec.text_to_be_present_in_element(element, string)


def element_being(element):
    return ec.presence_of_element_located(element)


def sleep(seconds):
    logging.info("Sleep for: %ss", seconds)
    time.sleep(seconds)


def enter_text(text, element):

    logging.info("Enter text: %s", text)
    el = driver.find_element(*element)
    el.send_keys(text)


def clear_field(element):

    logging.info("Clear field: %s", element)
    el = driver.find_element(*element)
    el.clear()


# list of keys is in Keys.py (look up at imports)
# use lower or upper letters , doesn't matter


def press_key(key, element):
    el = driver.find_element(*element)
    el.send_keys(Keys.__dict__[key.upper()])


def scroll_into(element):
    el = driver.find_element(*element)
    driver.execute_script("arguments[0].scrollIntoView();", el)


# def load_js():
#    driver.execute_script(JSFunctions.click)
#    driver.execute_script(JSFunctions.enter_text)
#    driver.execute_script(JSFunctions.get_row_sibling)


def pagetest_headers():
    pass


def pagetest_ip():
    pass


def pagetest_recaptchav3():
    pass


command_list = {
    "init": init,
    "restart": restart,
    "clean": clean,
    "get_cookies": get_cookies,
    "source": source,
    "set_cookies": set_cookies,
    "open_page": open_page,
    "take_screenshoot": take_screenshoot,
    "accept_alert": accept_alert,
    "dismiss_alert": dismiss_alert,
    "alert_text": alert_text,
    "execute_script": execute_script,
    "find": find,
    "click": click,
    "type_text": type_text,
    "click_on_link_with_text": click_on_link_with_text,
    "check_page_url": check_page_url,
    "wait": wait,
    "wait_for": wait_for,
    "title_contains": title_contains,
    "element_contains": element_contains,
    "element_being": element_being,
    "sleep": sleep,
    "enter_text": enter_text,
    "clear_field": clear_field,
    "press_key": press_key,
    "scroll_into": scroll_into,
}

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


from selenium_automation.javascript import JSFunctions   # noqa


def get_log_file(path, extension):
    return path + "-{}-{}.{}".format(datetime.date.today().isoformat(),
                                     time.time(),
                                     extension)


def filepath(name, extension):
    return get_log_file("../data/trace/" + name, extension)


class Commands:
    def __init__(self, driver):
        self.driver = driver
        self.driver.delete_all_cookies()
        # self.driver.fullscreen_window()

    def restart(self):
        self.driver.start_client()

    def clean(self):
        self.driver.quit()

    def get_cookies(self, file):
        logging.info("get Cookies")
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(file, "wb"))

    def source(self):
        return self.driver.page_source

    def set_cookies(self, file):

        logging.info("get Cookies")
        cookies = pickle.load(open(file, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def get_page_source(self):
        return self.driver.page_source

    def open_page(self, url):

        logging.info("Open: %s", url)
        self.driver.get(url)

    def download_src(self, javascript):  # TODO: make it work

        time.sleep(1)
        image_src = self.driver.execute_script(javascript)
        # check if there is http/https in the front.
        # yes go
        # no:
        # # add first part of the url
        # run content = requests.get(image_src)
        # extract filename with file utils
        # save content
        # file with name like the image
        contents = "<img src='{}' />"
        image_filename = filepath("file", 'html')

        file = open(image_filename, 'w')
        file.write(contents.format(image_src))
        file.close()

    def download_known_file(self, prefix, suffix):
        query = "/".join([self.driver.download_dir, '%s*%s' % (prefix, suffix, )])

        while True:
            files = glob.glob(query)
            if len(files):
                return files[0]
            time.sleep(1)

    def download_file(self):
        """ download a file that is somewhere """
        chrome_download = 'crdownload'
        extension = '.' + chrome_download
        download = None
        query = "/".join([self.driver.download_dir, '*' + extension])
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

    def take_screenshoot(self):
        image_filename = filepath("screenshoot", 'png')
        self.driver.save_screenshot(image_filename)

    def accept_alert(self):
        Alert(self.driver).accept()

    def dismiss_alert(self):
        Alert(self.driver).dismiss()

    def alert_text(self):
        return Alert(self.driver).text

    def execute_script(self, script, *args):

        self.driver.execute_script(script, *args)

    def find(self, element):
        return self.driver.find_element(*element)

    def click(self, element):

        logging.info("Click: %s", repr(element))
        el = self.driver.find_element(*element)

        actions = ActionChains(self.driver)
        actions.move_to_element(el)
        actions.click(el)
        actions.perform()

    def type_text(self, text):
        """Type text to last focused element"""
        logging.info("Enter text: %s", text)

        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()

    def click_on_link_with_text(self, text):

        logging.info("Click on link with text: %s", text)
        element = self.driver.find_element_by_link_text(text)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.perform()

    def check_page_url(self, url, page):

        logging.info("Check if page: %s", url)
        page = url == self.driver.current_url
        print(page)

    def wait(self, seconds):

        logging.info("Wait: %ss", seconds)
        self.driver.implicitly_wait(seconds)

    def wait_for(self, condition, seconds):

        try:
            element = WebDriverWait(self.driver, seconds).until(
                condition
            )
            return element
        except Exception as e:
            raise e

    def title_contains(self, string):
        return ec.title_contains(string)

    def element_contains(self, string, element):
        return ec.text_to_be_present_in_element(element, string)

    def element_being(self, element):
        return ec.presence_of_element_located(element)

    def sleep(self, seconds):
        logging.info("Sleep for: %ss", seconds)
        time.sleep(seconds)

    def enter_text(self, text, element):

        logging.info("Enter text: %s", text)
        el = self.driver.find_element(*element)
        el.send_keys(text)

    def clear_field(self, element):

        logging.info("Clear field: %s", element)
        el = self.driver.find_element(*element)
        el.clear()

    # list of keys is in Keys.py (look up at imports)
    # use lower or upper letters , doesn't matter

    def press_key(self, key, element):
        el = self.driver.find_element(*element)
        el.send_keys(Keys.__dict__[key.upper()])

    def scroll_into(self, element):
        el = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

    def load_js(self):
        self.driver.execute_script(JSFunctions.click)
        self.driver.execute_script(JSFunctions.enter_text)
        self.driver.execute_script(JSFunctions.get_row_sibling)


    def pagetest_headers(self):
        pass

    def pagetest_ip(self):
        pass

    def pagetest_recaptchav3(self):
        pass

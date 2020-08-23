#!/usr/bin/env python
# -*- coding: utf-8 -*-
from inspect import getsource
from selenium.webdriver.common.by import By
from codelib.automation_testing.selenium_automation.selenium_automation.pages.base import BasePage  # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.timeunits import five, two, thirty  # noqa


"""Selectors and data used on google.com
"""
google_com = "http://google.com"
search_input = (By.XPATH, '//*[@name="q"]')
search_images = (By.LINK_TEXT, "Grafika")  # for polish google
first_result = "return document.querySelector('#rg_s :first-child img').src;"
test_arguments = "console.log(arguments[0]);alert(arguments[0]);"

alert = "alert('No ja się mam wyświetlić.');"  # test alert
the_argument = "No ja się mam wyświetlić."

search_result_selector = "div.g"
image_search_result_selector = "div.rg_bx.rg_di.rg_el.ivg-i"


class GoogleSearch(BasePage):
    """Actions for Google Search
    """

    def search(self, phrase):
        self.open(google_com)

        self.b.clear_field(search_input)
        self.b.enter_text(phrase, search_input)
        self.b.press_key('ENTER', search_input)
        self.b.sleep(two)
        self.b.wait_for(self.b.title_contains(phrase), thirty)
        return self.source()

    def show_images(self):
        self.b.click(search_images)
        self.b.wait(five)
        self.b.sleep(two)
        return self.source()

    def download_first_image(self):
        self.b.sleep(two)
        self.b.take_screenshoot()
        self.b.download_src(first_result)

    def test_alert(self):
        self.b.execute_script(alert)
        return True

    def test_script_arguments(self):
        self.b.wait(five)
        self.b.execute_script(test_arguments, the_argument)
        self.b.accept_alert()
        self.b.sleep(five)
        self.b.take_screenshoot()
        self.b.sleep(two)

    def find_image(self, phrase):
        search = self.search(phrase)
        return self.show_images()

    def search_phrase(self, phrase):
        return self.search(phrase)

    def get_page_source(self, page):
        self.b.open_page(page)
        return self.source()

    def do_several_things(self, phrase):
        search = self.search(phrase)
        images = self.show_images()
        alert = self.test_alert()
        return search, images, alert

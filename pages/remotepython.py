#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from codelib.automation_testing.selenium_automation.selenium_automation.pages.base import \
    BasePage
from codelib.automation_testing.selenium_automation.selenium_automation.timeunits import \
    five

__all__ = []

url = "https://www.remotepython.com"

search = (By.XPATH, "//input[@name='q']")

search_result = ".item"
link = ".item h3 > a"  # for link and text


class RemotePython(BasePage):
    """Actions for We Work Remotely
    """

    def search(self, phrase):
        self.open(url)

        self.b.clear_field(search)
        # click remote and wait
        self.b.enter_text(phrase, search)
        self.b.press_key('ENTER', search)
        self.b.sleep(five)

        return self.source()
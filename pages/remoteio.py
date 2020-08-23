#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from codelib.automation_testing.selenium_automation.selenium_automation.pages.base import \
    BasePage
from codelib.automation_testing.selenium_automation.selenium_automation.timeunits import \
    five

url = "https://remoteok.io/"

search = (By.CLASS_NAME, "search")

jobs = ".job"


class Remoteio(BasePage):
    """Actions for We Work Remotely
    """

    def search(self, phrase):
        self.open(url)

        self.b.clear_field(search)
        self.b.enter_text(phrase, search)
        self.b.press_key('ENTER', search)
        self.b.sleep(five)

        return self.source()
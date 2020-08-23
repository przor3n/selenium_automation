#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from codelib.automation_testing.selenium_automation.selenium_automation.pages.base import \
    BasePage
from codelib.automation_testing.selenium_automation.selenium_automation.timeunits import \
    five

__all__ = []

url = "https://stackoverflow.com/jobs"
search = (By.ID, 'q')
remote = (By.ID, 'r')
jobs = ".listResults .-item.-job .-job-summary"


class StackJobs(BasePage):
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

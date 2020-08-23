#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from codelib.automation_testing.selenium_automation.selenium_automation.pages.base import \
    BasePage
from codelib.automation_testing.selenium_automation.selenium_automation.timeunits import \
    five

url = "https://jobs.github.com/"

search = (By.ID, "description_field")
location_field = (By.ID, "location_field")
job = ".job"


class GithubJobs(BasePage):
    """Actions for We Work Remotely
    """

    def search(self, phrase, location=None):
        self.open(url)

        if location:
            self.b.clear_field(location_field)
            self.b.enter_text(location, location_field)
            self.b.wait(five)

        self.b.clear_field(search)
        self.b.enter_text(phrase, search)
        self.b.press_key('ENTER', search)
        self.b.sleep(five)

        return self.source()
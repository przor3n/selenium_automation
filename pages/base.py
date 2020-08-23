#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from selenium_automation.browsers import \
    Browser
from selenium_automation.timeunits import \
    five, one, two


class BasePage:
    def __init__(self, browser: Browser):
        self.b = browser

    def open(self, url):
        """Open URL"""
        self.b.open_page(url)
        self.b.wait(five)

    def enter_text(self, text, element):
        """Enter text into input"""
        self.b.scroll_into(element)
        self.b.click(element)
        self.b.wait(two)
        try:
            self.b.type_text(text)
        except WebDriverException:
            pass
        self.b.wait(one)

    def source(self):
        """Get the page source"""
        return self.b.get_page_source()

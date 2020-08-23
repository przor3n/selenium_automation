#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from codelib.automation_testing.selenium_automation.selenium_automation.pages.base import \
    BasePage
from codelib.automation_testing.selenium_automation.selenium_automation.timeunits import \
    two, five, one


class Luxmed(BasePage):
    """Actions for Luxmed Portal
    """

    URL = 'https://portalpacjenta.luxmed.pl/PatientPortal/Account/LogOn'

    USERNAME = ''
    PASSWORD = ''

    # login page
    LOGIN_INPUT = (By.ID, 'Login')
    PASSWORD_INPUT = (By.ID, 'TempPassword')
    # PASSWORD_INPUT = (By.ID, 'Password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.button.large.green')

    VISIT_BUTTON = (By.CSS_SELECTOR, '.button.accept.calendar.bg-green')

    PLACOWKA_BUTTON = (By.PARTIAL_LINK_TEXT, 'Wizyta w placówce')

    # SELECT_CITY = (By.XPATH, '//*[text()="Wybierz miasto"]')
    SELECT_CITY = (By.XPATH,
                      '/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/form/div[1]/div[1]/div[1]/div/div/div[1]')

    # CITY = (By.XPATH, '//li[text()="Warszawa"]')
    CITY = (By.XPATH, '//ul[@id="__selectOptions"]/li[@class=""]')

    # SELECT_SERVICE = (By.XPATH, '//*[text()="Wybierz usługę"]')
    # SELECT_SERVICE = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/form/div[1]/div[2]/div[1]/div/div/div[1]')
    SELECT_SERVICE = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/form/div[1]/div[2]/div[1]/div/div/div[1]')
    SERVICE = (By.XPATH, '//li[text()="Konsultacja okulisty"]')
    SERVICE = (By.XPATH, '//ul[@id="__selectOptions"]/li[@class=""]')



    def accept_cookies(self):
        # cookies_div = (By.CSS_SELECTOR, 'cookies')
        cookies_link = (By.PARTIAL_LINK_TEXT, 'ZAMKNIJ')

        cookies = self.b.find(cookies_link)
        cookies.click()

    def login(self):
        self.open(self.URL)

        self.accept_cookies()

        self.enter_text(self.USERNAME, self.LOGIN_INPUT)
        self.enter_text(self.PASSWORD, self.PASSWORD_INPUT)

        self.b.click(self.SUBMIT_BUTTON)
        self.b.sleep(five)

    def open_visits(self):
        self.b.click(self.VISIT_BUTTON)
        self.b.wait(two)

        self.b.click(self.PLACOWKA_BUTTON)
        self.b.wait(two)

        self.b.click(self.SELECT_CITY)
        self.b.type_text('Warszawa')
        self.b.wait(one)
        self.b.click(self.CITY)
        self.b.wait(two)

        self.b.click(self.SELECT_SERVICE)
        self.b.type_text('Konsultacja okulisty')
        self.b.wait(one)
        self.b.click(self.SERVICE)
        self.b.wait(two)

        sleep(200)

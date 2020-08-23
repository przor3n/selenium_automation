#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, FirefoxProfile
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as CHOptions

from codelib.automation_testing.selenium_automation.selenium_automation.commands import Commands  # noqa

STANDALONE = "http://127.0.0.1:4444/wd/hub"
STANDALONE_FF = "http://172.17.0.4:4444/wd/hub"
HUB = "http://172.30.0.2:4444/wd/hub"
FIREFOX_PROFILE_DIR = '/home/red/WAREHOUSE/profiles/automat_firefox'

class UserAgent:
    HTTP_USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    ]

    @classmethod
    def get(cls):
        return cls.HTTP_USER_AGENTS[3]


class Browser(Commands):
    """Browser object
    It has driver instance set with default settings.
    Inherits Commands, that are basic user actions.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.delete_all_cookies()
        # self.driver.fullscreen_window()

    def restart(self):
        self.driver.start_client()

    def clean(self):
        self.driver.quit()


def firefox_profile():
    profile = FirefoxProfile(FIREFOX_PROFILE_DIR)
    # profile.setPreference("browser.download.dir",
                          # "C:\\Users\\Admin\\Desktop\\ScreenShot\\");
    # profile.setAssumeUntrustedCertificateIssuer(false);
    # profile.setEnableNativeEvents(false);
    # profile.setPreference("network.proxy.type", 1);
    # profile.setPreference("network.proxy.http", "localHost");
    # profile.setPreference("newtwork.proxy.http_port", 3128);
    return profile

def firefox_options():
    options = FFOptions()
    # options.add_argument("-headless")
    return options


def chrome_options():
    options = CHOptions()
    #     options.add_argument('--load-images=no')
    #     options.add_argument('--incognito')  # optional
    options.add_experimental_option("prefs", {
        "download.default_directory": tempfile.mkdtemp(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        'safebrowsing.enabled': False,
        'safebrowsing.disable_download_protection': True,
    })
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-web-security')
    options.add_argument('--ignore-ssl-errors=true'),
    options.add_argument('--ssl-protocol=any')
    options.add_argument('--disable-infobars')
    options.add_argument('--user-agent=%s' % UserAgent().get())
    # options.add_argument('--lang=%s' % LANG)
    options.add_argument('--hide-scrollbars')
    options.add_argument('--mute-audio')
    options.add_argument('--enable-logging=stderr')
    options.add_argument('--v=1')
    options.add_argument('--start-maximized')


    # options.add_extension('/tmp/proxy.zip')
    options.add_argument('proxy-server=localhost:8080')
    return options

def chrome_service():
    service = []

    service += ['--proxy-server=localhost:8080']
    service += ['--proxy=localhost:8080']
    service += ['--proxy-type=https']

    return service

class DriverFactory:
    """Webdriver factory
    """
    @staticmethod
    def local():
        return webdriver.Firefox(
            firefox_profile=firefox_profile(),
            options=firefox_options(),
        )

    @staticmethod
    def chrome():
        return webdriver.Chrome(
            options=chrome_options()
        )

    @staticmethod
    def local_headless():
        """Headless version"""
        options = FFOptions()
        options.add_argument("-headless")
        return webdriver.Firefox(options=options)

    @staticmethod
    def remote_chrome():
        """Remote standalone"""
        return webdriver.Remote(
            command_executor=STANDALONE,
            desired_capabilities=DesiredCapabilities.CHROME)

    @staticmethod
    def remote_firefox():
        """Remote standalone"""
        return webdriver.Remote(
            command_executor=STANDALONE_FF,
            desired_capabilities=DesiredCapabilities.FIREFOX)

    @staticmethod
    def remote_chrome_headless():
        """Remote standalone headless version"""
        options = CHOptions()
        options.add_argument("--headless")
        return webdriver.Remote(
            command_executor=STANDALONE,
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options)

    @staticmethod
    def hub():
        return webdriver.Remote(
            command_executor=HUB,
            desired_capabilities=DesiredCapabilities.CHROME)

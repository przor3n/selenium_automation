#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, FirefoxProfile
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as CHOptions

from selenium_automation import log
from selenium_automation.utils import get_file_generator
from selenium_automation.words import *
from selenium_automation.config import config

class UserAgent:
    HTTP_USER_AGENTS = [
        # Chrome versions 58 - 64
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
    ]

    @classmethod
    def get(cls):
        return cls.HTTP_USER_AGENTS[3]


def firefox_arguments():
    log.info("Building Firefox arguments ...")
    args = {}
    opt = FFOptions()

    _profile = config[firefox].get(profile, fallback=None):
    if _profile:
        # profile.setPreference("browser.download.dir",
        # "C:\\Users\\Admin\\Desktop\\ScreenShot\\");
        # profile.setAssumeUntrustedCertificateIssuer(false);
        # profile.setEnableNativeEvents(false);
        # profile.setPreference("network.proxy.type", 1);
        # profile.setPreference("network.proxy.http", "localHost");
        # profile.setPreference("newtwork.proxy.http_port", 3128);
        args[firefox_profile] = FirefoxProfile(_profile)


    _arguments = config[firefox].get(arguments, fallback=None):
    if _arguments:


        for arg in get_file_generator(_arguments):
            opt.add_argument(arg)

    _extensions = config[firefox].get(extensions, fallback=None)
    if _extensions:
        for ext in _extensions.split(';'):
            if not ext:
                continue

            opt.add_extension(ext)

    args[options] = opt

    return args

def chrome_arguments():
    log.info("Building Chrome arguments...")
    args = {}
    opt = CHOptions()

    _arguments = config[chrome].get(arguments, fallback=None):
    if _arguments:

        for arg in get_file_generator(_arguments):
            opt.add_argument(arg)

    _extensions = config[chrome].get(extensions, fallback=None)
    if _extensions:
        for ext in _extensions.split(';'):
            if not ext:
                continue

            opt.add_extension(ext)


    args[options] = opt

    return args


# Browser initializers


def Firefox():
    """Local instance"""
    log.info("Initiating Firefox")
    args = firefox_arguments()

    return webdriver.Firefox(
        **args
    )


def Chrome():
    """Local instance"""
    log.info("Initiating Chrome")
    args = chrome_arguments()

    return webdriver.Chrome(**args)


def Remote():
    """Load remote instances"""
    log.info("Initiating Remote")
    _name = config[browser][name]

    browser = DesiredCapabilities.CHROME if _name == chrome else DesiredCapabilities.FIREFOX
    args = chrome_arguments() if _name == chrome else firefox_arguments()

    url = config[remote][url]


    return webdriver.Remote(
            command_executor=url,
            desired_capabilities=browser,
            **args
        )


# list of browsers that are handled
browsers = {
    (local, firefox,): Firefox,
    (local, chrome,): Chrome,
    (remote, firefox,): Remote,
    (remote, chrome,): Remote,
    (remote, hub,): Remote,
}


def build_driver():
    """That was defined in the config file"""
    log.info("Building instance...")
    _where = config[browser][where]
    _name = config[browser][name]

    instance = browsers.get((_where, _name,), None)

    assert instance, "We don't have a browser instance"|

    return instance()


# finally, the instance is created and
# available to import
driver = build_driver()
log.info("Driver runs...")

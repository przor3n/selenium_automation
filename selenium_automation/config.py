#!/usr/bin/env python3
import configparser
import os
from selenium_automation import log


def load_config():
    log.info('Loading config')
    config_file = os.getenv('SELENIUM_AUTOMATION_CONFIG')

    config = configparser.ConfigParser(allow_no_value=True)
    config.read_string(config_file)

    return config

config = load_config()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from codelib.automation_testing.selenium_automation\
    .selenium_automation.browsers import Browser, DriverFactory      # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.pages.google import \
    GoogleSearch, image_search_result_selector, \
    search_result_selector  # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.pages.luxmed import \
    Luxmed
from codelib.automation_testing.selenium_automation.\
    selenium_automation.runner import Runner    # noqa
from codelib.parsing.beautifulsoup import load_html

"""Luxmed Robots
"""


def luxmed_scenarios(scenario):
    def luxmed_robot(driver):
        tools = {
            'b': Browser(driver)
        }

        slots = {
            'luxmed': Luxmed(tools['b']),
        }

        try:
            runner = Runner(tools, slots, scenario)
            runner.do()
            runner.clean()

            return runner.output

        except Exception as e:
            print(e)
            raise e
    return luxmed_robot


login_luxmed = luxmed_scenarios("output = luxmed.login()\nluxmed.open_visits()")

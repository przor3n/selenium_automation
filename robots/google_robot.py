#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from selenium_automation.browsers import Browser, DriverFactory      # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.pages.google import \
    GoogleSearch, image_search_result_selector, \
    search_result_selector  # noqa
from codelib.automation_testing.selenium_automation.\
    selenium_automation.runner import Runner    # noqa
from codelib.parsing.beautifulsoup import load_html

"""Google Robots
"""


def google_scenarios(scenario):
    def google_robot(phrase, driver):
        tools = {
            'b': Browser(driver)
        }

        slots = {
            'google': GoogleSearch(tools['b']),
            'phrase': phrase
        }

        try:
            runner = Runner(tools, slots, scenario)
            runner.do()
            runner.clean()

            return runner.output

        except Exception as e:
            print(e)
            raise e
    return google_robot


search_google = google_scenarios("output = google.search_phrase(phrase)")
search_google_images = google_scenarios("output = google.find_image(phrase)")


def parse_search_results(page):
    results = page.select(search_result_selector)

    results = filter(lambda x: len(x['class']) == 1, results)

    for markup in list(results):

        link = markup.select(".r > a")
        heading = markup.select("h3")
        desc = markup.select(".st")

        proper_row = desc and link and heading

        if not proper_row:
            continue

        data = {
            'title': heading[0].text,
            'url': link[0]['href'],
            'desc': desc[0].text
        }

        yield data


def parse_image_search_results(page):
    results = page.select(image_search_result_selector)

    for markup in results:

        content_json = markup.select_one('.rg_meta.notranslate')
        content = json.loads(content_json.text)

        data = {
            'title': content['pt'],
            'url': content['ou'],
            'desc': ""
        }

        yield data


def search_images(phrase):
    page = search_google_images(phrase, DriverFactory.local())
    return list(parse_image_search_results(load_html(page)))


def search_phrase(phrase):
    page = search_google(phrase, DriverFactory.local())
    return list(parse_search_results(load_html(page)))

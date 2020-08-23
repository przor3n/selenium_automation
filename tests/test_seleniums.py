#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

import pytest
import queue

from codelib.automation_testing.selenium_automation.selenium_automation.browsers import DriverFactory   # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.robots.google_robot import search_google, parse_search_results     # noqa
from codelib.parsing.beautifulsoup import load_html


drivers = [
    'local',
    'local_headless',
    'remote_chrome',
    'remote_chrome_headless',
    'remote_firefox',
    'hub']

search_words = ["Sun", "Moon", "Mars", "Jupiter", "Neptune"]


@pytest.mark.skip
def test_hub():
    short_set = search_words[:4]
    assert 4 == len(short_set)  # it has 4 elements

    for phrase in short_set:
        s = search_google(phrase, DriverFactory.hub())

        assert isinstance(s, str)
        s = load_html(s)

        title = s.title.string
        assert title.startswith(phrase)


@pytest.mark.skip
def test_local():
    phrase = "Saturn"

    for driver in drivers[:2]:
        s = search_google(phrase, getattr(DriverFactory, driver)())

        assert isinstance(s, str)
        s = load_html(s)

        title = s.title.string
        assert title.startswith(phrase)


@pytest.mark.skip
def test_remote_firefox():
    phrase = "Saturn"
    s = search_google(phrase, DriverFactory.remote_firefox())

    assert isinstance(s, str)
    s = load_html(s)

    title = s.title.string
    assert title.startswith(phrase)


def test_remote_chrome():
    phrase = "Saturn"
    s = search_google(phrase, DriverFactory.remote_chrome())

    assert isinstance(s, str)
    s = load_html(s)

    title = s.title.string
    assert title.startswith(phrase)


@pytest.mark.skip
def test_thread_hub():

    r = []
    q = queue.Queue()

    threads = []

    def worker():
        phrase = q.get()
        page = search_google(phrase, DriverFactory.hub())
        results = parse_search_results(load_html(page))
        r.append(results)

    for i in range(4):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for item in search_words[:4]:
        q.put(item)

    q.join()

    for t in threads:
        t.join()

    assert True


if __name__ == "__main__":
    pytest.main([__file__])

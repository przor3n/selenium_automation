#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from codelib.automation_testing.selenium_automation.selenium_automation.robots.google_robot import parse_search_results     # noqa
from codelib.files.read_write import get_file_contents
from codelib.files.system import file_sibling
from codelib.parsing.beautifulsoup import load_html

test_page = "google_result_test_page"
test_page_content = get_file_contents(file_sibling(__file__, test_page))


def test_retrive_data():

    search_page = load_html(test_page_content)

    results = list(parse_search_results(search_page))

    assert isinstance(results, list)

    first = results[0]

    assert first['title']
    assert first['url']
    assert first['desc']


if __name__ == "__main__":
    pytest.main([__file__])

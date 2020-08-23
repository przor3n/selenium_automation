#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from codelib.automation_testing.selenium_automation.selenium_automation.browsers import \
    DriverFactory
from codelib.automation_testing.selenium_automation.selenium_automation.robots.luxmed_robot import \
    login_luxmed


def test_luxmed_robot():
    visits = []
    # images = search_images(phrase)

    function = login_luxmed(DriverFactory.local())
    function()

    assert False


if __name__ == "__main__":
    pytest.main([__file__])

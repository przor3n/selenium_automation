#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from codelib.automation_testing.selenium_automation.selenium_automation.robots.google_robot import search_images, search_phrase     # noqa


def test_google_robot():
    phrase = "Sun"

    # images = search_images(phrase)

    links = search_phrase(phrase)

    # assert len(images) > 0
    assert len(links) > 0


if __name__ == "__main__":
    pytest.main([__file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from codelib.automation_testing.selenium_automation.selenium_automation.runner import Runner    # noqa


class FObject:
    """Fixture object
    it will be used to test
    basic functions of the Runner"""

    def __init__(self, value):
        self.value = value

    def action(self, number):
        return number + 1

    def clean(self):
        self.value = None


tool_value = 10

tool = FObject(tool_value)

slots = {
    'value': 5
}

tools = {
    'tool': tool
}


def test_runner():
    instructions = """\n
output = tool.action(value)
    """

    runner = Runner(tools, slots, instructions)
    runner.do()

    assert runner.output == 6  # action has been done
    assert tool.value == tool_value  # things that dont change - dont change

    runner.clean()  # clean the tools after work

    assert tool.value is None  # this should be None


def test_runner_exception():
    instructions = """\n
1/0
    """

    runner = Runner(tools, slots, instructions)
    catched = None

    try:
        runner.do()
    except Exception as e:
        catched = e

    assert isinstance(runner.output, type(catched))


if __name__ == "__main__":
    pytest.main([__file__])

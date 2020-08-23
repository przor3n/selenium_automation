import pytest

from codelib.automation_testing.selenium_automation.selenium_automation.browsers import Browser, DriverFactory      # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.pages.google import GoogleSearch    # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.pages.google import scenario_get_page_source, scenario_do_several_things  # noqa
from codelib.automation_testing.selenium_automation.selenium_automation.runner import Runner    # noqa
from codelib.parsing.beautifulsoup import load_html


def execute_runner(t, s, i):
    runner = Runner(t, s, i)
    runner.do()

    return runner


@pytest.fixture
def toolbox():
    tools = {
        'b': Browser(DriverFactory.local_headless())
    }

    slots = {
        'google': GoogleSearch(tools['b']),
        'phrase': "doge memes"
    }

    return tools, slots


def test_selenium_automation(toolbox):
    tools, slots = toolbox

    try:
        runner = execute_runner(tools, slots, scenario_get_page_source)
    except Exception as e:
        print(e)
        runner = None

    assert runner

    page = load_html(runner.output)
    assert page.title.string == "Google"

    runner.clean()


def test_selenium_find_doge(toolbox):
    tools, slots = toolbox

    try:
        runner = execute_runner(tools, slots, scenario_do_several_things)
    except Exception as e:
        print(e)
        runner = None

    assert runner

    search, images, alert = runner.output

    assert load_html(search).title.string.startswith("doge memes")
    assert alert

    runner.clean()


if __name__ == "__main__":
    pytest.main([__file__])

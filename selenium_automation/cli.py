# -*- coding: utf-8 -*-

"""Console script for copypaster."""
import os
import sys
import click
from selenium_automation import log, PROJECT_DIR
from selenium_automation.config import config
from selenium_automation.runner import Runner

default_config_path = os.path.join(PROJECT_DIR, "config/example.conf")


@click.command()
@click.argument('script')
def main(script):
    log.info("Started Selenium_Automation")

    assert script, "No script file"

    instructions = None
    with open(script, 'r') as f:
        instructions = f.read()

    runner = Runner({}, instructions)

    try:
        from selenium_automation.commands import command_list

        runner.prepare(command_list)

        runner.do()
        runner.clean()

        output = runner.output
        print(output)

        with open('output.data', 'w') as f:
            f.write(output)

        log.info("Finished task")
    except Exception as e:
        log.info(e)
    finally:
        runner.clean()


if __name__ == "__main__":
    sys.exit(main(None))  # pragma: no cover

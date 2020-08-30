#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium_automation import log

class Runner:
    def __init__(self, tools, instructions):

        self.tools = tools
        self.instructions = instructions


        self.output = None


        self.on = True
        self.single_run = True

        self.environment = {
            'runner': self
        }
        self.environment.update(tools)

    def prepare(self, data):
        self.environment.update(data)

    def do(self):
        while self.on:
            try:
                # execute instuctions
                # pass buitins and other stuff
                # pass prepared environment
                exec(self.instructions, globals(), self.environment)
            except Exception as e:
                log.error(e)
                raise e
            finally:
                self.last_checks()

    def last_checks(self):
        """Here we do stuff on every run"""
        if self.single_run:
            self.on = False

        self.output = self.environment.get('output', None)

    def clean(self):
        """Run cleanup"""
        for _, tool in self.tools.items():
            tool.clean()

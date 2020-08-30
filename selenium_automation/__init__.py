#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Selenium automation

This module is about Selenium webdriver
and code to some related ideas.
"""
import logging
import os

# usefull paths
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)


log = logging.getLogger('SeleniumAutomation')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

log.addHandler(ch)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codelib.files.system import file_sibling
from codelib.parsing.configs import read_config_file as read_script_from

jspath = file_sibling(__file__, 'jsfunctions.config')
script = read_script_from(jspath)


class JsFunctions:
    pass


JSFunctions = JsFunctions()

for name, func in script['functions'].items():
    setattr(JSFunctions, name, func)

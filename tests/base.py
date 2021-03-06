#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of LibToHttp.
# https://github.com/Utsav2/LibToHttp

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Utsav Shah <ukshah2@illinois.edu>

from unittest import TestCase as PythonTestCase
from LibToHttp import router


class TestCase(PythonTestCase):
    ''' base class for all LibToHttp tests '''
    def setUp(self):
        router.config.API_ROUTES_ENABLED = True
        router.reset()

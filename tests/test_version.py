#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of LibToHttp.
# https://github.com/Utsav2/LibToHttp

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Utsav Shah <ukshah2@illinois.edu>

from LibToHttp import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        self.assertEquals(__version__, '0.1.0')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ramapi` package."""


import unittest

from ramapi import ramapi
from ramapi.ramapi import * 



class TestRamapi(unittest.TestCase):

    def testapi_info(self):
        response=ramapi.Base.api_info()['characters']
        self.assertEqual(response,"https://rickandmortyapi.com/api/character")


    
if __name__ == '__main__':
    unittest.main()
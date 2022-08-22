'''
Doc
'''
from __future__ import (absolute_import, division, print_function)
import unittest
__metaclass__ = type


class AddTester(unittest.TestCase):
    '''
    Doc
    '''
    a = 10
    b = 23

    # this function will
    def test_add(self):
        '''
        Doc
        '''
        c_var = 33
        assert self.a + self.b == c_var

    # this function will
    def test_subtract(self):
        '''
        Doc
        '''
        c_var = -13
        assert self.a - self.b == c_var

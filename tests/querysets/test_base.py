# -*- coding:utf-8 -*-

import unittest2

from swf.querysets.base import BaseQuerySet


class TestBaseQuerySet(unittest2.TestCase):

    def setUp(self):
        self.base_qs = BaseQuerySet()

    def tearDown(self):
        pass

    def test_get_method_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.base_qs.get()

    def test_filter_method_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.base_qs.filter()

    def test_all_method_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.base_qs.all()

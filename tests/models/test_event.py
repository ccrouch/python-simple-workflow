# -*- coding:utf-8 -*-

import unittest2

from swf.models.event import Event, History

from ..mocks.event import mock_get_workflow_execution_history


class TestEvent(unittest2.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instantiate_with_invalid_type(self):
        with self.assertRaises(ValueError):
            Event("WrongType")


class TestHistory(unittest2.TestCase):

    def setUp(self):
        self.event_list = mock_get_workflow_execution_history()
        self.history = History.from_event_list(self.event_list['events'])

    def tearDown(self):
        pass

    def test_get_by_valid_index(self):
        val = self.history[0]
        self.assertIsNotNone(val)
        self.assertIsInstance(val, Event)

    def test_get_by_invalid_index(self):
        with self.assertRaises(IndexError):
            self.history[42]  # mocked event list doesn't have 43 indexes

    def test_get_by_valid_slice(self):
        val = self.history[0:1]
        self.assertIsNotNone(val)
        self.assertIsInstance(val, History)
        self.assertEqual(len(val.container), 1)

    def test_get_by_invalid_slice(self):
        h = self.history[45:99]
        self.assertIsNotNone(h)
        self.assertIsInstance(h, History)
        self.assertEqual(len(h.container), 0)

    def test_get_by_invalid_index_type(self):
        with self.assertRaises(TypeError):
            self.history["invalid, bitch"]

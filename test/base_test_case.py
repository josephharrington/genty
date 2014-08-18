# coding: utf-8

from __future__ import unicode_literals
import six
from unittest import TestCase


# pylint: disable=no-member
class BaseTestCase(TestCase):

    if six.PY3:
        # assertItemsEqual was combined with assertCountEqual
        assertItemsEqual = TestCase.assertCountEqual

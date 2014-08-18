# coding: utf-8

from __future__ import unicode_literals
import six


def format_kwarg(key, value):
    """
    Return a string of form:  "key=<value>"

    If 'value' is a string, we want it quoted. The goal is to make
    the string a named parameter in a method call.
    """
    return '{}={}'.format(key, format_arg(value))


def format_arg(value):
    """
    :param value:
        Some value in a dataset.
    :type value:
        varies
    :return:
        unicode representation of that value
    :rtype:
        `unicode`
    """
    translator = repr if isinstance(value, six.string_types) else six.text_type
    return translator(value)


def encode_non_ascii_string(string):
    """
    :param string: The string to be encoded
    :type string: str
    :return: The encoded string
    :rtype: str
    """
    encoded_string = string.encode('utf-8', 'replace')
    # In Python 3, str.encode() returns bytes, so convert it back to str
    if six.PY3:
        encoded_string = encoded_string.decode()

    return encoded_string

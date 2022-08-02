#!/usr/bin/python3
"""Module 6-from_json_string.
Returns an object (Python data structure)
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Return the object represented my my_str.

    Args:
        - my_str: JSON string representation

    Returns: corresponding object
    """

    return json.loads(my_str)

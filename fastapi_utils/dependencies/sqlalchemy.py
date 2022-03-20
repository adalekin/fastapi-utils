import json
from typing import Optional


def filter_spec(filter: Optional[str] = None):
    if filter:
        return json.loads(filter)


def sort_spec(sort: Optional[str] = None):
    if sort:
        return json.loads(sort)

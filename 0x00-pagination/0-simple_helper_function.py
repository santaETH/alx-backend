#!/usr/bin/env python3
"""Pagination simple  helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

#!/usr/bin/env python3
"""Pagination Simple helper function.
Write a function named index_range that 
takes two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of start and end index for a given pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

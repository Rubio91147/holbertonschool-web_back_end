#!/usr/bin/env python3
'''Replicate code from the previous task.

Implement a get_hyper method that takes
 the same arguments (and defaults) as get_page and returns
   a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.'''


import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ That return a list with the values of the index"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index: tuple = index_range(page, page_size)

        return self.dataset()[index[0]: index[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' That return a range of indexes '''
    return ((page_size * page) - page_size, page_size * page)

import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self._collection)

    # returns the number of pages
    def page_count(self):
        return int(math.ceil(1.0 * self.item_count() / self._items_per_page))

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if (page_index + 1) * self._items_per_page <= self.item_count():
            return self._items_per_page

        if page_index * self._items_per_page < self.item_count() < (page_index + 1) * self._items_per_page:
            return self.item_count() % self._items_per_page

        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if self.item_count() > item_index >= 0:
            return item_index / self._items_per_page

        return -1

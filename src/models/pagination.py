import math

# Dto untuk pagination
class Pagination:
    def __init__(self, total_row: int, page: int, size: int):

        total_page = int
        if size > 0:
            total_page = math.ceil(total_row / size)
        else:
            total_page = 1

        if total_page == 0:
            total_page = 1

        has_more = bool
        if total_page-page < 1:
            has_more = False
        else:
            has_more = True

        self.total_row = total_row
        self.total_page = total_page
        self.page = page
        self.size = size
        self.has_more = has_more

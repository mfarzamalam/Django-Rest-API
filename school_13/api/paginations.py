from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_num'
    page_size_query_param = 'record'
    max_page_size  = 7
    last_page_strings = ('last','end')


class CustomLimitOffset(LimitOffsetPagination):
    default_limit      = 5
    limit_query_param  = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit          = 6
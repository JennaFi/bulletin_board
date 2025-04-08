from rest_framework.pagination import PageNumberPagination


class ProductPaginator(PageNumberPagination):
    """Paginate list of announcements by 4 product """

    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

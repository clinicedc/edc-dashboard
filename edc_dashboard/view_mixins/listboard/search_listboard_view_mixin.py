from django.utils.html import escape
from django.db.models import Q
from django.utils.text import slugify


class SearchListboardMixin:

    search_fields = ["slug"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._search_term = None

    def extra_search_options(self, search_term):
        """Returns a list of search Q() objects that will be added to the
        search criteria (OR) for the search queryset.
        """
        return None

    def clean_search_term(self, search_term):
        return search_term

    @property
    def search_term(self):
        if not self._search_term:
            search_term = self.request.GET.get("q")
            if search_term:
                search_term = escape(search_term).strip()
            search_term = self.clean_search_term(search_term)
            self._search_term = search_term
        return self._search_term

    @property
    def search_terms(self):
        return self.search_term.split("+")

    def get_search_filtered_queryset(self, filter_options=None, exclude_options=None):
        q = None
        q_objects = []
        for search_term in self.search_terms:
            for field in self.search_fields:
                q_objects.append(Q(**{f"{field}__icontains": slugify(search_term)}))
            extra_q_objects = self.extra_search_options(search_term)
            if extra_q_objects:
                q_objects.extend(extra_q_objects)
        for q_object in q_objects:
            if q:
                q = q | q_object
            else:
                q = q_object
        if q:
            queryset = (
                getattr(self.listboard_model_cls, self.listboard_model_manager_name)
                .filter(q, **filter_options)
                .exclude(**exclude_options)
            )
        else:
            queryset = (
                getattr(self.listboard_model_cls, self.listboard_model_manager_name)
                .filter(**filter_options)
                .exclude(**exclude_options)
            )
        return queryset

    def get_filtered_queryset(self, filter_options=None, exclude_options=None):
        """Override to add conditional logic to filter on search term.
        """
        if self.search_term and "|" not in self.search_term:
            queryset = self.get_search_filtered_queryset(
                filter_options=filter_options, exclude_options=exclude_options
            )
        else:
            queryset = super().get_filtered_queryset(
                filter_options=filter_options, exclude_options=exclude_options
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

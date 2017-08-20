from ...listboard_filter import ListboardViewFilters


class ListboardFilterViewMixin:

    listboard_view_filters = ListboardViewFilters()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.listboard_view_exclude_filter_applied = False
        self.listboard_view_include_filter_applied = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            listboard_view_filters=self.listboard_view_filters.filters)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        self.listboard_view_include_filter_applied = False
        for listboard_filter in self.listboard_view_filters.include_filters:
            if self.request.GET.get(listboard_filter.attr) == listboard_filter.name:
                lookup_options = listboard_filter.lookup_options
                if lookup_options:
                    options.update(**listboard_filter.lookup_options)
                self.listboard_view_include_filter_applied = True
        if (not self.listboard_view_include_filter_applied
                and self.listboard_view_filters.default_include_filter):
            options.update(
                **self.listboard_view_filters.default_include_filter.lookup_options)
        return options

    def get_queryset_exclude_options(self, request, *args, **kwargs):
        options = super().get_queryset_exclude_options(
            request, *args, **kwargs)
        self.listboard_view_exclude_filter_applied = False
        for listboard_filter in self.listboard_view_filters.exclude_filters:
            if self.request.GET.get(listboard_filter.attr) == listboard_filter.name:
                lookup_options = listboard_filter.lookup_options
                if lookup_options:
                    options.update(**listboard_filter.lookup_options)
                self.listboard_view_exclude_filter_applied = True
        if (not self.listboard_view_exclude_filter_applied
                and not self.listboard_view_include_filter_applied
                and self.listboard_view_filters.default_exclude_filter):
            options.update(
                **self.listboard_view_filters.default_exclude_filter.lookup_options)
        return options
from interface import implements

from zipline.utils.compat import contextmanager

from .iface import PipelineHooks


class NoHooks(implements(PipelineHooks)):
    """A PipelineHooks that defines no-op methods for all available hooks.

    Use this as a base class if you only want to implement a subset of all
    possible hooks.
    """
    def on_create_execution_plan(self, plan):
        pass

    @contextmanager
    def running_pipeline(self, pipeline, start_date, end_date):
        yield

    @contextmanager
    def computing_chunk(self, plan, start_date, end_date):
        yield

    @contextmanager
    def loading_terms(self, terms):
        yield

    @contextmanager
    def computing_term(self, term):
        yield

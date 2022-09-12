import mock

is_test_page = mock.Mock()


def include_setup_and_teardown_pages(page_data, is_suite):
    pass


def render_page_with_setups_and_teardowns(page_data, is_suite):
    if is_test_page(page_data):
        include_setup_and_teardown_pages(page_data, is_suite)
        return page_data.getHtml()

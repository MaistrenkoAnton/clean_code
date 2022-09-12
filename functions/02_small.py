import mock

is_test_page = mock.Mock()
include_setup_and_teardown_pages = mock.Mock()

# The first rule of functions is that they should be small (max 4 lines)


def render_page_with_setups_and_teardowns(page_data, is_suite):
    if is_test_page(page_data):
        include_setup_and_teardown_pages(page_data, is_suite)
        return page_data.getHtml()

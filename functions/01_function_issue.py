import mock


StringBuffer = mock.Mock()
page_crawler_impl = mock.Mock()
suite_responder = mock.Mock()
path_parser = mock.Mock()
include_setup_pages = mock.Mock()
include_teardown_pages = mock.Mock()

# FitNesse product
# Not only is it long, but it’s got duplicated
# code, lots of odd strings, and many strange and inobvious data types and APIs. See how
# much sense you can make of it in the next three minutes.


def testable_html(page_data, include_suit_setup):
    wiki_page = page_data.get_wiki_page()
    buffer = StringBuffer()
    if page_data.has_attribute('Test'):
        if include_suit_setup:
            suite_setup = page_crawler_impl.get_inherit_page(suite_responder.SUITE_SETUP_NAME, wiki_page)
            if suite_setup is not None:
                page_path = suite_setup.get_page_crawler().get_full_path(suite_setup)
                page_path_name = path_parser.render(page_path)
                buffer.append("!include -setup .").append(page_path_name).append("\n")

        setup = page_crawler_impl.get_inherit_page("SetUp", wiki_page)
        if setup is not None:
            setup_path = wiki_page.get_page_crawler().get_full_path(setup)
            setup_path_name = path_parser.render(setup_path)
            buffer.append("!include -setup .").append(setup_path_name).append("\n")
    buffer.append(page_data.get_content())
    if page_data.has_attribute("Test"):
        tear_down = page_crawler_impl.get_inherit_page("TearDown", wiki_page)
        if tear_down is not None:
            tear_down_path = wiki_page.get_page_crawler().get_full_path(tear_down)
            tear_down_path_name = path_parser.render(tear_down_path)
            buffer.append("\n").append("!include -teardown .").append(tear_down_path_name).append("\n")
        if include_suit_setup:
            suite_teardown = page_crawler_impl.get_inherit_page(suite_responder.SUITE_TEARDOWN_NAME, wiki_page)
            if suite_teardown is not None:
                page_path = suite_teardown.get_page_crawler().get_full_path(suite_teardown)
                page_path_name = path_parser.render(page_path)
                buffer.append("!include -teardown .").append(page_path_name).append("\n")
                page_data.setContent(buffer.toString())
                return page_data.get_html()


# refactored
def render_page_with_setups_and_teardowns(page_data, is_suite):
    is_test_page = page_data.hasAttribute("Test")
    if is_test_page:
        test_page = page_data.getWikiPage()
        new_page_content = StringBuffer()
        include_setup_pages(test_page, new_page_content, is_suite)
        new_page_content.append(page_data.getContent())
        include_teardown_pages(test_page, new_page_content, is_suite)
        page_data.setContent(new_page_content.toString())
        return page_data.get_html()

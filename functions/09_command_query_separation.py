import mock
attribute_exists = mock.Mock()
set_attribute = mock.Mock()


def set(attribute, value) -> bool:
    pass


if set("username", "unclebob"):
    pass


if attribute_exists("username"):
    set_attribute("username", "unclebob")



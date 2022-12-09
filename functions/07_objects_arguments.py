import mock
make_circle = mock.Mock()


class Point:
    x = 10
    y = 20
    radius = 15


center = Point()

# bad
make_circle(10, 20, 15)

# good
make_circle(center)

import pytest

from everycheese.users.models import User

pytestmark = pytest.mark.django_db  # drives the test database system.


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"

from unittest.mock import Mock

import pytest
from flask import Response
from flask.views import MethodView

from eat_it.controllers import (
    GetUserController,
    UpdateUserController,
    DeleteUserController,
)
from eat_it.views import UserView


@pytest.fixture
def get_user_controller() -> GetUserController:
    return Mock(GetUserController)


@pytest.fixture
def update_user_controller() -> UpdateUserController:
    return Mock(UpdateUserController)


@pytest.fixture
def delete_user_controller() -> DeleteUserController:
    return Mock(DeleteUserController)


@pytest.fixture
def user_view(
    get_user_controller: GetUserController,
    update_user_controller: UpdateUserController,
    delete_user_controller: DeleteUserController,
) -> UserView:
    return UserView(
        get_controller=get_user_controller,
        update_controller=update_user_controller,
        delete_controller=delete_user_controller,
    )


def test_user_view_returns_501_on_get_method(user_view: UserView) -> None:
    actual = user_view.get("1")
    assert actual.status_code == 501


def test_user_view_returns_response_on_get_method(user_view: UserView) -> None:
    actual = user_view.get("1")
    assert isinstance(actual, Response)


def test_user_view_is_subclass_of_method_view(user_view: UserView) -> None:
    assert isinstance(user_view, MethodView)


def test_user_view_uses_get_user_controller(user_view: UserView, get_user_controller: Mock) -> None:
    user_view.get("1")
    assert get_user_controller.get.call_count > 0


def test_user_view_calls_update_user_controller_on_put_method(
    user_view: UserView,
    update_user_controller: Mock,
) -> None:
    user_view.put("1")
    assert update_user_controller.update.call_count > 0


def test_user_view_calls_delete_user_controller_on_delete_method(
    user_view: UserView,
    delete_user_controller: Mock,
) -> None:
    user_view.delete("1")
    assert delete_user_controller.delete.call_count > 0

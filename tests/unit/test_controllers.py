import json
from unittest.mock import Mock

import pytest
from _pytest.capture import CaptureFixture

from eat_it.controllers import (
    AddUserController,
    AddUserRequest,
    GetUserController,
    UpdateUserController,
    PartialUpdateUserController,
    DeleteUserController,
)
from eat_it.repositories import UserRepository


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


@pytest.fixture
def user_repository() -> UserRepository:
    return Mock(UserRepository)


@pytest.fixture
def add_user_controller(user_repository: UserRepository) -> AddUserController:
    return AddUserController(repository=user_repository)


@pytest.fixture
def get_user_controller(user_repository: UserRepository) -> GetUserController:
    return GetUserController(repository=user_repository)


@pytest.fixture
def update_user_controller(user_repository: UserRepository) -> UpdateUserController:
    return UpdateUserController(repository=user_repository)


@pytest.fixture
def partial_update_user_controller(
    user_repository: UserRepository,
) -> PartialUpdateUserController:
    return PartialUpdateUserController(repository=user_repository)


@pytest.fixture
def delete_user_controller(user_repository: UserRepository) -> DeleteUserController:
    return DeleteUserController(repository=user_repository)


def test_add_user_controller_has_add_method(
    capsys: CaptureFixture,
    payload: dict,
    add_user_controller: AddUserController,
) -> None:
    request = AddUserRequest(user=payload)
    add_user_controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_calls_add_in_repository_on_calling_add_user_controller(
    add_user_controller: AddUserController,
    user_repository: Mock,
    payload: dict,
) -> None:
    request = AddUserRequest(user=payload)
    add_user_controller.add(request)
    assert user_repository.add.call_count > 0


def test_get_user_controller_raises_not_implemented_error(
    get_user_controller: GetUserController,
) -> None:
    with pytest.raises(NotImplementedError):
        get_user_controller.get(1)


def test_update_user_controller_calls_update_in_repository(
    update_user_controller: UpdateUserController,
    user_repository: Mock,
    payload: dict,
) -> None:
    request = AddUserRequest(user=payload)
    update_user_controller.update(1, request)
    assert user_repository.update.call_count > 0


def test_partial_update_user_controller_calls_partial_update_in_repository(
    partial_update_user_controller: PartialUpdateUserController,
    user_repository: Mock,
    payload: dict,
) -> None:
    request = AddUserRequest(user=payload)
    partial_update_user_controller.partial_update(1, request)
    assert user_repository.partial_update.call_count > 0


def test_delete_user_controller_calls_delete_in_repository(
    delete_user_controller: DeleteUserController,
    user_repository: Mock,
) -> None:
    delete_user_controller.delete(1)
    assert user_repository.delete.call_count > 0

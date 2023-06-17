from dataclasses import dataclass

from eat_it.repositories import UserRepository


@dataclass
class AddUserRequest:
    user: dict


@dataclass
class UpdateUserRequest:
    user: dict


@dataclass
class PartialUpdateUserRequest:
    user: dict


@dataclass
class DeleteUserRequest:
    pass


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add(request.user)


class GetUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def get(self, id: int):
        raise NotImplementedError


class UpdateUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def update(self, id: int, request: UpdateUserRequest) -> None:
        self._repository.update(id, request.user)


class PartialUpdateUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def partial_update(self, id: int, request: PartialUpdateUserRequest) -> None:
        self._repository.partial_update(id, request.user)


class DeleteUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def delete(self, id: int, request: DeleteUserRequest) -> None:
        self._repository.delete(id)

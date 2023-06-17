class UserRepository:
    def add(self, user: dict) -> None:
        raise NotImplementedError

    def update(self, id: int, user: dict) -> None:
        raise NotImplementedError

    def partial_update(self, id: int, user: dict) -> None:
        raise NotImplementedError

    def delete(self, id: int) -> None:
        raise NotImplementedError

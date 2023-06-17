from flask import Flask, Response, request, jsonify
from sqlalchemy import create_engine

from eat_it.controllers import AddUserController, AddUserRequest, GetUserController, UpdateUserController, \
    PartialUpdateUserController, DeleteUserController
from eat_it.repositories import UserRepository
from eat_it.views import UserView


class DBFlask(Flask):
    def run(self, *args, **kwargs):
        create_engine("postgresql://user:password@localhost:5432/user_db")


app = DBFlask(__name__)
repository = UserRepository()
add_user_controller = AddUserController(repository)
get_user_controller = GetUserController(repository)
update_user_controller = UpdateUserController(repository)
partial_update_user_controller = PartialUpdateUserController(repository)
delete_user_controller = DeleteUserController(repository)


@app.get("/users")
def get_users() -> Response:
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    add_user_request = AddUserRequest(user=user)
    add_user_controller.add(request=add_user_request)
    return jsonify(user), 201


@app.put('/users/<id>')
def update_user(id: int) -> Response:
    user = request.json
    update_user_request = UpdateUserRequest(user=user)
    update_user_controller.update(id=id, request=update_user_request)
    return jsonify(user)


@app.patch('/users/<id>')
def partial_update_user(id: int) -> Response:
    user = request.json
    partial_update_user_request = PartialUpdateUserRequest(user=user)
    partial_update_user_controller.partial_update(id=id, request=partial_update_user_request)
    return jsonify(user)


@app.delete('/users/<id>')
def delete_user(id: int) -> Response:
    delete_user_request = DeleteUserRequest()
    delete_user_controller.delete(id=id, request=delete_user_request)
    return '', 204


user_view = UserView.as_view("user_view", controller=get_user_controller)
app.add_url_rule("/users/<id>", view_func=user_view)

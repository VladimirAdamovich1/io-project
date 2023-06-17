from flask import Response, jsonify
from flask.views import MethodView

from eat_it.controllers import GetUserController, AddUserController, UpdateUserController, \
    PartialUpdateUserController, DeleteUserController


class PingView(MethodView):
    def get(self) -> Response:
        return Response(status=501)


class UsersView(MethodView):
    def get(self) -> Response:
        return Response(status=501)

    def post(self) -> Response:
        user = request.json
        add_user_request = AddUserRequest(user=user)
        add_user_controller.add(request=add_user_request)
        return jsonify(user), 201


class UserView(MethodView):
    def get(self, id: str) -> Response:
        try:
            get_user_controller.get(int(id))
        except NotImplementedError:
            pass
        return Response(status=501)

    def put(self, id: str) -> Response:
        user = request.json
        update_user_request = UpdateUserRequest(user=user)
        update_user_controller.update(id=int(id), request=update_user_request)
        return jsonify(user)

    def patch(self, id: str) -> Response:
        user = request.json
        partial_update_user_request = PartialUpdateUserRequest(user=user)
        partial_update_user_controller.partial_update(id=int(id), request=partial_update_user_request)
        return jsonify(user)

    def delete(self, id: str) -> Response:
        delete_user_request = DeleteUserRequest()
        delete_user_controller.delete(id=int(id), request=delete_user_request)
        return '', 204

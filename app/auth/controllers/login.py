from flask_restful import Resource

class LoginView(Resource):
    def get(self):
        return {'Login': 'Successfully logged in'}

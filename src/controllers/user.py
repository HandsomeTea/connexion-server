from src.configs import HttpError, ErrorCode


class Users:
    def login(login_args: dict):
        raise HttpError('Invalid username or password', ErrorCode.UNAUTHORIZED)
        return {
            'user_id': '123456789'
        }

    def get_user_list(data: str):
        return f"test {data}"

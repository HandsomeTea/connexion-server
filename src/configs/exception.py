import json
from src.configs.error_code import ErrorCode
from app import app_name


class HttpError(Exception):
    def __init__(self, message, code: str = 'INTERNAL_SERVER_ERROR', reason: dict = {}):
        if isinstance(message, HttpError):
            self.code = message.code
            self.status = message.status
            self.message = message.message
            self.reason = message.reason
            if app_name not in message.source:
                message.source.append(app_name)
            self.source = message.source
        elif type(message) is dict:
            self.code = message.get('code', code)
            self.status = message.get('status') or ErrorCode.get_error_number(self.code)
            self.message = message.get('message', message.get('detail', 'internal server error!'))
            self.reason = message.get('reason', reason)
            source = message.get('source', [])
            if app_name not in source:
                source.append(app_name)
            self.source = source
        else:
            self.code = code
            self.status = ErrorCode.get_error_number(self.code)
            self.message = str(message)
            self.reason = reason
            self.source = [app_name]

        super().__init__(self.message)

    def to_dict(self):
        return {
            # 旧的错误返回统一格式
            # 'status': self.status,
            'detail': self.message,
            # 新的错误返回统一格式，现在使用新的，并逐步替换旧的
            'message': self.message,
            'code': self.code,
            'status': self.status,
            'reason': self.reason,
            'source': self.source
        }

    def __repr__(self) -> str:
        result = f'http error [{self.code}({self.status})] ' \
            f'from {" => ".join(str(element) for element in self.source)}'
        if len(self.reason) > 0:
            result += f' with data {json.dumps(self.reason, ensure_ascii=False)}'
        result += f': {self.message}'
        return result

    def __str__(self) -> str:
        return self.__repr__()

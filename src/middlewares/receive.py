import json
from app import application
from flask import request
from src.configs import log_api
from src.utils import random_string

app = application.app

# @app.before_request
# def set_header():
#     print('===========middleware 2 start======================')
#     # 抛出错误，会中断api请求
#     # raise HttpError('权限错误')
#     # 设置header，key必须以 HTTP_ 开头，后续将被当做header的key，如HTTP_xab-test或HTTP_xab_test，会为header设置key: Xab-Test
#     # request.headers.environ['HTTP_xab-test'] = '123'
#     print('===========middleware 2 end======================')


@app.before_request
def set_log_trace_header():
    request.headers.environ['HTTP_X_B3_TRACEID'] = request.headers.get('X-B3-TraceId') or random_string()
    request.headers.environ['HTTP_X_B3_PARENTSPANID'] = request.headers.get('X-B3-SpanId') or ''
    request.headers.environ['HTTP_X_B3_SPANID'] = random_string()


@app.before_request
def log_request():
    if not request.data:
        body = {}
    else:
        body = request.get_json(force=True)

    log_api.info(f'{request.method}:{request.path}\n' + json.dumps({
        'query': request.args,
        'body': body,
        'headers': dict(request.headers),
    }, indent=4, ensure_ascii=False), extra={
        'trace_id': request.headers.get('X-B3-TraceId'),
        'span_id': request.headers.get('X-B3-SpanId'),
        'parent_span_id': request.headers.get('X-B3-ParentSpanId')
    })

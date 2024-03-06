import json
from app import application
from flask import request
from src.configs import log_api
from src.utils import random_string

app = application.app


@app.before_request
def set_log_trace_header():
    request.headers.environ['HTTP_X_B3_TRACEID'] = request.headers.get('X-B3-TraceId') or random_string()
    request.headers.environ['HTTP_X_B3_PARENTSPANID'] = request.headers.get('X-B3-SpanId') or ''
    request.headers.environ['HTTP_X_B3_SPANID'] = random_string()


@app.before_request
def log_request():
    log_api.info(f'{request.method}:{request.path}\n' + json.dumps({
        'query': request.args,
        'body': request.get_json(),
        'headers': dict(request.headers),
    }, indent=4, ensure_ascii=False), extra={
        'trace_id': request.headers.get('X-B3-TraceId'),
        'span_id': request.headers.get('X-B3-SpanId'),
        'parent_span_id': request.headers.get('X-B3-ParentSpanId')
    })

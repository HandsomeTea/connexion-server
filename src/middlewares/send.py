import json
from app import application
from flask import request, make_response
from src.configs import log_api, HttpError

app = application.app


@app.after_request
def log_response(response):
    status = response.status_code
    if not (status >= 200 and status < 300):
        response = make_response(HttpError(response.get_json()).to_dict())
        response.status = str(status)

    if 'application/json' in response.headers['Content-Type']:
        if len(response.data) > 0:
            log_api.info(
                f'{request.method}:{request.path} => \n' + json.dumps(
                    json.loads(response.data.decode('utf-8')),
                    indent=4,
                    ensure_ascii=False
                ),
                extra={
                    'trace_id': request.headers.get('X-B3-TraceId'),
                    'span_id': request.headers.get('X-B3-SpanId'),
                    'parent_span_id': request.headers.get('X-B3-ParentSpanId')
                }
            )

    return response

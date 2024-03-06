import traceback
from app import application
from werkzeug.exceptions import HTTPException
from src.configs import log, HttpError

app = application.app


@app.errorhandler(Exception)
def error_catch(error):
    result = HttpError('Internal Server Error: ' + str(error)).to_dict()

    if isinstance(error, HTTPException):
        result = HttpError(error.description).to_dict()
    elif isinstance(error, HttpError):
        result = error.to_dict()

    log.error(traceback.format_exc())

    return result, result.get('status')

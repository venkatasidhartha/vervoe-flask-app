from flask import jsonify,request
from typing import Union, Dict, List
from functools import wraps
import logging

def errorResponse(status: str = "green", message: Union[str, None] = None, data: Union[Dict, List] = None, trace: Union[str, None] = None):
        response = {
            "status": status,
        }
        if message:
            response["message"] = message
        if data:
            response["data"] = data
        if trace:
            response["trace"] = trace
        return response


def capture_error(function):
    @wraps(function)
    def executor(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in extraction",exc_info=e)
            return jsonify(errorResponse(status="red",message="An unexpected error occurred",trace=str(e))), 500
    return executor
from typing import Union, Dict, List



def response(status: str = "green", message: Union[str, None] = None, data: Union[Dict, List] = None, trace: Union[str, None] = None):
        response = {
            "status": status,
        }
        if message:
            response["message"] = message
        if data:
            response["data"] = data
        if trace:
            response["trace"] = trace
        response = response
        return response
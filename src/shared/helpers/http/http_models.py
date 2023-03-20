from typing import Any
from warnings import warn

from src.shared.helpers.enum.http_status_code_enum import HttpStatusCodeEnum


class HttpRequest:
    body: dict
    headers: dict
    query_params: dict

    def __init__(self, body: dict = {}, headers: dict = {}, query_params: dict = {}):
        self.body = body or {}
        self.headers = headers or {}
        self.query_params = query_params or {}
        data_dict = {}

        # check overlapping keys
        if type(body) is dict:
            data_dict.update(body)
            if [key for key in self.body.keys() if key in self.query_params.keys()] or [key for key in self.body.keys()
                                                                                        if key in self.headers.keys()]:
                warn(
                    f"body, query_params and/or headers have overlapping keys → {[key for key in self.body.keys() if key in self.query_params.keys()] or [key for key in self.body.keys() if key in self.headers.keys()]}")
        else:
            if [key for key in self.query_params.keys() if key in self.headers.keys()]:
                warn(
                    f"query_params and headers have overlapping keys → {[key for key in self.query_params.keys() if key in self.headers.keys()]}")

        if type(body) is str:
            data_dict.update({"body": body})

        data_dict.update(self.headers)
        data_dict.update(self.query_params)
        self.data = data_dict

    def __repr__(self):
        return (
            f"HttpRequest (body={self.body}, headers={self.headers}, query_params={self.query_params}, data={self.data})"
        )



class HttpResponse:
    status_code: int
    body: dict
    headers: dict

    def __init__(self, status_code: int, body: dict = None, headers: dict = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def __repr__(self):
        return (
            f"HttpResponse (status_code={self.status_code}, body={self.body}, headers={self.headers})"
        )


class OK(HttpResponse):
    def __init__(self, body: Any = None) -> None:
        super().__init__(HttpStatusCodeEnum.OK.value, body)


class Created(HttpResponse):
    def __init__(self, body: Any = None) -> None:
        super().__init__(HttpStatusCodeEnum.CREATED.value, body)


class NoContent(HttpResponse):
    def __init__(self) -> None:
        super().__init__(HttpStatusCodeEnum.NO_CONTENT.value, None)


class BadRequest(HttpResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(HttpStatusCodeEnum.BAD_REQUEST.value, body)

class InternalServerError(HttpResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(HttpStatusCodeEnum.INTERNAL_SERVER_ERROR.value, body)


class NotFound(HttpResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(HttpStatusCodeEnum.NOT_FOUND.value, body)

class Conflict(HttpResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(HttpStatusCodeEnum.CONFLICT.value, body)

class RedirectResponse(HttpResponse):
    def __init__(self, body: dict) -> None:
        super().__init__(HttpStatusCodeEnum.REDIRECT.value, None)
        self.location = body
        
class Forbidden(HttpResponse):
    def __init__(self, body: dict) -> None:
        super().__init__(HttpStatusCodeEnum.FORBIDDEN.value, body)

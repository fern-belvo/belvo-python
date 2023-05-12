# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import BelvoEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.precondition_error import PreconditionError
from ...errors.request_timeout_error import RequestTimeoutError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.patch_body import PatchBody
from ...types.recurring_expenses import RecurringExpenses
from ...types.recurring_expenses_paginated_response import RecurringExpensesPaginatedResponse
from ...types.recurring_expenses_request import RecurringExpensesRequest
from ...types.request_timeout_error_body import RequestTimeoutErrorBody
from ...types.token_required_response import TokenRequiredResponse
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError


class RecurringExpensesClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    def list_recurring_expenses(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        account_in: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        id_in: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
    ) -> RecurringExpensesPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/recurring-expenses"),
            params={
                "page": page,
                "page_size": page_size,
                "omit": omit,
                "fields": fields,
                "link": link,
                "account": account,
                "account_in": account_in,
                "id": id,
                "id__in": id_in,
                "link__in": link_in,
            },
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecurringExpensesPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_recurring_expenses(
        self,
        *,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        request: RecurringExpensesRequest,
    ) -> typing.List[RecurringExpenses]:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/recurring-expenses"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[RecurringExpenses], _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 408:
            raise RequestTimeoutError(
                pydantic.parse_obj_as(typing.List[RequestTimeoutErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 428:
            raise PreconditionError(
                pydantic.parse_obj_as(typing.List[TokenRequiredResponse], _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch_recurring_expenses(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: PatchBody
    ) -> typing.List[RecurringExpenses]:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/recurring-expenses"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[RecurringExpenses], _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 408:
            raise RequestTimeoutError(
                pydantic.parse_obj_as(typing.List[RequestTimeoutErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 428:
            raise PreconditionError(
                pydantic.parse_obj_as(typing.List[TokenRequiredResponse], _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def detail_recurring_expense(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> typing.List[RecurringExpenses]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/recurring-expenses/{id}"),
            params={"omit": omit, "fields": fields},
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[RecurringExpenses], _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def destroy_recurring_expense(self, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/recurring-expenses/{id}"),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRecurringExpensesClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    async def list_recurring_expenses(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        account_in: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        id_in: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
    ) -> RecurringExpensesPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/recurring-expenses"),
                params={
                    "page": page,
                    "page_size": page_size,
                    "omit": omit,
                    "fields": fields,
                    "link": link,
                    "account": account,
                    "account_in": account_in,
                    "id": id,
                    "id__in": id_in,
                    "link__in": link_in,
                },
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecurringExpensesPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_recurring_expenses(
        self,
        *,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        request: RecurringExpensesRequest,
    ) -> typing.List[RecurringExpenses]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/recurring-expenses"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[RecurringExpenses], _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 408:
            raise RequestTimeoutError(
                pydantic.parse_obj_as(typing.List[RequestTimeoutErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 428:
            raise PreconditionError(
                pydantic.parse_obj_as(typing.List[TokenRequiredResponse], _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch_recurring_expenses(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: PatchBody
    ) -> typing.List[RecurringExpenses]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/recurring-expenses"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[RecurringExpenses], _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 408:
            raise RequestTimeoutError(
                pydantic.parse_obj_as(typing.List[RequestTimeoutErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 428:
            raise PreconditionError(
                pydantic.parse_obj_as(typing.List[TokenRequiredResponse], _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def detail_recurring_expense(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> typing.List[RecurringExpenses]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/recurring-expenses/{id}"),
                params={"omit": omit, "fields": fields},
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[RecurringExpenses], _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def destroy_recurring_expense(self, id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/recurring-expenses/{id}"),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
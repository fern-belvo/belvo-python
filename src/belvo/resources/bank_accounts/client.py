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
from ...errors.request_timeout_error import RequestTimeoutError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.bank_account_paginated_response import BankAccountPaginatedResponse
from ...types.create_bank_account_request import CreateBankAccountRequest
from ...types.create_bank_account_response import CreateBankAccountResponse
from ...types.detail_bank_account_response import DetailBankAccountResponse
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.request_timeout_error_body import RequestTimeoutErrorBody
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError


class BankAccountsClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    def list_bank_account(
        self,
        *,
        page: typing.Optional[int] = None,
        id_in: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        number: typing.Optional[str] = None,
        number_in: typing.Optional[str] = None,
        customer: typing.Optional[str] = None,
        institution: typing.Optional[str] = None,
        holder_type: typing.Optional[str] = None,
        holder_type_in: typing.Optional[str] = None,
        providers: typing.Optional[str] = None,
    ) -> BankAccountPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/bank-accounts"),
            params={
                "page": page,
                "id__in": id_in,
                "created_at": created_at,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "number": number,
                "number__in": number_in,
                "customer": customer,
                "institution": institution,
                "holder__type": holder_type,
                "holder__type__in": holder_type_in,
                "providers": providers,
            },
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BankAccountPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_bank_account(self, *, request: CreateBankAccountRequest) -> CreateBankAccountResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/bank-accounts"),
            json=jsonable_encoder(request),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateBankAccountResponse, _response.json())  # type: ignore
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
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def detail_bank_account(self, id: str) -> DetailBankAccountResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"payments/bank-accounts/{id}"),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DetailBankAccountResponse, _response.json())  # type: ignore
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


class AsyncBankAccountsClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    async def list_bank_account(
        self,
        *,
        page: typing.Optional[int] = None,
        id_in: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        number: typing.Optional[str] = None,
        number_in: typing.Optional[str] = None,
        customer: typing.Optional[str] = None,
        institution: typing.Optional[str] = None,
        holder_type: typing.Optional[str] = None,
        holder_type_in: typing.Optional[str] = None,
        providers: typing.Optional[str] = None,
    ) -> BankAccountPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/bank-accounts"),
                params={
                    "page": page,
                    "id__in": id_in,
                    "created_at": created_at,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "number": number,
                    "number__in": number_in,
                    "customer": customer,
                    "institution": institution,
                    "holder__type": holder_type,
                    "holder__type__in": holder_type_in,
                    "providers": providers,
                },
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BankAccountPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_bank_account(self, *, request: CreateBankAccountRequest) -> CreateBankAccountResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/bank-accounts"),
                json=jsonable_encoder(request),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateBankAccountResponse, _response.json())  # type: ignore
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
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def detail_bank_account(self, id: str) -> DetailBankAccountResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"payments/bank-accounts/{id}"),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DetailBankAccountResponse, _response.json())  # type: ignore
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

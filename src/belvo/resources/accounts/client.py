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
from ...types.account import Account
from ...types.accounts_paginated_response import AccountsPaginatedResponse
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.patch_body import PatchBody
from ...types.request_timeout_error_body import RequestTimeoutErrorBody
from ...types.standard_request import StandardRequest
from ...types.token_required_response import TokenRequiredResponse
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError


class AccountsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    def list_accounts(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        balance_available: typing.Optional[str] = None,
        balance_available_lt: typing.Optional[str] = None,
        balance_available_lte: typing.Optional[str] = None,
        balance_available_gt: typing.Optional[str] = None,
        balance_available_gte: typing.Optional[str] = None,
        balance_available_range: typing.Optional[str] = None,
        balance_current: typing.Optional[str] = None,
        balance_current_lt: typing.Optional[str] = None,
        balance_current_lte: typing.Optional[str] = None,
        balance_current_gt: typing.Optional[str] = None,
        balance_current_gte: typing.Optional[str] = None,
        balance_current_range: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        category_in: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        currency_in: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        id_in: typing.Optional[str] = None,
        institution: typing.Optional[str] = None,
        institution_in: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_icontains: typing.Optional[str] = None,
        number: typing.Optional[str] = None,
        number_in: typing.Optional[str] = None,
        public_identification_name: typing.Optional[str] = None,
        public_identification_value: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> AccountsPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounts"),
            params={
                "page": page,
                "page_size": page_size,
                "omit": omit,
                "fields": fields,
                "link": link,
                "balance__available": balance_available,
                "balance__available__lt": balance_available_lt,
                "balance__available__lte": balance_available_lte,
                "balance__available__gt": balance_available_gt,
                "balance__available__gte": balance_available_gte,
                "balance__available__range": balance_available_range,
                "balance__current": balance_current,
                "balance__current__lt": balance_current_lt,
                "balance__current__lte": balance_current_lte,
                "balance__current__gt": balance_current_gt,
                "balance__current__gte": balance_current_gte,
                "balance__current__range": balance_current_range,
                "category": category,
                "category__in": category_in,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "currency": currency,
                "currency__in": currency_in,
                "id": id,
                "id__in": id_in,
                "institution": institution,
                "institution__in": institution_in,
                "link__in": link_in,
                "name": name,
                "name__icontains": name_icontains,
                "number": number,
                "number__in": number_in,
                "public_identification_name": public_identification_name,
                "public_identification_value": public_identification_value,
                "type": type,
            },
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccountsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_accounts(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: StandardRequest
    ) -> typing.List[typing.Optional[Account]]:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounts"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Optional[Account]], _response.json())  # type: ignore
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

    def patch_accounts(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: PatchBody
    ) -> typing.List[typing.Optional[Account]]:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/accounts"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Optional[Account]], _response.json())  # type: ignore
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

    def detail_account(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> typing.Optional[Account]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/accounts/{id}"),
            params={"omit": omit, "fields": fields},
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[Account], _response.json())  # type: ignore
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

    def destroy_account(self, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/accounts/{id}"),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
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


class AsyncAccountsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    async def list_accounts(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        balance_available: typing.Optional[str] = None,
        balance_available_lt: typing.Optional[str] = None,
        balance_available_lte: typing.Optional[str] = None,
        balance_available_gt: typing.Optional[str] = None,
        balance_available_gte: typing.Optional[str] = None,
        balance_available_range: typing.Optional[str] = None,
        balance_current: typing.Optional[str] = None,
        balance_current_lt: typing.Optional[str] = None,
        balance_current_lte: typing.Optional[str] = None,
        balance_current_gt: typing.Optional[str] = None,
        balance_current_gte: typing.Optional[str] = None,
        balance_current_range: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        category_in: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        currency_in: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        id_in: typing.Optional[str] = None,
        institution: typing.Optional[str] = None,
        institution_in: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_icontains: typing.Optional[str] = None,
        number: typing.Optional[str] = None,
        number_in: typing.Optional[str] = None,
        public_identification_name: typing.Optional[str] = None,
        public_identification_value: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> AccountsPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/accounts"),
                params={
                    "page": page,
                    "page_size": page_size,
                    "omit": omit,
                    "fields": fields,
                    "link": link,
                    "balance__available": balance_available,
                    "balance__available__lt": balance_available_lt,
                    "balance__available__lte": balance_available_lte,
                    "balance__available__gt": balance_available_gt,
                    "balance__available__gte": balance_available_gte,
                    "balance__available__range": balance_available_range,
                    "balance__current": balance_current,
                    "balance__current__lt": balance_current_lt,
                    "balance__current__lte": balance_current_lte,
                    "balance__current__gt": balance_current_gt,
                    "balance__current__gte": balance_current_gte,
                    "balance__current__range": balance_current_range,
                    "category": category,
                    "category__in": category_in,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "currency": currency,
                    "currency__in": currency_in,
                    "id": id,
                    "id__in": id_in,
                    "institution": institution,
                    "institution__in": institution_in,
                    "link__in": link_in,
                    "name": name,
                    "name__icontains": name_icontains,
                    "number": number,
                    "number__in": number_in,
                    "public_identification_name": public_identification_name,
                    "public_identification_value": public_identification_value,
                    "type": type,
                },
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccountsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_accounts(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: StandardRequest
    ) -> typing.List[typing.Optional[Account]]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/accounts"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Optional[Account]], _response.json())  # type: ignore
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

    async def patch_accounts(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: PatchBody
    ) -> typing.List[typing.Optional[Account]]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/accounts"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Optional[Account]], _response.json())  # type: ignore
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

    async def detail_account(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> typing.Optional[Account]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/accounts/{id}"),
                params={"omit": omit, "fields": fields},
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[Account], _response.json())  # type: ignore
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

    async def destroy_account(self, id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/accounts/{id}"),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
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

# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import BelvoEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.precondition_error import PreconditionError
from ...errors.request_timeout_error import RequestTimeoutError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.asynchronous_accepted_202 import AsynchronousAccepted202
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.patch_body import PatchBody
from ...types.request_timeout_error_body import RequestTimeoutErrorBody
from ...types.token_required_response import TokenRequiredResponse
from ...types.transaction import Transaction
from ...types.transactions_paginated_response import TransactionsPaginatedResponse
from ...types.transactions_request import TransactionsRequest
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError


class TransactionsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    def list_transactions(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: str,
        account: typing.Optional[str] = None,
        account_balance_available: typing.Optional[str] = None,
        account_balance_available_lt: typing.Optional[str] = None,
        account_balance_available_lte: typing.Optional[str] = None,
        account_balance_available_range: typing.Optional[str] = None,
        account_balance_current: typing.Optional[str] = None,
        account_balance_current_gt: typing.Optional[str] = None,
        account_balance_current_gte: typing.Optional[str] = None,
        account_balance_current_lt: typing.Optional[str] = None,
        account_balance_current_lte: typing.Optional[str] = None,
        account_balance_current_range: typing.Optional[str] = None,
        account_in: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        account_type_in: typing.Optional[str] = None,
        accounting_date: typing.Optional[str] = None,
        accounting_date_gt: typing.Optional[str] = None,
        accounting_date_gte: typing.Optional[str] = None,
        accounting_date_lt: typing.Optional[str] = None,
        accounting_date_lte: typing.Optional[str] = None,
        accounting_date_range: typing.Optional[str] = None,
        amount: typing.Optional[str] = None,
        amount_gt: typing.Optional[str] = None,
        amount_gte: typing.Optional[str] = None,
        amount_lt: typing.Optional[str] = None,
        amount_lte: typing.Optional[str] = None,
        amount_range: typing.Optional[str] = None,
        collected_at: typing.Optional[str] = None,
        collected_at_gt: typing.Optional[str] = None,
        collected_at_gte: typing.Optional[str] = None,
        collected_at_lt: typing.Optional[str] = None,
        collected_at_lte: typing.Optional[str] = None,
        collected_at_range: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        credit_card_data_bill_name_in: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        currency_in: typing.Optional[str] = None,
        reference: typing.Optional[str] = None,
        reference_in: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        status_in: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        type_in: typing.Optional[str] = None,
        value_date: typing.Optional[str] = None,
        value_date_gt: typing.Optional[str] = None,
        value_date_gte: typing.Optional[str] = None,
        value_date_lt: typing.Optional[str] = None,
        value_date_lte: typing.Optional[str] = None,
        value_date_range: typing.Optional[str] = None,
    ) -> TransactionsPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
            params={
                "page": page,
                "page_size": page_size,
                "omit": omit,
                "fields": fields,
                "link": link,
                "account": account,
                "account__balance__available": account_balance_available,
                "account__balance__available__lt": account_balance_available_lt,
                "account__balance__available__lte": account_balance_available_lte,
                "account__balance__available__range": account_balance_available_range,
                "account__balance__current": account_balance_current,
                "account__balance__current__gt": account_balance_current_gt,
                "account__balance__current__gte": account_balance_current_gte,
                "account__balance__current__lt": account_balance_current_lt,
                "account__balance__current__lte": account_balance_current_lte,
                "account__balance__current__range": account_balance_current_range,
                "account__in": account_in,
                "account_type": account_type,
                "account_type__in": account_type_in,
                "accounting_date": accounting_date,
                "accounting_date__gt": accounting_date_gt,
                "accounting_date__gte": accounting_date_gte,
                "accounting_date__lt": accounting_date_lt,
                "accounting_date__lte": accounting_date_lte,
                "accounting_date__range": accounting_date_range,
                "amount": amount,
                "amount__gt": amount_gt,
                "amount__gte": amount_gte,
                "amount__lt": amount_lt,
                "amount__lte": amount_lte,
                "amount__range": amount_range,
                "collected_at": collected_at,
                "collected_at__gt": collected_at_gt,
                "collected_at__gte": collected_at_gte,
                "collected_at__lt": collected_at_lt,
                "collected_at__lte": collected_at_lte,
                "collected_at__range": collected_at_range,
                "created_at": created_at,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "credit_card_data__bill_name__in": credit_card_data_bill_name_in,
                "currency": currency,
                "currency__in": currency_in,
                "reference": reference,
                "reference__in": reference_in,
                "status": status,
                "status__in": status_in,
                "type": type,
                "type__in": type_in,
                "value_date": value_date,
                "value_date__gt": value_date_gt,
                "value_date__gte": value_date_gte,
                "value_date__lt": value_date_lt,
                "value_date__lte": value_date_lte,
                "value_date__range": value_date_range,
            },
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_transactions(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: TransactionsRequest
    ) -> typing.List[Transaction]:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Transaction], _response.json())  # type: ignore
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

    def retrieve_transactions_async(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: TransactionsRequest
    ) -> AsynchronousAccepted202:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            headers=remove_none_from_headers({"X-Belvo-Request-Mode": "async"}),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AsynchronousAccepted202, _response.json())  # type: ignore
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

    def patch_transactions(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: PatchBody
    ) -> typing.List[Transaction]:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Transaction], _response.json())  # type: ignore
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

    def detail_transaction(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> Transaction:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/transactions/{id}"),
            params={"omit": omit, "fields": fields},
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Transaction, _response.json())  # type: ignore
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

    def destroy_transaction(self, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/transactions/{id}"),
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


class AsyncTransactionsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    async def list_transactions(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: str,
        account: typing.Optional[str] = None,
        account_balance_available: typing.Optional[str] = None,
        account_balance_available_lt: typing.Optional[str] = None,
        account_balance_available_lte: typing.Optional[str] = None,
        account_balance_available_range: typing.Optional[str] = None,
        account_balance_current: typing.Optional[str] = None,
        account_balance_current_gt: typing.Optional[str] = None,
        account_balance_current_gte: typing.Optional[str] = None,
        account_balance_current_lt: typing.Optional[str] = None,
        account_balance_current_lte: typing.Optional[str] = None,
        account_balance_current_range: typing.Optional[str] = None,
        account_in: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        account_type_in: typing.Optional[str] = None,
        accounting_date: typing.Optional[str] = None,
        accounting_date_gt: typing.Optional[str] = None,
        accounting_date_gte: typing.Optional[str] = None,
        accounting_date_lt: typing.Optional[str] = None,
        accounting_date_lte: typing.Optional[str] = None,
        accounting_date_range: typing.Optional[str] = None,
        amount: typing.Optional[str] = None,
        amount_gt: typing.Optional[str] = None,
        amount_gte: typing.Optional[str] = None,
        amount_lt: typing.Optional[str] = None,
        amount_lte: typing.Optional[str] = None,
        amount_range: typing.Optional[str] = None,
        collected_at: typing.Optional[str] = None,
        collected_at_gt: typing.Optional[str] = None,
        collected_at_gte: typing.Optional[str] = None,
        collected_at_lt: typing.Optional[str] = None,
        collected_at_lte: typing.Optional[str] = None,
        collected_at_range: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        credit_card_data_bill_name_in: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        currency_in: typing.Optional[str] = None,
        reference: typing.Optional[str] = None,
        reference_in: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        status_in: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        type_in: typing.Optional[str] = None,
        value_date: typing.Optional[str] = None,
        value_date_gt: typing.Optional[str] = None,
        value_date_gte: typing.Optional[str] = None,
        value_date_lt: typing.Optional[str] = None,
        value_date_lte: typing.Optional[str] = None,
        value_date_range: typing.Optional[str] = None,
    ) -> TransactionsPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
                params={
                    "page": page,
                    "page_size": page_size,
                    "omit": omit,
                    "fields": fields,
                    "link": link,
                    "account": account,
                    "account__balance__available": account_balance_available,
                    "account__balance__available__lt": account_balance_available_lt,
                    "account__balance__available__lte": account_balance_available_lte,
                    "account__balance__available__range": account_balance_available_range,
                    "account__balance__current": account_balance_current,
                    "account__balance__current__gt": account_balance_current_gt,
                    "account__balance__current__gte": account_balance_current_gte,
                    "account__balance__current__lt": account_balance_current_lt,
                    "account__balance__current__lte": account_balance_current_lte,
                    "account__balance__current__range": account_balance_current_range,
                    "account__in": account_in,
                    "account_type": account_type,
                    "account_type__in": account_type_in,
                    "accounting_date": accounting_date,
                    "accounting_date__gt": accounting_date_gt,
                    "accounting_date__gte": accounting_date_gte,
                    "accounting_date__lt": accounting_date_lt,
                    "accounting_date__lte": accounting_date_lte,
                    "accounting_date__range": accounting_date_range,
                    "amount": amount,
                    "amount__gt": amount_gt,
                    "amount__gte": amount_gte,
                    "amount__lt": amount_lt,
                    "amount__lte": amount_lte,
                    "amount__range": amount_range,
                    "collected_at": collected_at,
                    "collected_at__gt": collected_at_gt,
                    "collected_at__gte": collected_at_gte,
                    "collected_at__lt": collected_at_lt,
                    "collected_at__lte": collected_at_lte,
                    "collected_at__range": collected_at_range,
                    "created_at": created_at,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "credit_card_data__bill_name__in": credit_card_data_bill_name_in,
                    "currency": currency,
                    "currency__in": currency_in,
                    "reference": reference,
                    "reference__in": reference_in,
                    "status": status,
                    "status__in": status_in,
                    "type": type,
                    "type__in": type_in,
                    "value_date": value_date,
                    "value_date__gt": value_date_gt,
                    "value_date__gte": value_date_gte,
                    "value_date__lt": value_date_lt,
                    "value_date__lte": value_date_lte,
                    "value_date__range": value_date_range,
                },
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_transactions(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: TransactionsRequest
    ) -> typing.List[Transaction]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Transaction], _response.json())  # type: ignore
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

    async def retrieve_transactions_async(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: TransactionsRequest
    ) -> AsynchronousAccepted202:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                headers=remove_none_from_headers({"X-Belvo-Request-Mode": "async"}),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AsynchronousAccepted202, _response.json())  # type: ignore
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

    async def patch_transactions(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: PatchBody
    ) -> typing.List[Transaction]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/transactions"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Transaction], _response.json())  # type: ignore
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

    async def detail_transaction(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> Transaction:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/transactions/{id}"),
                params={"omit": omit, "fields": fields},
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Transaction, _response.json())  # type: ignore
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

    async def destroy_transaction(self, id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/transactions/{id}"),
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

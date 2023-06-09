# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...environment import BelvoEnvironment
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.payment_transaction import PaymentTransaction
from ...types.payments_transactions_paginated_response import PaymentsTransactionsPaginatedResponse
from ...types.unauthorized_error_body import UnauthorizedErrorBody


class PaymentTransactionsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    def list_payment_transactions(
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
        charge: typing.Optional[str] = None,
        charge_in: typing.Optional[str] = None,
        beneficiary: typing.Optional[str] = None,
        beneficiary_in: typing.Optional[str] = None,
        payer: typing.Optional[str] = None,
        payer_in: typing.Optional[str] = None,
        transaction_type: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        amount: typing.Optional[str] = None,
        amount_gt: typing.Optional[str] = None,
        amount_gte: typing.Optional[str] = None,
        amount_lt: typing.Optional[str] = None,
        amount_lte: typing.Optional[str] = None,
        amount_range: typing.Optional[str] = None,
    ) -> PaymentsTransactionsPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/transactions"),
            params={
                "page": page,
                "id__in": id_in,
                "created_at": created_at,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "charge": charge,
                "charge__in": charge_in,
                "beneficiary": beneficiary,
                "beneficiary__in": beneficiary_in,
                "payer": payer,
                "payer__in": payer_in,
                "transaction__type": transaction_type,
                "currency": currency,
                "description": description,
                "amount": amount,
                "amount__gt": amount_gt,
                "amount__gte": amount_gte,
                "amount__lt": amount_lt,
                "amount__lte": amount_lte,
                "amount__range": amount_range,
            },
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentsTransactionsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def detail_payment_transactions(self, id: str) -> PaymentTransaction:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"payments/transactions/{id}"),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentTransaction, _response.json())  # type: ignore
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


class AsyncPaymentTransactionsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    async def list_payment_transactions(
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
        charge: typing.Optional[str] = None,
        charge_in: typing.Optional[str] = None,
        beneficiary: typing.Optional[str] = None,
        beneficiary_in: typing.Optional[str] = None,
        payer: typing.Optional[str] = None,
        payer_in: typing.Optional[str] = None,
        transaction_type: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        amount: typing.Optional[str] = None,
        amount_gt: typing.Optional[str] = None,
        amount_gte: typing.Optional[str] = None,
        amount_lt: typing.Optional[str] = None,
        amount_lte: typing.Optional[str] = None,
        amount_range: typing.Optional[str] = None,
    ) -> PaymentsTransactionsPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/transactions"),
                params={
                    "page": page,
                    "id__in": id_in,
                    "created_at": created_at,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "charge": charge,
                    "charge__in": charge_in,
                    "beneficiary": beneficiary,
                    "beneficiary__in": beneficiary_in,
                    "payer": payer,
                    "payer__in": payer_in,
                    "transaction__type": transaction_type,
                    "currency": currency,
                    "description": description,
                    "amount": amount,
                    "amount__gt": amount_gt,
                    "amount__gte": amount_gte,
                    "amount__lt": amount_lt,
                    "amount__lte": amount_lte,
                    "amount__range": amount_range,
                },
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentsTransactionsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def detail_payment_transactions(self, id: str) -> PaymentTransaction:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"payments/transactions/{id}"),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentTransaction, _response.json())  # type: ignore
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

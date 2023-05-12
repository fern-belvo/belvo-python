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
from ...types.create_payment_intent_pse import CreatePaymentIntentPse
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.patch_payment_intents_body_pse import PatchPaymentIntentsBodyPse
from ...types.payment_intent_paginated_response import PaymentIntentPaginatedResponse
from ...types.payment_intent_pse import PaymentIntentPse
from ...types.request_timeout_error_body import RequestTimeoutErrorBody
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PaymentIntentsClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    def list_payment_intents(
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
        provider: typing.Optional[str] = None,
        payment_method_type: typing.Optional[str] = None,
        customer: typing.Optional[str] = None,
        customer_in: typing.Optional[str] = None,
        amount: typing.Optional[str] = None,
        amount_gt: typing.Optional[str] = None,
        amount_gte: typing.Optional[str] = None,
        amount_lt: typing.Optional[str] = None,
        amount_lte: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        status_in: typing.Optional[str] = None,
    ) -> PaymentIntentPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-intents"),
            params={
                "page": page,
                "id__in": id_in,
                "created_at": created_at,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "provider": provider,
                "payment_method_type": payment_method_type,
                "customer": customer,
                "customer__in": customer_in,
                "amount": amount,
                "amount__gt": amount_gt,
                "amount__gte": amount_gte,
                "amount__lt": amount_lt,
                "amount__lte": amount_lte,
                "status": status,
                "status__in": status_in,
            },
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_payment_intent(self, *, request: CreatePaymentIntentPse) -> PaymentIntentPse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-intents"),
            json=jsonable_encoder(request),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPse, _response.json())  # type: ignore
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

    def detail_payment_intent(self, id: str) -> PaymentIntentPse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"payments/payment-intents/{id}"),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPse, _response.json())  # type: ignore
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

    def patch_payment_intent(
        self, id: str, *, payment_method_details: PatchPaymentIntentsBodyPse, confirm: typing.Optional[bool] = OMIT
    ) -> PaymentIntentPse:
        _request: typing.Dict[str, typing.Any] = {"payment_method_details": payment_method_details}
        if confirm is not OMIT:
            _request["confirm"] = confirm
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", f"payments/payment-intents/{id}"),
            json=jsonable_encoder(_request),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPaymentIntentsClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    async def list_payment_intents(
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
        provider: typing.Optional[str] = None,
        payment_method_type: typing.Optional[str] = None,
        customer: typing.Optional[str] = None,
        customer_in: typing.Optional[str] = None,
        amount: typing.Optional[str] = None,
        amount_gt: typing.Optional[str] = None,
        amount_gte: typing.Optional[str] = None,
        amount_lt: typing.Optional[str] = None,
        amount_lte: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        status_in: typing.Optional[str] = None,
    ) -> PaymentIntentPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-intents"),
                params={
                    "page": page,
                    "id__in": id_in,
                    "created_at": created_at,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "provider": provider,
                    "payment_method_type": payment_method_type,
                    "customer": customer,
                    "customer__in": customer_in,
                    "amount": amount,
                    "amount__gt": amount_gt,
                    "amount__gte": amount_gte,
                    "amount__lt": amount_lt,
                    "amount__lte": amount_lte,
                    "status": status,
                    "status__in": status_in,
                },
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_payment_intent(self, *, request: CreatePaymentIntentPse) -> PaymentIntentPse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-intents"),
                json=jsonable_encoder(request),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPse, _response.json())  # type: ignore
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

    async def detail_payment_intent(self, id: str) -> PaymentIntentPse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"payments/payment-intents/{id}"),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPse, _response.json())  # type: ignore
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

    async def patch_payment_intent(
        self, id: str, *, payment_method_details: PatchPaymentIntentsBodyPse, confirm: typing.Optional[bool] = OMIT
    ) -> PaymentIntentPse:
        _request: typing.Dict[str, typing.Any] = {"payment_method_details": payment_method_details}
        if confirm is not OMIT:
            _request["confirm"] = confirm
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", f"payments/payment-intents/{id}"),
                json=jsonable_encoder(_request),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentIntentPse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

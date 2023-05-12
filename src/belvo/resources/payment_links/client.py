# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import BelvoEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.request_timeout_error import RequestTimeoutError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.create_paymentlink_request import CreatePaymentlinkRequest
from ...types.create_paymentlink_response import CreatePaymentlinkResponse
from ...types.detail_create_paymentlink_response import DetailCreatePaymentlinkResponse
from ...types.list_payment_links_request_ordering import ListPaymentLinksRequestOrdering
from ...types.list_payment_links_request_status import ListPaymentLinksRequestStatus
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.payment_link_paginated_response import PaymentLinkPaginatedResponse
from ...types.request_timeout_error_body import RequestTimeoutErrorBody
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError


class PaymentLinksClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    def list_payment_links(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        created_at: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        status: typing.Optional[ListPaymentLinksRequestStatus] = None,
        ordering: typing.Optional[ListPaymentLinksRequestOrdering] = None,
        search: typing.Optional[str] = None,
    ) -> PaymentLinkPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-links"),
            params={
                "page": page,
                "page_size": page_size,
                "created_at": created_at,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "status": serialize_datetime(status) if status is not None else None,
                "ordering": serialize_datetime(ordering) if ordering is not None else None,
                "search": search,
            },
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentLinkPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_paymentlink(self, *, request: CreatePaymentlinkRequest) -> CreatePaymentlinkResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-links"),
            json=jsonable_encoder(request),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreatePaymentlinkResponse, _response.json())  # type: ignore
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

    def detail_create_paymentlink(self, access_token: str) -> DetailCreatePaymentlinkResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"payments/payment-links/{access_token}"),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DetailCreatePaymentlinkResponse, _response.json())  # type: ignore
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


class AsyncPaymentLinksClient:
    def __init__(self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password

    async def list_payment_links(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        created_at: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        status: typing.Optional[ListPaymentLinksRequestStatus] = None,
        ordering: typing.Optional[ListPaymentLinksRequestOrdering] = None,
        search: typing.Optional[str] = None,
    ) -> PaymentLinkPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-links"),
                params={
                    "page": page,
                    "page_size": page_size,
                    "created_at": created_at,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "status": serialize_datetime(status) if status is not None else None,
                    "ordering": serialize_datetime(ordering) if ordering is not None else None,
                    "search": search,
                },
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentLinkPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_paymentlink(self, *, request: CreatePaymentlinkRequest) -> CreatePaymentlinkResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "payments/payment-links"),
                json=jsonable_encoder(request),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreatePaymentlinkResponse, _response.json())  # type: ignore
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

    async def detail_create_paymentlink(self, access_token: str) -> DetailCreatePaymentlinkResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"payments/payment-links/{access_token}"),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DetailCreatePaymentlinkResponse, _response.json())  # type: ignore
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

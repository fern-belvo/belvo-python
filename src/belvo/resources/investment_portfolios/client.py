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
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.investments_portfolio import InvestmentsPortfolio
from ...types.investments_portfolios_paginated_response import InvestmentsPortfoliosPaginatedResponse
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.patch_body_without_save_data import PatchBodyWithoutSaveData
from ...types.standard_request import StandardRequest
from ...types.token_required_response import TokenRequiredResponse
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError


class InvestmentPortfoliosClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    def list_portfolio(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
    ) -> InvestmentsPortfoliosPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "investments/portfolios"),
            params={
                "page": page,
                "page_size": page_size,
                "omit": omit,
                "fields": fields,
                "link": link,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "link__in": link_in,
            },
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfoliosPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_portfolio(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: StandardRequest
    ) -> InvestmentsPortfolio:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "investments/portfolios"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfolio, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
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

    def patch_portfolio(
        self,
        *,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        request: PatchBodyWithoutSaveData,
    ) -> InvestmentsPortfolio:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", "investments/portfolios"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfolio, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
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

    def detail_portfolio(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> InvestmentsPortfolio:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"investments/portfolios/{id}"),
            params={"omit": omit, "fields": fields},
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfolio, _response.json())  # type: ignore
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

    def destroy_portfolio(self, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"investments/portfolios/{id}"),
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


class AsyncInvestmentPortfoliosClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    async def list_portfolio(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
    ) -> InvestmentsPortfoliosPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "investments/portfolios"),
                params={
                    "page": page,
                    "page_size": page_size,
                    "omit": omit,
                    "fields": fields,
                    "link": link,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "link__in": link_in,
                },
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfoliosPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_portfolio(
        self, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None, request: StandardRequest
    ) -> InvestmentsPortfolio:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "investments/portfolios"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfolio, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
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

    async def patch_portfolio(
        self,
        *,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        request: PatchBodyWithoutSaveData,
    ) -> InvestmentsPortfolio:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", "investments/portfolios"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfolio, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
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

    async def detail_portfolio(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> InvestmentsPortfolio:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"investments/portfolios/{id}"),
                params={"omit": omit, "fields": fields},
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvestmentsPortfolio, _response.json())  # type: ignore
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

    async def destroy_portfolio(self, id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"investments/portfolios/{id}"),
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

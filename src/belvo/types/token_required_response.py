# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .token_required_response_token_generation_data import TokenRequiredResponseTokenGenerationData


class TokenRequiredResponse(pydantic.BaseModel):
    """
    MFA Token Required
    """

    code: typing.Optional[str] = pydantic.Field(
        description=(
            "A unique error code (`token_required`) that allows you to classify and handle the error programmatically.\n"
            "\n"
            'ℹ️ Check our DevPortal for more information on how to handle <a href="https://developers.belvo.com/docs/belvo-api-errors#428-token_required" target="_blank">428 token_required errors</a>.\n'
        )
    )
    message: typing.Optional[str] = pydantic.Field(
        description=(
            "A short description of the error. \n"
            "\n"
            "For `token_required` errors, the description is:\n"
            "  \n"
            "  - `A MFA token is required by the institution to login`.\n"
        )
    )
    request_id: typing.Optional[str] = pydantic.Field(
        description=(
            "A 32-character unique ID of the request (matching a regex pattern of: `[a-f0-9]{32}`). Provide this ID when contacting the Belvo support team to accelerate investigations.\n"
        )
    )
    session: typing.Optional[str] = pydantic.Field(
        description=("A 32-character unique ID of the login session (matching a regex pattern of: `[a-f0-9]{32}`).\n")
    )
    expiry: typing.Optional[int] = pydantic.Field(description=("Session duration time in seconds.\n"))
    link: typing.Optional[str] = pydantic.Field(
        description=("Unique identifier created by Belvo, used to reference the current Link.\n")
    )
    token_generation_data: typing.Optional[TokenRequiredResponseTokenGenerationData]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

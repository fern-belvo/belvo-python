# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class LastErrorInvalidToken(pydantic.BaseModel):
    """
    Information about the error you ran into in the previous step of the payment intent, if applicable. This error can occur when the MFA token your customer provides is invalid.
    """

    error_code: str = pydantic.Field(
        description=(
            "A unique error code (`invalid_token`) that allows you to classify and handle the error programmatically.\n"
        )
    )
    error_message: str = pydantic.Field(description=("A short description of the error.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

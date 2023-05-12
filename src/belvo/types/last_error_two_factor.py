# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class LastErrorTwoFactor(pydantic.BaseModel):
    """
    Information about the error you ran into in the previous step of the payment intent, if applicable. This error can occur when something unexpected happened in the `pse_display_token_required` next step.
    """

    error_code: str = pydantic.Field(
        description=(
            "A unique error code (`login_two_factor_error`) that allows you to classify and handle the error programmatically.\n"
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
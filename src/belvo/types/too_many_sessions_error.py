# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class TooManySessionsError(pydantic.BaseModel):
    """
    This error occurs when:

      - a user is attempting to log in to their institution via Belvo while also already being logged in to their institution on a web browser or mobile app.
      - you make a request for information while Belvo is scraping data from the institution for that user.
    """

    code: typing.Optional[str] = pydantic.Field(
        description=(
            "A unique error code (`too_many_sessions`) that allows you to classify and handle the error programmatically.\n"
            "\n"
            'ℹ️ Check our DevPortal for more information on how to handle <a href="https://developers.belvo.com/docs/belvo-api-errors#400-too_many_sessions" target="_blank">400 too_many_sessions errors</a>.\n'
        )
    )
    message: typing.Optional[str] = pydantic.Field(
        description=(
            "A short description of the error.\n"
            "\n"
            "For `too_many_sessions` errors, the description is:\n"
            "\n"
            "  - `Impossible to login, a session is already opened with the institution for these credentials`.\n"
        )
    )
    request_id: typing.Optional[str] = pydantic.Field(
        description=(
            "A 32-character unique ID of the request (matching a regex pattern of: `[a-f0-9]{32}`). Provide this ID when contacting the Belvo support team to accelerate investigations.\n"
        )
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

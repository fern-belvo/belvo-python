# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class LoginError(pydantic.BaseModel):
    """
    This error can occur when:

      - the credentials that your user provides are incorrect or missing.
      - the MFA token your user provides is not supported by Belvo.
      - there is an issue with the institution that prevents logins.
      - the user's account is either locked or the user does not have permission to access their internet banking.
    """

    code: typing.Optional[str] = pydantic.Field(
        description=(
            "A unique error code (`login_error`) that allows you to classify and handle the error programmatically.\n"
            "\n"
            'ℹ️ Check our DevPortal for more information on how to handle <a href="https://developers.belvo.com/docs/belvo-api-errors#400-login_error" target="_blank">400 login_error errors</a>.\n'
        )
    )
    message: typing.Optional[str] = pydantic.Field(
        description=(
            "A short description of the error.\n"
            "\n"
            "For `login_error` errors, the description can be one of the following:\n"
            "\n"
            "  - `Invalid credentials provided to login to the institution`\n"
            "  - `A MFA token is required by the institution, but it's not supported yet by Belvo.`\n"
            "  - `Impossible to login, something unexpected happened while logging into the institution. Try again later.`\n"
            "  - `Login not attempted due to invalid credentials`\n"
            "  - `Missing credentials to login to the institution`\n"
            "  - `The user account access was forbidden by the institution`\n"
            "  - `The user account is locked, user needs to contact the institution to unlock it`\n"
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

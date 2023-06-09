# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumInstitutionIntegrationType(str, enum.Enum):
    """
    The type of technology used to access the institution. We return one of the following values:

    - `credentials`: Uses Belvo's scraping technology, combined with user credentials, to perform requests.
    - `openbanking`: Uses the bank's openbanking API to perform requests.
    """

    CREDENTIALS = "credentials"
    OPENBANKING = "openbanking"

    def visit(self, credentials: typing.Callable[[], T_Result], openbanking: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumInstitutionIntegrationType.CREDENTIALS:
            return credentials()
        if self is EnumInstitutionIntegrationType.OPENBANKING:
            return openbanking()

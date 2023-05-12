# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumInstitutionStatus(str, enum.Enum):
    """
    Indicates whether Belvo's integration with the institution is currently active (`healthy`) or undergoing maintenance (`down`).
    """

    HEALTHY = "healthy"
    DOWN = "down"

    def visit(self, healthy: typing.Callable[[], T_Result], down: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumInstitutionStatus.HEALTHY:
            return healthy()
        if self is EnumInstitutionStatus.DOWN:
            return down()
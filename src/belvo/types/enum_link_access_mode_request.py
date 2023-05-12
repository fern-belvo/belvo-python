# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumLinkAccessModeRequest(str, enum.Enum):
    """
    The type of link to create.

    - Use `single` to do ad hoc one-time POST requests for accounts, owners, and transactions.
    - Use `recurrent` to have Belvo access information on a recurrent basis so you always have fresh account, owner, balance, and transaction data.

    For more information, see our [Links](https://developers.belvo.com/docs/links-and-institutions#links) article.
    """

    SINGLE = "single"
    RECURRENT = "recurrent"

    def visit(self, single: typing.Callable[[], T_Result], recurrent: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumLinkAccessModeRequest.SINGLE:
            return single()
        if self is EnumLinkAccessModeRequest.RECURRENT:
            return recurrent()

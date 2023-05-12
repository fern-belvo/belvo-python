# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumInvoiceAllowedIncomeTypesRequest(str, enum.Enum):
    """
    The categories of the incomes you want to get information for.
    You can send through one or more of the following values:
      - `SALARY`
      - `GOVERNMENT`
      - `INTEREST`
      - `RENT`
      - `RETIREMENT`
      - `FREELANCE`
      - `ALTERNATIVE_INCOME`
      - `TRANSFER`
      - `DEPOSIT`
      - `UNKNOWN`
    """

    SALARY = "SALARY"
    GOVERNMENT = "GOVERNMENT"
    INTEREST = "INTEREST"
    RENT = "RENT"
    RETIREMENT = "RETIREMENT"
    FREELANCE = "FREELANCE"
    ALTERNATIVE_INCOME = "ALTERNATIVE_INCOME"
    TRANSFER = "TRANSFER"
    DEPOSIT = "DEPOSIT"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        salary: typing.Callable[[], T_Result],
        government: typing.Callable[[], T_Result],
        interest: typing.Callable[[], T_Result],
        rent: typing.Callable[[], T_Result],
        retirement: typing.Callable[[], T_Result],
        freelance: typing.Callable[[], T_Result],
        alternative_income: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
        deposit: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumInvoiceAllowedIncomeTypesRequest.SALARY:
            return salary()
        if self is EnumInvoiceAllowedIncomeTypesRequest.GOVERNMENT:
            return government()
        if self is EnumInvoiceAllowedIncomeTypesRequest.INTEREST:
            return interest()
        if self is EnumInvoiceAllowedIncomeTypesRequest.RENT:
            return rent()
        if self is EnumInvoiceAllowedIncomeTypesRequest.RETIREMENT:
            return retirement()
        if self is EnumInvoiceAllowedIncomeTypesRequest.FREELANCE:
            return freelance()
        if self is EnumInvoiceAllowedIncomeTypesRequest.ALTERNATIVE_INCOME:
            return alternative_income()
        if self is EnumInvoiceAllowedIncomeTypesRequest.TRANSFER:
            return transfer()
        if self is EnumInvoiceAllowedIncomeTypesRequest.DEPOSIT:
            return deposit()
        if self is EnumInvoiceAllowedIncomeTypesRequest.UNKNOWN:
            return unknown()
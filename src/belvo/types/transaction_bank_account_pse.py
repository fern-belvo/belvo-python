# This file was auto-generated by Fern from our API Definition.

import typing

from .bank_account_information_pse import BankAccountInformationPse
from .transaction_bank_account_body_pse import TransactionBankAccountBodyPse

TransactionBankAccountPse = typing.Union[TransactionBankAccountBodyPse, BankAccountInformationPse]
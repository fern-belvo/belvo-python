# This file was auto-generated by Fern from our API Definition.

import typing

from .payment_intent_payment_method_details_business_ofpi import PaymentIntentPaymentMethodDetailsBusinessOfpi
from .payment_intent_payment_method_details_individual_ofpi import PaymentIntentPaymentMethodDetailsIndividualOfpi

PaymentIntentOfpiPaymentMethodDetails = typing.Union[
    PaymentIntentPaymentMethodDetailsIndividualOfpi, PaymentIntentPaymentMethodDetailsBusinessOfpi
]

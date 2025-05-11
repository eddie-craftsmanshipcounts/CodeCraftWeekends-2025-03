from datetime import date

class Parcel:
    def __init__(
        self,
        account_id: str,
        postal_code: str,
        total_approved_value: int,
        last_purchased_on: date,
        legal_description: str,
        ):
        self._account_id = account_id
        self._postal_code = postal_code
        self._total_approved_value = total_approved_value
        self._last_purchased_on = last_purchased_on
        self._legal_description = legal_description

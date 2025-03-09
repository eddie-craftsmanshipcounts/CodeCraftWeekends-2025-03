from abc import ABC, abstractmethod
import csv

from hcad_star_schema.domain.real_estate.account_owner.account_owner import AccountOwner

class AccountOwnerSource(ABC):
    def __next__(self) -> AccountOwner:
        return self.next()

    def __iter__(self):
        pass

    def _make_account_owner(self, record):
        clean_records = { key: value.strip() for key, value in record.items() }

        return AccountOwner(
            clean_records['acct'],
            clean_records['site_addr_3'],
        )


class TabSeparatedAccountOwnerSource(AccountOwnerSource):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def __iter__(self):
        self._file = open(self._filepath, "r")
        self._reader = csv.DictReader(self._file, delimiter='\t')

        return self

    def __next__(self) -> AccountOwner:
        """Return the next Account from the TSV file."""
        if self._reader is None:
            raise StopIteration
            
        try:
            record = next(self._reader)
            # Convert row to Account (adjust field indices based on your TSV structure)
            return self._make_account_owner(record)
        except StopIteration:
            if self._file:
                self._file.close()
                self._file = None
                self._reader = None
            raise



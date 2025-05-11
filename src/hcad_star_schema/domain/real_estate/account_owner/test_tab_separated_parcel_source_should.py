import unittest
from unittest import mock
from unittest.mock import MagicMock
import os
from datetime import datetime, date
import io

from hcad_star_schema.domain.real_estate.account_owner.parcel_source import ParcelSource
from hcad_star_schema.domain.real_estate.account_owner.parcel_source import TabSeparatedParcelSource


class TestReadFromFileShould(unittest.TestCase):
    def setUp(self):
        path = 'data/unit_test/real_acc.txt'
        source: ParcelSource = TabSeparatedParcelSource(path)
        self.account_owners = list(iter(source))
        self.account_owner = self.account_owners[0]

    def test_read_acctount_id_for_each_row(self):
        self.assertEqual(self.account_owner._account_id, '0010010000013')
    
    def test_read_acctount_postal_code_for_each_row(self):
        self.assertEqual(self.account_owner._postal_code, '77002')

    def test_read_total_approved_value(self):
        self.assertEqual(self.account_owner._total_approved_value, 0)

    def test_read_date_last_purchased(self):
        self.assertEqual(self.account_owner._last_purchased_on, date(1988, 1, 2))

    def test_read_legal_description(self):
        self.assertEqual(self.account_owner._legal_description, 'ALL BLK 1')

class TestInvalidZipCodeShould(unittest.TestCase):
    def test_load_null_instead_of_empty_string(self):
        def tsv_row(*args):
            return "\t".join(args)

        content = [
            tsv_row('acct', 'site_addr_3', 'tot_appr_val', 'new_own_dt', 'lgl_1'),
            tsv_row(':ignored:', '', '0', '01/01/2025', ':ignored:')
        ]

        mock_file = io.StringIO("\n".join(content))

        with unittest.mock.patch('builtins.open') as open_mock:
            open_mock.return_value = mock_file
            path = 'data/unit_test/real_acc.txt'
            source: ParcelSource = TabSeparatedParcelSource(path)
            self.account_owners = list(iter(source))
            self.account_owner = self.account_owners[0]

        self.assertIsNone(self.account_owner._postal_code, "Postal Code should be None")


# Should this move to Infrastructure? It's testing an adapter!

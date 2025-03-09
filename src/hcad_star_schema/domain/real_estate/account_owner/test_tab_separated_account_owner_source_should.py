import unittest
import os

from hcad_star_schema.domain.real_estate.account_owner.account_owner_source import AccountOwnerSource
from hcad_star_schema.domain.real_estate.account_owner.account_owner_source import TabSeparatedAccountOwnerSource


class TestTabSeparatedAccountOwnerSourceShould(unittest.TestCase):
    def setUp(self):
        path = 'data/unit_test/real_acc.txt'
        source: AccountOwnerSource = TabSeparatedAccountOwnerSource(path)
        self.account_owner = next(iter(source))

    def test_read_acctount_id_for_each_row(self):
        self.assertEqual(self.account_owner._account_id, '0010010000013')
    
    def test_read_acctount_postal_code_for_each_row(self):
        self.assertEqual(self.account_owner._postal_code, '77002')

    @unittest.skip
    def test_read_total_approved_value(self):
        self.assertEqual(self.total_approved_value, 0)
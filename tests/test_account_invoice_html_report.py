# This file is part account_invoice_html_report module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountInvoiceHtmlReportTestCase(ModuleTestCase):
    'Test Account Invoice Html Report module'
    module = 'account_invoice_html_report'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountInvoiceHtmlReportTestCase))
    return suite

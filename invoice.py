#This file is part account_invoice_html_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
import os
from trytond.pool import Pool, PoolMeta
from trytond.config import config
from trytond.transaction import Transaction
from trytond.modules.html_report.html_report import HTMLReport

__all__ = ['InvoiceReport', 'Invoice']

STORE_REPORT = config.getint('html_report', 'store_report', default=False)


class InvoiceReport(HTMLReport):
    __metaclass__ = PoolMeta
    __name__ = 'account.invoice'

    @classmethod
    def execute(cls, ids, data):
        Invoice = Pool().get('account.invoice')

        invoice = Invoice(ids[0])

        context = Transaction().context
        context['report_lang'] = invoice.party.lang.code if invoice.party.lang \
            else Transaction().language
        context['report_translations'] = os.path.join(
            os.path.dirname(__file__), 'report', 'translations')
        with Transaction().set_context(**context):
            result = super(InvoiceReport, cls).execute(ids, data)
            return result


class Invoice:
    __metaclass__ = PoolMeta
    __name__ = 'account.invoice'

    def print_invoice(self):
        if STORE_REPORT:
            return super(Invoice, self).print_invoice()
        return

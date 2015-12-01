# This file is part of the sale_delivery_date_manual module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleDeliveryDateManualTestCase(ModuleTestCase):
    'Test Sale Delivery Date Manual module'
    module = 'sale_delivery_date_manual'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleDeliveryDateManualTestCase))
    return suite
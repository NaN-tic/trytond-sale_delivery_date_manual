#This file is part of the sale_delivery_date_manual module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['SaleLine']
__metaclass__ = PoolMeta


class SaleLine:
    __name__ = 'sale.line'
    delivery_date = fields.Date('Delivery Date',
        states={
            'invisible': Eval('type') != 'line',
            'required': Eval('type') == 'line',
            }, depends=['type'])

    def on_change_product(self):
        res = super(SaleLine, self).on_change_product()
        res['delivery_date'] = self.on_change_with_delivery_date()
        return res

    def on_change_quantity(self):
        res = super(SaleLine, self).on_change_quantity()
        res['delivery_date'] = self.on_change_with_delivery_date()
        return res

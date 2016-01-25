# This file is part of the sale_delivery_date_manual module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval


__all__ = ['SaleLine']
__metaclass__ = PoolMeta


class SaleLine:
    __name__ = 'sale.line'
    delivery_date_ = fields.Date('Delivery Date',
        states={
            'invisible': Eval('type') != 'line',
            'required': Eval('type') == 'line',
            }, depends=['type'])

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        if not cls.delivery_date.setter:
            cls.delivery_date.setter = 'set_delivery_date'
        if cls.delivery_date._field.readonly:
            cls.delivery_date._field.readonly = False

    @fields.depends('delivery_date_')
    def on_change_with_delivery_date(self, name=None):
        if self.delivery_date_:
            return self.delivery_date_
        return super(SaleLine, self).on_change_with_delivery_date(name)

    @classmethod
    def set_delivery_date(cls, lines, name, value):
        if not value:
            value = Pool().get('ir.date').today()
        cls.write(lines, {'delivery_date_': value})

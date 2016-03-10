# This file is part of the sale_delivery_date_manual module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond import backend
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval


__all__ = ['SaleLine']
__metaclass__ = PoolMeta


class SaleLine:
    __name__ = 'sale.line'
    shipping_date_ = fields.Date('Shipping Date',
        states={
            'invisible': Eval('type') != 'line',
            'required': Eval('type') == 'line',
            }, depends=['type'])

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        if not cls.shipping_date.setter:
            cls.shipping_date.setter = 'set_shipping_date'
        if cls.shipping_date._field.readonly:
            cls.shipping_date._field.readonly = False

    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        table = TableHandler(cls, module_name)

        # Migration from 3.8:
        #   - delivery_date renamed into shipping_date
        if table.column_exist('delivery_date'):
            table.column_rename('delivery_date', 'shipping_date')
        super(SaleLine, cls).__register__(module_name)

    @fields.depends('shipping_date_')
    def on_change_with_shipping_date(self, name=None):
        if self.shipping_date_:
            return self.shipping_date_
        return super(SaleLine, self).on_change_with_shipping_date(name)

    @classmethod
    def set_shipping_date(cls, lines, name, value):
        if not value:
            value = Pool().get('ir.date').today()
        cls.write(lines, {'shipping_date_': value})

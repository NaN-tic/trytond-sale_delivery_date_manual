#This file is part of the sale_delivery_date_manual module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .sale import *


def register():
    Pool.register(
        SaleLine,
        module='sale_delivery_date_manual', type_='model')

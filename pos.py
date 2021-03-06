# -*- coding: utf-8 -*-
# This file is part of the account_invoice_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['Pos']


class Pos:
    __name__ = 'account.pos'
    __metaclass__ = PoolMeta

    pos_do_not_report = fields.Boolean('Do not report')

    @staticmethod
    def default_pos_do_not_report():
        return False

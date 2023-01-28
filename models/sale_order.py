# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError,ValidationError
from odoo.tools import format_datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    date_receipt = fields.Datetime(string='Receipt Date', readonly=True,
                                   states={'draft': [('readonly', False)], 'sent': [('readonly', False)],
                                           'sale': [('readonly', False)]}, copy=False, )


    @api.constrains('date_order', 'date_receipt')
    def _check_date_receipt_range(self):
        for each in self:
            if each.date_order and each.date_receipt and each.date_order > each.date_receipt:
                raise ValidationError(_('%s : Receipt Date (%s) should be greater than Order Date (%s)', each.name,
                                        format_datetime(self.env, each.date_receipt),
                                        format_datetime(self.env, each.date_order)))

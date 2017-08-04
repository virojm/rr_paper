# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_rm = fields.Boolean(
        string='IS RM',
        default=lambda self:self._context.copy().get('is_rm', False),
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain=[('customer', '=', True)],
    )
    sale_ok = fields.Boolean(
        default=False,
    )

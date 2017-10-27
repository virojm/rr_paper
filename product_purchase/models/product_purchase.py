# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ProductTemplatePurchase(models.Model):
    _name = 'producttemplatepurchase'
    _inherit = 'product.product'
    partner_id = fields.Many2one(
        'res.partner',size=40,
    )

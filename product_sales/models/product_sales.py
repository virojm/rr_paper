# -*- coding: utf-8 -*-
from openerp import models, fields, api
class ProductTemplateSales(models.Model):
    _inherit = 'product.template'
    sale_partner_id = fields.Many2one(
        'res.partner',
        string="Customer",
        size=40,
    )

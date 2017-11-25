# -*- coding: utf-8 -*-
from openerp import models, fields, api
class ProductTemplateSales(models.Model):
    _inherit = 'product.template'

    def compute_default_product_condition(self):
        res = False
        if self.env.context.get('default_sale_ok', False):
            res = True  # After sale_ok is checked, res is sent to purchse_ok
        elif self.env.context.get('default_purchase_ok', False):
            res = True  # After purchase_ok is checked, res is sent to sale_ok
        return res

    sale_ok = fields.Boolean(
        default = compute_default_product_condition,
    )
    purchase_ok = fields.Boolean(
        default = compute_default_product_condition,
    )
    sale_partner_id = fields.Many2one(
        'res.partner',
#        domain=[('supplier', '!=', True)],
        domain=[('customer', '=', True)],
        string="Customer",
        size=80,
    )

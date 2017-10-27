# -*- coding: utf-8 -*-
from openerp import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_product_id = fields.Many2one(
        'product.template',
        string="Product",
    )

    @api.onchange('x_product_id')
    def _onchange_x_product(self):
        self.product_id = self.x_product_id.id

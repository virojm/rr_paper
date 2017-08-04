# -*- coding: utf-8 -*-
from openerp import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    purchase_ok = fields.Boolean(
        default=False,
    )

    @api.onchange('sale_ok')
    def _onchange_sale_ok(self):
        if self.sale_ok:
            self.purchase_ok = False

    @api.onchange('purchase_ok')
    def _onchange_purchase_ok(self):
        if self.purchase_ok:
            self.sale_ok = False

#-*- coding: utf-8 -*-
from openerp import models, fields, api
class BOMTemplate(models.Model):
    _inherit = 'mrp.bom'

    product_tmpl_id = fields.Many2one(
        'product.template', 'Product',
        domain="[('type', 'in', ['product', 'consu']),('purchase_ok','!=',True),]", required=True)

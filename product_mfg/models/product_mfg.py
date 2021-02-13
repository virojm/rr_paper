#-*- coding: utf-8 -*-
from openerp import models, fields, api
class ProductTemplateMfg(models.Model):
    _inherit = 'product.template'
    # purchase_partner_id = fields.Many2one(
    #     'res.partner',
    #     string="Supplier",
    #     size=80,
    # )

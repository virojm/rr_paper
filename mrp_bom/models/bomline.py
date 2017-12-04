from openerp import models, fields, api

class MRPBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    product_id = fields.Many2one(
        'product.product', 'Product', domain=[('sale_ok','!=', True)], required=True)

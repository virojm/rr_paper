from openerp import models, fields


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    production_id = fields.Many2one(
        'mrp.production',
        'Manufacturing Order',
    )

from openerp import models, fields, api

class MrpWorkOrder(models.Model):
    _inherit = 'mrp.workorder'

    final_lot_id = fields.Many2one(
        'stock.production.lot',
        'Current Lot',
        domain= "[('production_id','=', production_id)]")

    @api.multi
    def record_production(self):
        self.ensure_one()
        self.final_lot_id.production_id = self.production_id.id
        res = super(MrpWorkOrder, self).record_production()
        return res

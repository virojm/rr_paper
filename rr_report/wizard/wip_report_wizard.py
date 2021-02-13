# -*- coding: utf-8 -*-
from openerp import models, fields, api


class WipReportWizard(models.TransientModel):

    _name = 'wip.report.wizard'

    date_to = fields.Date(
        string='Date',
    )

    location_id = fields.Many2one(
        'stock.location',
        string="Location",
    )

    @api.multi
    def run_report(self):
        data = {'parameters': {}}
        report_name = 'wip_report'
        # For SQL, we search simply pass params
        data['parameters']['location_id'] = self.location_id.id
        data['parameters']['date_to'] = self.date_to
        res = {
            'type': 'ir.actions.report.xml',
            'report_name': report_name,
            'datas': data,
        }
        return res

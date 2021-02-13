# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Report2ReportWizard(models.TransientModel):

    _name = 'report2.report.wizard'

    @api.multi
    def run_report(self):
        data = {'parameters': {}}
        report_name = 'report2_report'
        res = {
            'type': 'ir.actions.report.xml',
            'report_name': report_name,
            'datas': data,
        }
        return res

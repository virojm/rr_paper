# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PPDailyReport(models.TransientModel):

    _name = "pp.daily.report"

    date_current = fields.Date(
        string="Current Date",
        required=True,
    )

    @api.multi
    def action_print_report(self, data):
        records = []
        wizard = self
        date_current = wizard.date_current

        report_name = "pp.daily.report.jasper"

        # Send parameter to print
        params = {
            'current_date': str(date_current),
        }
        data.update({'records': records, 'parameters': params})
        return self.env['report'].with_context(context=data).get_action(
            wizard,
            report_name,
            data=data,
        )

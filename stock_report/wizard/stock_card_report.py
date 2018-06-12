# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockCardReport(models.TransientModel):

    _name = "stock.card.report"

    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_end = fields.Date(
        string="Date End",
        required=True,
    )
    location_id = fields.Many2one(
        comodel_name="stock.location",
        string="Location",
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product",
        required=True,
    )
    location_id = fields.Many2one(
        comodel_name="stock.location",
        string="Location",
        required=True,
    )

    @api.multi
    def action_print_report(self, data):
        records = []
        wizard = self
        date_start = wizard.date_start
        date_end = wizard.date_end
        product_id = wizard.product_id.id
        location_id = wizard.location_id.id

        report_name = "stock.card.report.jasper"

        # Send parameter to print
        params = {
            'begin_date': str(date_start),
            'end_date': str(date_end),
            'product_id': product_id,
            'location_id': location_id,
        }
        data.update({'records': records, 'parameters': params})
        return self.env['report'].with_context(context=data).get_action(
            wizard,
            report_name,
            data=data,
        )

# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductLotReport(models.TransientModel):

    _name = "product.lot.report"

    product_ids = fields.Many2many(
        comodel_name="product.product",
        string="Products",
        required=True,
    )

    @api.multi
    def action_print_report(self, data):
        records = []
        wizard = self
        if not wizard.product_ids:
            return True
        product_ids = wizard.product_ids._ids
        report_name = "product.lot.report.jasper"
        product_str = ""
        for id in product_ids:
            product_str += str(id) + ','
        product_str = product_str[:-1]
        # Send parameter to print
        params = {
            'product_id': product_str,
        }
        data.update({'records': records, 'parameters': params})
        return self.env['report'].with_context(context=data).get_action(
            wizard,
            report_name,
            data=data,
        )

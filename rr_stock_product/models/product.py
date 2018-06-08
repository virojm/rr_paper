# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import datetime, timedelta


class Product(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        res = super(Product, self).create(vals)
        ean = self.rr_generate_ean(str(res.id))
        res.barcode = ean
        return res

    def generate_barcode(self):
        products = self.search([('barcode', '=', False)])
        for product in products:
            bar = self.rr_generate_ean(str(product.id))
            product.barcode = bar
            # print product.id
            # print product.barcode

    @api.model
    def rr_generate_ean(self, product_id):
        res = '0000000000000'
        today = datetime.today() + timedelta(hours=7)
        str_date = datetime.strftime(today, '%y%m%d')
        res = str_date + res[6:]
        # print res
        # print len(product_id)
        res = res[:-len(product_id)]
        res = res + product_id
        # print "=============================="
        # print res
        return res

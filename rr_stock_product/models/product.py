# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import datetime, timedelta

import math


class Product(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        res = super(Product, self).create(vals)
        ean = self.rr_generate_ean(str(res.id))
        res.barcode = ean
        return res

    def ean_checksum(self, eancode):
        """returns the checksum of an ean string of length 13, returns -1 if the string has the wrong length"""
        if len(eancode) != 13:
            return -1
        oddsum = 0
        evensum = 0
        eanvalue = eancode
        reversevalue = eanvalue[::-1]
        finalean = reversevalue[1:]

        for i in range(len(finalean)):
            if i % 2 == 0:
                oddsum += int(finalean[i])
            else:
                evensum += int(finalean[i])
        total = (oddsum * 3) + evensum

        check = int(10 - math.ceil(total % 10.0)) % 10
        return check

    def check_ean(eancode):
        """returns True if eancode is a valid ean13 string, or null"""
        if not eancode:
            return True
        if len(eancode) != 13:
            return False
        try:
            int(eancode)
        except:
            return False
        return ean_checksum(eancode) == int(eancode[-1])

    def generate_barcode(self):
        products = self.search([('barcode', '!=', False)])
        for product in products:
            bar = self.rr_generate_ean(str(product.id))
            product.barcode = bar
        print product.id
        print product.barcode

    @api.model
    def rr_generate_ean(self, product_id):
        res = '0000000000000'
        today = datetime.today() + timedelta(hours=7)
        str_date = datetime.strftime(today, '%y%m')
        bar_str = str_date
        resx = bar_str + res[1+len(bar_str)+len(product_id):]
        res = resx + str(product_id) + '0'

        # bar_str = str_date + str(product_id)
        # res = bar_str + res[len(bar_str):]
        # print resx
        # print res
        # print len(product_id)
        # print product_id
        check_digit = str(self.ean_checksum(res))
        res = res[:-len(check_digit)]
        res = res + check_digit
        # print "=============================="
        # print res
        # print check_digit
        return res
        # if len(res) < 13:
        #     res = res + '0' * (13 - len(res))
        # return res[:-1] + str(ean_checksum(res))
        # print res

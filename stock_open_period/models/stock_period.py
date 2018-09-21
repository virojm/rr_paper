# -*- coding: utf-8 -*-
from openerp import models, fields, api
from odoo.addons import decimal_precision as dp
from datetime import datetime


class StockPeriod(models.Model):
    _name = 'stock.period'

    name = fields.Char(
        string='Period Name',
    )
    date_open = fields.Datetime(
        string='Period Date',
    )
    period_lines = fields.One2many(
        'stock.period.line',
        'period_id',
        string='Stock Period Line',
    )

    def init_stock_period(self):
        # circulate each product and get quantity in each location
        date_stamp = fields.datetime.now()
        date_stamp = date_stamp.strftime('%Y-%m-%d %H:%M:%S')
        Product = self.env['product.product']
        Move = self.env['stock.move']
        Location = self.env['stock.location']
        SPLine = self.env['stock.period.line']
        products = Product.search([])
        stock_period = self.create({
            'date_open': date_stamp,
        })
        for product in products:
            locations = Location.search(
                [('usage', '=', 'internal')],
            )
            for location in locations:
                qty = 0.0
                in_moves = Move.search([
                    ('date','<=', date_stamp),
                    ('product_id', '=', product.id),
                    ('location_dest_id', '=', location.id),
                    ('location_id', '!=', location.id),
                    ('state', '=', 'done')
                ])
                out_moves = Move.search([
                    ('date','<=', date_stamp),
                    ('product_id', '=', product.id),
                    ('location_id', '=', location.id),
                    ('location_dest_id', '!=', location.id),
                    ('state', '=', 'done'),
                ])
                for in_move in in_moves:
                    qty += in_move.product_uom_qty
                for out_move in out_moves:
                    qty -= out_move.product_uom_qty
                SPLine.create({
                    'period_id': stock_period.id,
                    'product_id': product.id,
                    'uom_id': product.uom_id.id,
                    'product_qty': qty,
                    'location_id': location.id,
                })

    def calculate_from_last_period(self, last_period=False):
        Product = self.env['product.product']
        Move = self.env['stock.move']
        Location = self.env['stock.location']
        SPLine = self.env['stock.period.line']
        if last_period:
            date_stamp = fields.datetime.now()
            date_stamp = date_stamp.strftime('%Y-%m-%d %H:%M:%S')
            products = Product.search([])
            stock_period = self.create({
                'date_open': date_stamp,
            })
            for product in products:
                locations = Location.search(
                    [('usage', '=', 'internal')],
                )
                qty = 0.0
                process_move_qty = 0.0
                for location in locations:
                    in_moves = Move.search([
                        ('date','>', last_period.date_open),
                        ('date','<=', date_stamp),
                        ('product_id', '=', product.id),
                        ('location_dest_id', '=', location.id),
                        ('location_id', '!=', location.id),
                        ('state', '=', 'done')
                    ])
                    out_moves = Move.search([
                        ('date','>', last_period.date_open),
                        ('date','<=', date_stamp),
                        ('product_id', '=', product.id),
                        ('location_id', '=', location.id),
                        ('location_dest_id', '!=', location.id),
                        ('state', '=', 'done'),
                    ])
                    for in_move in in_moves:
                        process_move_qty += in_move.product_uom_qty
                    for out_move in out_moves:
                        process_move_qty -= out_move.product_uom_qty
                    # check product and location with last period line
                    last_lines = last_period.period_lines
                    for line in last_lines:
                        if line.product_id.id == product.id \
                            and line.location_id.id == location.id:
                            qty = line.product_qty + process_move_qty
                            break
                        else:
                            qty = process_move_qty
                SPLine.create({
                    'period_id': stock_period.id,
                    'product_id': product.id,
                    'uom_id': product.uom_id.id,
                    'product_qty': qty,
                    'location_id': location.id,
                })



    @api.model
    def calculate_on_hand(self):
        last_period = self.search([],order='id desc', limit=1)
        if not last_period:
            self.init_stock_period()
        else:
            self.calculate_from_last_period(last_period)

    @api.multi
    def recalculate_by_date(self):
        Product = self.env['product.product']
        Move = self.env['stock.move']
        Location = self.env['stock.location']
        SPLine = self.env['stock.period.line']
        for res in self:
            if res.date_open:
                # date_stamp = fields.datetime.now()
                # date_stamp = date_stamp.strftime('%Y-%m-%d %H:%M:%S')
                date_stamp = self.date_open
                res.period_lines.unlink()
                products = Product.search([])
                for product in products:
                    locations = Location.search(
                        [('usage', '=', 'internal')],
                    )
                    for location in locations:
                        qty = 0.0
                        in_moves = Move.search([
                            ('date', '<=', date_stamp),
                            ('product_id', '=', product.id),
                            ('location_dest_id', '=', location.id),
                            ('location_id', '!=', location.id),
                            ('state', '=', 'done')
                        ])
                        out_moves = Move.search([
                            ('date', '<=', date_stamp),
                            ('product_id', '=', product.id),
                            ('location_id', '=', location.id),
                            ('location_dest_id', '!=', location.id),
                            ('state', '=', 'done'),
                        ])
                        for in_move in in_moves:
                            qty += in_move.product_uom_qty
                        for out_move in out_moves:
                            qty -= out_move.product_uom_qty
                        SPLine.create({
                            'period_id': res.id,
                            'product_id': product.id,
                            'uom_id': product.uom_id.id,
                            'product_qty': qty,
                            'location_id': location.id,
                        })


class StockPeriodLine(models.Model):
    _name = 'stock.period.line'

    period_id = fields.Many2one(
        'stock.period',
        string='Stock Period',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    uom_id = fields.Many2one(
        'product.uom',
        string='Unit of Measure',
    )
    product_qty = fields.Float(
        string='Quantity',
        digits=dp.get_precision('Product Unit of Measure'),
    )
    location_id = fields.Many2one(
        'stock.location',
        string='Source Location',
    )

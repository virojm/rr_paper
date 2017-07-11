# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _layers = [('a', 'A'),
               ('b', 'B'),
               ('c', 'C'),
               ('d', 'D'),
               ]

    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain=[('customer', '=', True)],
    )
    # Layers
    layer1 = fields.Selection(
        selection=_layers,
        string='Layer 1',
    )
    layer2 = fields.Selection(
        selection=_layers,
        string='Layer 2',
    )
    layer3 = fields.Selection(
        selection=_layers,
        string='Layer 3',
    )
    layer4 = fields.Selection(
        selection=_layers,
        string='Layer 4',
    )
    layer5 = fields.Selection(
        selection=_layers,
        string='Layer 5',
    )
    layer6 = fields.Selection(
        selection=_layers,
        string='Layer 6',
    )
    layer7 = fields.Selection(
        selection=_layers,
        string='Layer 7',
    )
    layer8 = fields.Selection(
        selection=_layers,
        string='Layer 8',
    )
    # _sql_constraints = [
    #     ('layers_uniq',
    #      'UNIQUE(layer1,layer2,layer3,layer4,layer5,layer6,layer7,layer8,)',
    #      'Layers must be UNIQUE!'),
    # ]

    @api.constrains('layer1', 'layer2', 'layer3', 'layer4',
                    'layer5', 'layer6', 'layer7', 'layer8')
    def _check_partner_layers(self):
        for rec in self:
            if not rec.sale_ok:
                continue
            product = self.search([('partner_id', '=', rec.partner_id.id),
                                   ('layer1', '=', rec.layer1),
                                   ('layer2', '=', rec.layer2),
                                   ('layer3', '=', rec.layer3),
                                   ('layer4', '=', rec.layer4),
                                   ('layer5', '=', rec.layer5),
                                   ('layer6', '=', rec.layer6),
                                   ('layer7', '=', rec.layer7),
                                   ('layer8', '=', rec.layer8)])
            if len(product) > 1:
                raise ValidationError(_('Duplicate Partner/Layers!'))

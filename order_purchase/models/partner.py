from openerp import models,fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # tax_id = fields.Char('Tax ID',size=60)
    # person_name = fields.Char('Contact:')
    company_type = fields.Char(default='company')
    parent_id = fields.Many2one(
        'res.partner',
        domain=[('is_company','=', True)],
        size=80,
    )

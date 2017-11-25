from openerp import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    tax_id = fields.Char('Tax ID')
    is_company = fields.Boolean(default= True)
    company_type = fields.Char()

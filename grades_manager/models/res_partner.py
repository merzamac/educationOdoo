from odoo import models,fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    #_order = 'email' #oderna la lista por el campo email

    is_teacher = fields.Boolean(string='Is Teacher')

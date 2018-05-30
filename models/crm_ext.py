import odoo
from odoo import models,fields
class Project_ext(models.Model):
    _inherit = 'crm.lead'
    
    code_number = fields.Char('Code')
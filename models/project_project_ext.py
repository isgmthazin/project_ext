'''
Created on May 29, 2018

@author: isgm90
'''
import odoo
from odoo import models,fields
class Project_ext(models.Model):
    _inherit = 'project.project'
    
    code_number = fields.Char('Project Code')
    
class Project_task_ext(models.Model):
    _inherit = 'project.task'
    
    task_id = fields.Char("Task ID")
    
    
    
from odoo import models, fields, api

class Travel(models.Model):
    _name = 'travel.travel'
    _description = 'this model for travel history'

    name = fields.Char(string="Name")
    destination = fields.Char(string="Destination")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
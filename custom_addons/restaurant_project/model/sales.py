from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_new_field = fields.Char(string='Sale New Field')

from odoo import models, fields, api


class RestStaff(models.Model):
    _name = 'res.staff'  # (This is object of Model) This name write in security file res_staff
    _description = 'this model store the data of staff'

    name = fields.Char(string="Name", size=50)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('1', 'Male'), ('2', 'Female')],
                              string="Gender")  # if you doesn't provide string name is auto take "Gender" in views
    dob = fields.Date(string="Dob")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")

from odoo import models, fields

class Plants(models.Model):
    _name = 'nursery.plants'

    name = fields.Char(string='Plant Name')
    price = fields.Float()
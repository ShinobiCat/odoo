from odoo import models, fields

class ModelNurseryPlant(models.Model):
    _name = 'model_nursery_plant'

    name = fields.Char(string='Plant Name')
    price = fields.Float()
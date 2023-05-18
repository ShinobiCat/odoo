from odoo import models, fields

class GelatoProduct(models.Model):
    _name = 'gelato.product'
    _description = 'Gelato Product'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    sku = fields.Char(string='SKU', required=True)
    price = fields.Float(string='Price', required=True)
    gelato_product_id = fields.Char(string='Gelato Product ID')

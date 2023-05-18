from odoo import models, fields

class GelatoOrder(models.Model):
    _name = 'gelato.order'
    _description = 'Gelato Order'

    name = fields.Char(string='Name', required=True)
    gelato_order_id = fields.Char(string='Gelato Order ID')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('placed', 'Placed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')],
        string='Status', default='draft', required=True)
    product_ids = fields.Many2many('gelato.product', string='Products')

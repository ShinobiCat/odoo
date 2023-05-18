# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class x_gelato_connector(models.Model):
#     _name = 'x_gelato_connector.x_gelato_connector'
#     _description = 'x_gelato_connector.x_gelato_connector'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

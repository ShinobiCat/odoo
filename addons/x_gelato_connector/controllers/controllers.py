# -*- coding: utf-8 -*-
from odoo import http


class XGelatoConnector(http.Controller):
     @http.route('/x_gelato_connector/x_gelato_connector', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/x_gelato_connector/x_gelato_connector/objects', auth='public')
     def list(self, **kw):
         return http.request.render('x_gelato_connector.listing', {
             'root': '/x_gelato_connector/x_gelato_connector',
             'objects': http.request.env['x_gelato_connector.x_gelato_connector'].search([]),
         })

     @http.route('/x_gelato_connector/x_gelato_connector/objects/<model("x_gelato_connector.x_gelato_connector"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('x_gelato_connector.object', {
             'object': obj
         })

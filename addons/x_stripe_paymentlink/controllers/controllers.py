# -*- coding: utf-8 -*-
# from odoo import http


# class XStripePaymentlink(http.Controller):
#     @http.route('/x_stripe_paymentlink/x_stripe_paymentlink', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/x_stripe_paymentlink/x_stripe_paymentlink/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('x_stripe_paymentlink.listing', {
#             'root': '/x_stripe_paymentlink/x_stripe_paymentlink',
#             'objects': http.request.env['x_stripe_paymentlink.x_stripe_paymentlink'].search([]),
#         })

#     @http.route('/x_stripe_paymentlink/x_stripe_paymentlink/objects/<model("x_stripe_paymentlink.x_stripe_paymentlink"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('x_stripe_paymentlink.object', {
#             'object': obj
#         })

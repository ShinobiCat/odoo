class PaymentLinkController(http.Controller):
    @http.route('/payment/link', type='http', auth='public', website=True)
    def payment_link(self, **kwargs):
        product_id = int(kwargs.get('product_id', 0))
        
        if product_id:
            product = request.env['product.template'].browse(product_id)
            payment_link = product.payment_link if product.payment_link else False
        else:
            payment_link = False

        if payment_link:
            return request.render('x_stripe_paymentlink.payment_link', {
                'payment_link': payment_link,
            })
        else:
            # Doorsturen naar de standaard betaalroute van Stripe
            return request.redirect('/shop/payment')


from odoo import http
import requests

class GelatoController(http.Controller):
    
    @http.route('/gelato/import_products', type='json', auth='user')
    def import_products(self):
        # Retrieve Gelato API key and base URL from module settings
        api_key = http.request.env['ir.config_parameter'].sudo().get_param('gelato.api_key')
        base_url = http.request.env['ir.config_parameter'].sudo().get_param('gelato.base_url')

        # Make a request to the Gelato API to fetch products
        headers = {'Gelato-Api-Key': api_key}
        url = f"{base_url}/products"
        response = requests.get(url, headers=headers)

        # Process the response and import products to Odoo
        if response.status_code == 200:
            products = response.json().get('products', [])
            for product in products:
                self._create_or_update_product(product)
        
        return True

    @http.route('/gelato/place_order', type='json', auth='user')
    def place_order(self, order_id):
        # Retrieve Gelato API key and base URL from module settings
        api_key = http.request.env['ir.config_parameter'].sudo().get_param('gelato.api_key')
        base_url = http.request.env['ir.config_parameter'].sudo().get_param('gelato.base_url')

        # Retrieve the order from Odoo
        order = http.request.env['gelato.order'].sudo().browse(order_id)

        # Prepare the order data for the Gelato API
        order_data = {
            'name': order.name,
            # Include other required order details
            # ...
        }

        # Make a request to the Gelato API to place the order
        headers = {'Gelato-Api-Key': api_key}
        url = f"{base_url}/orders"
        response = requests.post(url, json=order_data, headers=headers)

        # Process the response and update the order status in Odoo
        if response.status_code == 201:
            order.write({'status': 'placed'})
        else:
            # Handle the case when order placement fails
            # ...
        
         # Return True to indicate success
         return True

    def _create_or_update_product(self, product):
        # Check if the product already exists in Odoo based on Gelato Product ID
        existing_product = http.request.env['gelato.product'].sudo().search([
            ('gelato_product_id', '=', product['id'])
        ], limit=1)

        # Prepare the product data for creation or update
        product_data = {
            'name': product['name'],
            'description': product['description'],
            'sku': product['sku'],
            'price': product['price'],
            'gelato_product_id': product['id'],
        }

        # Create or update the product in Odoo
        if existing_product:
            existing_product.write(product_data)
        else:
            http.request.env['gelato.product'].sudo().create(product_data)

# Odoo Gelato Connector

The Odoo Gelato Connector is a module that allows you to import products and place orders from your Odoo ecommerce store to Gelato, a print-on-demand service for printing and delivering custom products.

## Installation

To install the module, follow these steps:

1. Clone this repository to your local machine
2. Copy the `gelato_connector` folder to your Odoo addons folder (usually located at `/odoo/addons/`)
3. Install the module from the Odoo Apps interface
4. Go to the Gelato configuration settings and enter your Gelato API key, Gelato base URL, and app URL (if applicable)
5. Create a product category in Gelato if it does not exist already
6. Create a product in Odoo and map it to a product in Gelato
7. Place an order in Odoo and it will automatically be sent to Gelato for printing and delivery

## Configuration

The following settings can be configured from the Odoo interface:

- Gelato API key
- Gelato base URL
- App URL (for odoo > gelato portal integration)

## Usage

To use the module, simply create a product in Odoo and map it to a product in Gelato. When a customer places an order in Odoo, the order will automatically be sent to Gelato for printing and delivery.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any contributions and feedback.

## License

This module is licensed under the AGPL-3.0 License. See the `LICENSE` file for more information.


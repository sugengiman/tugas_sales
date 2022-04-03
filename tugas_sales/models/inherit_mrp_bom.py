from odoo import models, fields, api


class Inherit_Sale(models.Model):
    _inherit = 'sale.order'

    button_product_id = fields.Integer(string='Cost Production', required=True)

    # def button_product_id
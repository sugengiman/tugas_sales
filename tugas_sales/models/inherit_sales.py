from odoo import models


class Inherit_Sale(models.Model):
    _inherit = 'sale.order'

    # button_create_mo = fields.Integer(string='Cost Production', required=True)

    def button_create_mo(self):
        # self.state = 'done'
        create_mo = []
        mo_target = self.env['sale.order'].browse(self.id)


from odoo import models


class Inherit_Sale(models.Model):
    _inherit = 'sale.order'

    # button_create_mo = fields.Integer(string='Cost Production', required=True)

    def button_create_mo(self):
        # self.state = 'done'
        create_mo = []
        mo_target = self.env['sale.order'].browse(self.id)
        print("a")
        # for m in mo_target:
        #     create_mo.append([{
        #        'product_id' : m.order_line.product_id.id, 
        #        'product_uom_id' : m.order_line.product_id.bom_ids.product_uom_id.id,
        #        'bom_id' : m.order_line.product_id.bom_ids.id,
        #        'harga_bom' : m.order_line.product_id.bom_ids.harga_bom,
        #        'product_qty' : m.order_line.product_uom_qty,
        #        }])
            
        # auto_product_id = create_mo[0][0]("product_id")
        # auto_product_uom_id = create_mo[0][0]("product_uom_id")
        # auto_bom_id = create_mo[0][0]("bom_id")
        # auto_harga_bom = create_mo[0][0]("harga_bom")
        # auto_product_id = create_mo[0][0]("product_qty")
        
        # if auto_harga_bom:
        #     self.env['mrp.production'].create(
        #         {'product_id': auto_product_id, 'product_uom_id': auto_product_uom_id, 'bom_id': auto_bom_id, 'product_qty': auto_product_id})
        # else:
        #     pass
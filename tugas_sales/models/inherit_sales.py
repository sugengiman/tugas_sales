from odoo import models


class Inherit_Sale(models.Model):
    _inherit = 'sale.order'

    # button_create_mo = fields.Integer(string='Cost Production', required=True)

    def button_create_mo(self):
        for record in self.order_line:
            for bom_id in record.product_id.bom_ids:
                bom_data = record.env['mrp.bom'].search([('id', '=', bom_id.id)]).read()
                if bool(bom_data) == True:
                    record.env['mrp.production'].create({
                        'product_id': record.product_id.id, 
                        'product_uom_id': record.product_id.bom_ids.product_uom_id.id, 
                        'bom_id': bom_id.id, 
                        'product_qty': record.product_uom_qty})
    
    # def button_create_mo(self):
    #     # self.state = 'done'
    #     create_mo = []
    #     mo_target = self.env['sale.order'].browse(self.id)
    #     # BA = 5
    #     # print(BA)
    #     for m in mo_target:
    #         create_mo.append({
    #            'product_id' : m.order_line.product_id.id, 
    #            'product_uom_id' : m.order_line.product_id.bom_ids.product_uom_id.id,
    #            'bom_id' : m.order_line.product_id.bom_ids.id,
    #            'cost_production' : m.order_line.product_id.bom_ids.cost_production,
    #            'product_qty' : m.order_line.product_uom_qty,
    #            })
            
    #     auto_product_id = create_mo[0]["product_id"]
    #     auto_product_uom_id = create_mo[0]["product_uom_id"]
    #     auto_bom_id = create_mo[0]["bom_id"]
    #     auto_cost_production = create_mo[0]["cost_production"]
    #     auto_product_qty = create_mo[0]["product_qty"]
        
    #     if auto_cost_production:
    #         self.env['mrp.production'].create(
    #             {'product_id': auto_product_id, 'product_uom_id': auto_product_uom_id, 'bom_id': auto_bom_id, 'product_qty': auto_product_qty})
from odoo import models


class Inherit_Sale(models.Model):
    _inherit = 'sale.order'

    # button_create_mo = fields.Integer(string='Cost Production', required=True)

    def button_create_mo(self):
        # self.state = 'done'
        create_mo = []
        mo_target = self.env['sale.order'].browse(self.id)
        # BA = 5
        # print(BA)
        for m in mo_target:
            create_mo.append({
               'product_id' : m.order_line.product_id.id, 
               'product_uom_id' : m.order_line.product_id.bom_ids.product_uom_id.id,
               'bom_id' : m.order_line.product_id.bom_ids.id,
               'cost_production' : m.order_line.product_id.bom_ids.cost_production,
               'product_qty' : m.order_line.product_uom_qty,
               })
            
        auto_product_id = create_mo[0]["product_id"]
        auto_product_uom_id = create_mo[0]["product_uom_id"]
        auto_bom_id = create_mo[0]["bom_id"]
        auto_cost_production = create_mo[0]["cost_production"]
        auto_product_qty = create_mo[0]["product_qty"]
        
        if auto_cost_production:
            self.env['mrp.production'].create(
                {'product_id': auto_product_id, 'product_uom_id': auto_product_uom_id, 'bom_id': auto_bom_id, 'product_qty': auto_product_qty})
    
    # def button_create_mo(self):
    #     for record in self:
    #         bom = record.order_line.product_id.bom_ids.id
    #         if bom:
    #             self.env['mrp.production'].create(
    #                 {
    #                 'product_id': record.order_line.product_id.id,
    #                 'product_qty': record.order_line.product_uom_qty,
    #                 'product_uom_id': record.order_line.product_uom.id,
    #                 'bom_id': record.order_line.product_id.bom_ids.id,
    #                 })
    #         else:
    #             pass
            
    # def button_create_mo(self):
    #     target = []
    #     target_browse = self.env['sale.order'].browse(self.id)
    #     for k in target_browse:
    #         target.append({
    #             'product_id':k.order_line.product_id.id,
    #             'bom_id':k.order_line.product_id.bom_ids.id,
    #             'cost_production':k.order_line.product_id.bom_ids.cost_production,
    #             'product_qty':k.order_line.product_uom_qty,
    #             'product_uom_id':k.order_line.product_id.bom_ids.product_uom_id.id,
    #         })
    #     tar_product_id = target[0]["product_id"]
    #     tar_product_qty = target[0]["product_qty"]
    #     tar_bom_id = target[0]["bom_id"]
    #     tar_cost_production = target[0]["cost_production"]
    #     tar_product_uom_id = target[0]["product_uom_id"]
    #     if tar_cost_production > 0:
    #         self.env['mrp.production'].create({'product_id': tar_product_id, 'product_uom_id': tar_product_uom_id, 'bom_id': tar_bom_id, 'product_qty': tar_product_qty})
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class stockmovee(models.Model):
    _inherit = 'stock.move'
    
    customer_id = fields.Many2one(
        'res.partner', 'Customer ',
        states={'done': [('readonly', True)]})
    
    qty_kecil = fields.Float(string='Std Qty')
    qty_kecil_dus = fields.Float(string='Jml Std Qty')
    qty_besar = fields.Float(string='Std Qty')
    qty_besar_dus = fields.Float(string='Jml Std Qty')
    qty_non_std = fields.Float(string='Jml Std Qty')
    
    @api.multi
    def action_create_package(self):
        
        
        for ml in range(int(self.qty_kecil_dus)) :
            self.move_line_ids.create({
                'product_id' : self.product_id.id,
                'product_uom_id' : self.product_id.uom_id.id,
                'qty_done' : self.qty_kecil,
                'product_uom_id' : self.product_id.uom_id.id,
                'location_id' : self.location_id.id,
                'picking_id' : self.picking_id.id,
                'location_dest_id' : self.location_dest_id.id,
                'move_id' : self.id 
            })
            
        
            
        
    
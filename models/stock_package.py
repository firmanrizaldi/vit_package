
from odoo import api, fields, models
import time
import datetime
import logging
_logger = logging.getLogger(__name__)





class Package_Quant(models.Model):
    _inherit = "stock.quant.package"

    
    package_ids = fields.One2many('stock.quant.package', 'package_baru_id', string='Package')
    
    
    package_baru_id = fields.Many2one(
        string='Package Baru',
        comodel_name='stock.quant.package'
    )
    
    

    
    

# class vit_stock_package(models.Model):
#     _name = 'vit.stock_package'
#     _description = 'New Description'

    
#     product_id = fields.Many2one(
#         string='Product',
#         comodel_name='product.product'
#     )
    
    
#     partner_id = fields.Many2one(
#         string='Customer',
#         comodel_name='res.partner'
#     )
    
#     qty_kecil = fields.Float(string='Qty Kecil')
#     qty_besar = fields.Float(string='Qty Besar')
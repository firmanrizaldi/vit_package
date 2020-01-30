# -*- coding: utf-8 -*-
{
    'name': "Package Product ",

    'summary': """
        Package Product dari MO ke dalam package box besar dan kecil""",

    'description': """
        Package Product dari MO ke dalam package box besar dan kecil
    """,

    
    'author': 'firmanrizaldiyusup@gmail.com',
    'website': 'http://www.vitraining.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','vit_mrp_cost','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_stock.xml',
        'views/qty_product.xml',
        'views/package.xml',
        # 'data/ir_sequence_lot.xml',
        
    ],
  
}
# -*- coding: utf-8 -*-
{
    'name': "Check Sales CUIT",

    'summary': """
        Completa con un tilde si el partner posee cuit registrado
        
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Fabian Cerchi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_tree_custom.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "Saldo APP",

    'summary': """
        Saldo app, que permite al usuario gestionar sus ingresos y egresos de dinero.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Escuela FULLSTACK",
    'website': "http://www.escuelafullstack.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/movimientos.xml',
        'views/res_users.xml',
        'views/mi_perfil.xml',
        'views/movimiento_report_wizard.xml',
        'reports/movimiento_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
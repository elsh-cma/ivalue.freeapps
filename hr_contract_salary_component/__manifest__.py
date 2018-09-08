# -*- coding: utf-8 -*-
{
    'name': "Employee Salary Component",

    'summary': """
        Adding Basic and Variable Salary in Contract""",

    'description': """
        Adding Basic and Variable Salary in Contract
    """,

    'author': "I VALUE solutions",
    'website': "www.ivalue-s.com",
	'email': "info@ivalue-s.com",
    'license': "OPL-1",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_contract'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
	'images': ['static/description/Banner.png'],
}
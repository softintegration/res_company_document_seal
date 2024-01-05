# -*- coding: utf-8 -*-

{
    'name': 'Company document seal',
    'version': '1.0.1',
    'author': 'Soft-integration',
    'category': 'Base',
    'description': "",
    'depends': [
        'base'
    ],
    'data': [
        'security/res_company_document_seal_security.xml',
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

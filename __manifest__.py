# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'iSGM Project',
    'version': '1.1',
    'category': 'ISGM Project System',
    'sequence': 75,
    'summary': 'ISGM Project System',
    'description': """
ISGM Project System with version 10
==========================

This application enables you to manage projects...


You can manage:
---------------
    """,
    'website': '',
    'images': [
      
    ],
    'depends': [
        'base_setup','project','crm',

    ],
    'data': [
        'views/project_project_view.xml',
        'views/crm_ext_view.xml',
    ],
    'demo': [],
    'test': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}

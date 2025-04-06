# -*- coding: utf-8 -*-
{
    'name': 'Grades Manager',
    'summary': 'Handles grades among students and courses',
    'description': 'Handles grades among students and courses',
    'author': 'Moises Merza',
    'category': 'Base',
    'version': '17.0.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/grades_course_views.xml',
        'views/res_partner_views.xml',
        'views/grades_evaluation_views.xml',
        'views/grades_grade_views.xml',




        'views/grades_manager_menus.xml',

    ],
    'license': 'AGPL-3',
    'application':True,
    'installable': True,
    'auto_install': False,
}
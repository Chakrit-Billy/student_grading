{
    'name': 'Student Grading System',
    'version': '1.0',
    'summary': 'Manage student grades by teacher and subject',
    'category': 'Education',
    'author': 'Billy',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',
        'views/student_view.xml',
        'views/grade_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}

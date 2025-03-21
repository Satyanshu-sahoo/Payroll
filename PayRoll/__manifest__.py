{
    'name': 'PayRoll',
    'version': '1.0',
    'summary': 'HR and Payroll System for Indian Compliance',
    'description': """Manage employee payroll, salary components, deductions, and compliance.""",
    'author': 'Your Name',
    'category': 'Human Resources',
    'depends': ['hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
    'views/employee_views.xml',
        'views/salary_views.xml',
        
        'views/attendance_views.xml',
        'views/compliance_views.xml',
    ],
    'installable': True,
    'application': True,
}

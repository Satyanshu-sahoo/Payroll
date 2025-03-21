from odoo import models, fields

class HRPayrollEmployee(models.Model):
    _name = 'hr.payroll.employee'
    _description = 'Employee Information'

    name = fields.Char(string="Employee Name", required=True)
    employee_id = fields.Char(string="Employee ID", required=True, index=True)  
    department = fields.Char(string="Department")
    designation = fields.Char(string="Designation")
    
    date_of_joining = fields.Date(string="Date of Joining")
    date_of_termination = fields.Date(string="Date of Termination")
    termination_reason = fields.Text(string="Termination Reason")

    # Bank Account Details
    bank_account = fields.Char(string="Bank Account Number")
    bank_name = fields.Char(string="Bank Name")
    ifsc_code = fields.Char(string="IFSC Code")

    # Identification Details
  #  identification_id = fields.Char(string="Employee Identification")  # ✅ Added this field
    pan = fields.Char(string="PAN")
    aadhaar = fields.Char(string="Aadhaar Number")

    _sql_constraints = [
        ('unique_employee_id', 'unique(employee_id)', 'Employee ID must be unique!'),
    ]

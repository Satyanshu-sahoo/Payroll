from odoo import models, fields, api

class HRPayrollAttendance(models.Model):
    _name = 'hr.payroll.attendance'
    _description = 'Payroll Attendance'

    employee_id = fields.Many2one('hr.payroll.employee', string="Employee", required=True)
    employee_identification = fields.Char(string="Employee ID", readonly=True, store=True)

    work_days = fields.Integer(string="Work Days")
    leave_taken = fields.Integer(string="Leave Taken")
    overtime_hours = fields.Float(string="Overtime Hours")

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        """ Auto-fill Employee ID when Employee is selected """
        if self.employee_id:
            self.employee_identification = self.employee_id.employee_id  

    @api.model
    def create(self, vals):
        """ Ensure employee_identification is saved in the database """
        if 'employee_id' in vals:
            employee = self.env['hr.payroll.employee'].browse(vals['employee_id'])
            vals['employee_identification'] = employee.employee_id  
        return super(HRPayrollAttendance, self).create(vals)

    def write(self, vals):
        """ Ensure employee_identification updates on record update """
        if 'employee_id' in vals:
            employee = self.env['hr.payroll.employee'].browse(vals['employee_id'])
            vals['employee_identification'] = employee.employee_id  
        return super(HRPayrollAttendance, self).write(vals)

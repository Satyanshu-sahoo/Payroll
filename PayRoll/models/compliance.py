from odoo import models, fields, api

class HRPayrollCompliance(models.Model):
    _name = 'hr.payroll.compliance'
    _description = 'Statutory Compliance'

    employee_id = fields.Many2one('hr.payroll.employee', string="Employee", required=True)
    employee_identification = fields.Char(string="Employee ID", readonly=True, store=True)

    compliance = fields.Selection([
        ('1', 'Statutory Compliance'),
        ('2', 'Tax Compliance'),
        ('4', 'PF/ESI Compliance'),
        ('6', 'Other Compliance')],
        string="Compliance Type",
        help="Select the compliance type: Statutory, Tax, PF/ESI, or Other."
    )

    tax_filed = fields.Boolean(string="Tax Filed")
    pf_compliance = fields.Boolean(string="PF Compliance")
    esi_compliance = fields.Boolean(string="ESI Compliance")
    other_compliance = fields.Text(string="Other Compliance Notes")

    description = fields.Text(string="Additional Information")  # ✅ ADD THIS FIELD

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            self.employee_identification = self.employee_id.employee_id  

    @api.model
    def create(self, vals):
        if 'employee_id' in vals:
            employee = self.env['hr.payroll.employee'].browse(vals['employee_id'])
            vals['employee_identification'] = employee.employee_id  
        return super(HRPayrollCompliance, self).create(vals)

    def write(self, vals):
        if 'employee_id' in vals:
            employee = self.env['hr.payroll.employee'].browse(vals['employee_id'])
            vals['employee_identification'] = employee.employee_id  
        return super(HRPayrollCompliance, self).write(vals)

from odoo import models, fields, api

class HRPayrollSalary(models.Model):
    _name = 'hr.payroll.salary'
    _description = 'Salary Details'

    employee_id = fields.Many2one('hr.payroll.employee', string="Employee", required=True)
    employee_identification = fields.Char(string="Employee ID", compute="_compute_employee_identification", store=True)

    # Earnings
    basic_salary = fields.Float(string="Basic Salary", required=True, default=0.0)
    hra = fields.Float(string="House Rent Allowance", default=0.0)
    da = fields.Float(string="Dearness Allowance", default=0.0)
    conveyance_allowance = fields.Float(string="Conveyance Allowance", default=0.0)
    special_allowance = fields.Float(string="Special Allowance", default=0.0)
    bonus = fields.Float(string="Bonus", default=0.0)
    overtime_pay = fields.Float(string="Overtime Pay", default=0.0)
    gross_salary = fields.Float(string="Gross Salary", compute="_compute_gross_salary", store=True)

    # Deductions
    provident_fund = fields.Float(string="Provident Fund (PF)", default=0.0)
    esi = fields.Float(string="Employee State Insurance (ESI)", default=0.0)
    tds = fields.Float(string="Tax Deduction at Source (TDS)", default=0.0)
    professional_tax = fields.Float(string="Professional Tax (PT)", default=0.0)
    other_deductions = fields.Float(string="Other Deductions", default=0.0)
    deduction_remark = fields.Text(string="Remark for Other Deductions")
    total_deductions = fields.Float(string="Total Deductions", compute="_compute_total_deductions", store=True)

    # Net Salary
    net_salary = fields.Float(string="Net Salary", compute="_compute_net_salary", store=True)

    @api.depends('basic_salary', 'hra', 'da', 'conveyance_allowance', 'special_allowance', 'bonus', 'overtime_pay')
    def _compute_gross_salary(self):
        for record in self:
            record.gross_salary = (
                record.basic_salary + record.hra + record.da +
                record.conveyance_allowance + record.special_allowance +
                record.bonus + record.overtime_pay
            ) or 0.0  # Ensuring no None values

    @api.depends('provident_fund', 'esi', 'tds', 'professional_tax', 'other_deductions')
    def _compute_total_deductions(self):
        for record in self:
            record.total_deductions = (
                record.provident_fund + record.esi + record.tds +
                record.professional_tax + record.other_deductions
            ) or 0.0

    @api.depends('gross_salary', 'total_deductions')
    def _compute_net_salary(self):
        for record in self:
            record.net_salary = (record.gross_salary - record.total_deductions) or 0.0

    @api.depends('employee_id')
    def _compute_employee_identification(self):
        for record in self:
            record.employee_identification = record.employee_id.employee_id if record.employee_id else ''

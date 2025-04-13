from odoo import models, fields, api
from odoo.exceptions import ValidationError

class GradesGrade(models.Model):
    _name = 'grades.grade'
    _description = 'Grade Grade'

    student_id = fields.Many2one('res.partner',string="Student")
    value =fields.Integer(string="Value")
    date = fields.Date(string="Date",default=fields.Date.today())
    evaluation_id = fields.Many2one('grades.evaluation',string="Evaluation",readonly=True)


    @api.constrains('value')
    def check_value(self):
        for grade in self:
            if grade.value < 0 or grade.value > 10:
                raise ValidationError('Not Valid, 0-10')
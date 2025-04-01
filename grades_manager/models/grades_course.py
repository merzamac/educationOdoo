from tokenize import String
from odoo import models,fields
# modelo 1
# modelo abstracto ()
# modelo transitorio (wizard)

class GradesCourse(models.Model):
    #metadatos
    _name = 'grades.course'# nombre de la tabla db
    _description = 'Grades Course'
    _order = 'name'
    #_rec_name = ''

    #import fields
    name = fields.Char(string='Name')
    student_quantity = fields.Integer(string='Student quantity')
    grades_average = fields.Float(string='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is active')
    course_start = fields.Date(string='Course start')
    course_end = fields.Date(string='Course end')
    last_evaluation_date = fields.Date(string='Last evaluation date')
    course_image = fields.Binary(string='Course image')
    course_shift = fields.Selection([('day','Day'),('night','Night')],string='Course shift')

    teacher_id = fields.Many2one('res.partner',string='Teacher')
    evaluation_ids = fields.One2many('grades.evaluation','course_id',string='Evaluations')
    student_ids = fields.Many2many('res.partner', 'grades_course_students_rel',string='Students')

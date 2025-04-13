from tokenize import String
from odoo import models,fields, api
from odoo.exceptions import ValidationError
# modelo 1
# modelo abstracto ()
# modelo transitorio (wizard)

class GradesCourse(models.Model):
    #metadatos
    _name = 'grades.course'# nombre de la tabla db
    _description = 'Grades Course'
    _order = 'name'
    #_rec_name = ''
    #buscar porfesor
    def _default_teacher_id(self):
        return self.env['res.partner'].search([('is_teacher','=',True),('email','=','mainteacher@main.com')],limit=1).id
    #import fields
    name = fields.Char(string='Name')
    student_quantity = fields.Integer(string='Student quantity',compute='_compute_student_quantity',store=True)
    grades_average = fields.Float(string='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is active')
    course_start = fields.Date(string='Course start',default=fields.Date.today())
    course_end = fields.Date(string='Course end')
    last_evaluation_date = fields.Date(string='Last evaluation date',compute='_compute_last_evaluation_date',store=True)
    course_image = fields.Binary(string='Course image')
    course_shift = fields.Selection([('day','Day'),('night','Night')],string='Course shift')

    #realaciones
    #ondelete --> restrict,cascade ||  ondelete="restrict"
    teacher_id = fields.Many2one('res.partner',string='Teacher',default=_default_teacher_id)
    teacher_email =fields.Char(related="teacher_id.email",store=True)

    evaluation_ids = fields.One2many('grades.evaluation','course_id',string='Evaluations')
    student_ids = fields.Many2many('res.partner', 'grades_course_students_rel',string='Students')

    #estados
    state = fields.Selection(selection=[('register','Register'),('in_progress','In progress'),('finished','Finished')],string="State", required=True,default='register')

    invalid_date = fields.Boolean(string="Wrong date")
    type = fields.Selection([('basic','Basic'),('advanced','Advanced')],string='Type',defaul='Basic')
    def action_advanced_course_wizard(self):
        return {
            "type":"ir.actions.act_window",
            "name":"Create advanced course",
            "res_model": "advanced.course.wizard",
            "view_mode": "form",
            "target": "new",

        }

    #funcion write
    def write(self,vals):
        if vals and 'evaluation_ids' in vals and not self.student_ids:
            raise ValidationError('There are not students for this course')
        result = super(GradesCourse, self).write(vals)
        return  result

    #decorador
    @api.onchange('course_end','course_end')
    def onchange_dates(self):
        if (self.course_start and self.course_end and (self.course_end <= self.course_start or self.course_start >= self.course_end)):
            self.invalid_date = True
        else:
            self.invalid_date = False

    @api.depends('evaluation_ids.date')
    def _compute_last_evaluation_date(self):
        for course in self:
            if course.evaluation_ids:
                evaluations = course.evaluation_ids[-1]
                course.last_evaluation_date = evaluations.date

    @api.depends('student_ids')
    def _compute_student_quantity(self):
        self.student_quantity = len(self.student_ids)

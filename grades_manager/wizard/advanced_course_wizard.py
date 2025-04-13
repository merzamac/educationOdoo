from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AdvancedCourse(models.TransientModel):
    _name = "advanced.course.wizard"
    _description = "Advance course wizard"

    def _default_available_student_ids(self):
        course_ids = self._context.get('active_ids')
        courses = self.env['grades.course'].browse(course_ids)
        students = self.env['res.partner']
        for course in courses:
            students |= course.student_ids

        return students

    course_name = fields.Char(string='Course name')
    teacher_id = fields.Many2one('res.partner', string="Teacher")
    available_student_ids = fields.Many2many('res.partner', "wizard_avl_student_rel", string="Available students",
                                             default=_default_available_student_ids)

    student_ids = fields.Many2many('res.partner', 'wizard_student_rel', string="Students")

    def create_course(self):
        if not self.student_ids:
            raise ValidationError("you must assign at least one student")
        course = self.env['grades.course'].create({
            'name': self.course_name,
            'teacher_id': self.teacher_id.id,
            'type':'advanced',
            'student_ids': self.student_ids.ids

        })

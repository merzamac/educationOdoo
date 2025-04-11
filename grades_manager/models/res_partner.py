from odoo import models,fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    #_order = 'email' #oderna la lista por el campo email

    is_teacher = fields.Boolean(string='Is Teacher')
    is_freelance =fields.Boolean(string="Is Freelance")
    is_student = fields.Boolean(string='Is Student')
    vat = fields.Char(required=True, copy=False)

    #unlink eliminar registro
    # singelton: un solo registro
    # recordset: mas de 2 registro
    def unlink(self):
        for partner in self:
            if partner.email == 'mainteacher@main.com':
                courses = self.env['grades.course'].search([('teacher_id','=',partner.id)])
                secondary_teacher = self.env['res.partner'].search([('email','=','mainteacher@main.com')])
                courses.write({'teacher_id':secondary_teacher.id})
                #print(courses)
            result = super(ResPartner, self).unlink()
            return result
    #trae un singleton
    def copy(self, default=None):
        default = default or {}
        if self.is_teacher:
            default['name'] = 'Teacher '
        elif self.is_student:
            default['name'] = 'Student '
        res = super(ResPartner,self).copy(default)

        return  res
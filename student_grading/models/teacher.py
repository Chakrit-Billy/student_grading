from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string="Teacher Name", required=True)
    teacher_code = fields.Char(string="Teacher ID", required=True, unique=True)
    subject_ids = fields.Many2one('school.subject', string="Subjects")
    students = fields.Many2many('student.student', string="Students")
    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user, readonly=True)

    @api.model
    def create(self, vals):
        """ Prevent users from creating more than one student record """
        existing_student = self.search([('user_id', '=', self.env.uid)], limit=1)
        if existing_student:
            raise ValidationError("You can only create one student record.")
        return super(Teacher, self).create(vals)
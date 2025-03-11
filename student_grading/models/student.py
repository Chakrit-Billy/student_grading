from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    student_id = fields.Char(string="Student ID", required=True)
    age = fields.Integer(string="Age")
    class_level = fields.Char(string="Class Level")
    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user, readonly=True)

    @api.model
    def create(self, vals):
        """ Prevent users from creating more than one student record """
        existing_student = self.search([('user_id', '=', self.env.uid)], limit=1)
        if existing_student:
            raise ValidationError("You can only create one student record.")
        return super(Student, self).create(vals)

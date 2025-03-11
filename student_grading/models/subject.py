from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subjects'

    name = fields.Char(string="Subject Name", required=True)
    subject_code = fields.Char(string="Subject Code", required=True, unique=True)
    unit_ids = fields.One2many('subject.unit', 'subject_id', string="Units")  # One2many Relationship

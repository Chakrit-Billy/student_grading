from odoo import models, fields

class Subject(models.Model):
    _name = 'subject.unit'
    _description = 'Subjects'

    name = fields.Char(string="Unit Name", required=True)
    unit_code = fields.Char(string="Unit Code", required=True, unique=True)
    subject_id = fields.Many2one('school.subject', string="Subject", ondelete='cascade' , readonly=True)  # Many2one Relationship

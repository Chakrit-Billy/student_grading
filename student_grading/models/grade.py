from odoo import models, fields, api


class StudentGrade(models.Model):
    _name = 'student.grade'
    _description = 'Student Grade Record'
    _rec_name = 'student_name'

    student_id = fields.Many2one('student.student', string="Student", required=True)
    student_name = fields.Char(related='student_id.name', string="Student Name", store=False)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    unit = fields.Many2one('subject.unit', string="Unit", required=True, domain="[('subject_id', '=', subject_id)]")
    teacher_id = fields.Many2one('teacher.teacher', string="Teacher", required=True, domain="[('user_id', '=', uid)]")
    mark = fields.Float(string="Mark", required=True)
    grade = fields.Selection([
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')
    ], string="Grade")
    remarks = fields.Text(string="Remarks")

    @api.onchange('mark')
    def _onchange_mark(self):
        """Automatically update grade based on mark"""
        if self.mark >= 90:
            self.grade = 'A'
        elif self.mark >= 80:
            self.grade = 'B'
        elif self.mark >= 70:
            self.grade = 'C'
        elif self.mark >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    @api.model
    def _default_teacher_id(self):
        """Fetch default teacher_id from the logged-in user"""
        teacher = self.env['teacher.teacher'].search([('user_id', '=', self.env.uid)], limit=1)
        return teacher.id if teacher else False

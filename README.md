Student Grading System - Odoo 16
A custom Odoo 16 module for managing student grading, where teachers assign grades, students view their report cards, and admins manage subjects and teacher assignments.

Features
✅ Students

Can register and create only one student record.
Can view their own report card with grades by subject.
✅ Teachers

Can bind students to specific subjects.
Can grade students.
✅ Admins

Can create and manage subjects.
Can assign teachers to subjects.
Access Control
👨‍🎓 Student Role → Can manage only their own record.
👨‍🏫 Teacher Role → Can manage students and grades.
🔧 Admin Role → Full control over students, teachers, and subjects.

Installation
Copy the module into your Odoo custom addons folder.
Run:
bash
คัดลอก
แก้ไข
odoo-bin -c odoo.conf -u student_grading_module
Assign user roles via Settings > Users & Companies > Users.
Future Improvements
📊 Report Cards PDF Export
🎨 Improved UI/UX
📌 Attendance Tracking

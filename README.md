# 📘 Student Grading System - Odoo 16

A powerful **Odoo 16** module for managing student grades, allowing teachers to assign grades, students to view their report cards, and admins to manage subjects and teacher assignments.

---

## 🚀 Features
### ✅ **For Students**
- 📌 Can register and create **only one** student record.
- 📊 Can view their **own** report card with grades by subject.

### ✅ **For Teachers**
- 🏫 Can bind students to specific subjects.
- ✏️ Can **grade** students.

### ✅ **For Admins**
- 📚 Can create and manage **subjects**.
- 👨‍🏫 Can assign **teachers** to subjects.

---

## 🔐 Access Control
👨‍🎓 **Student Role** → Can only manage their own record.
👨‍🏫 **Teacher Role** → Can manage students and assign grades.
🔧 **Admin Role** → Full control over students, teachers, and subjects.

---

## 🛠️ Installation
1. Clone this repository into your Odoo **custom addons** folder:
   ```bash
   git clone git@github.com:Chakrit-Billy/student_grading.git
   ```
2. Restart Odoo and upgrade the module:
   ```bash
   odoo-bin -c odoo.conf -u student_grading
   ```
3. Assign user roles via **Settings > Users & Companies > Users**.

---

## 🎨 Future Improvements
- 📄 **Report Cards PDF Export**
- 🖥 **Improved UI/UX with modern design**
- 📌 **Attendance Tracking**

---

💡 **Contributions Welcome!** Feel free to open issues and submit pull requests. 😃


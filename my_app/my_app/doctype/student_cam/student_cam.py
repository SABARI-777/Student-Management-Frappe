# Copyright (c) 2026, sab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class studentcam(Document):
	pass
	# def before_insert(self):
	# 	self.status = "Active"
	# def before_validate(self):
	# 	self.student_name=self.student_name.upper()
	# def validate(self):
	# 	if self.age < 17:
	# 		frappe.throw("AGE MUST 18")
	# 	if len(str(self.phone).strip()) <= 10:
	# 		frappe.throw("MOBILE NUMBER VALIDTE")
	# 	if len(str(self.email).strip())<=1:
	# 		frappe.throw("ENTER EMAIL")
	# def before_save(self):
	# 	self.student_name=self.student_name.strip()
	# def after_insert(self):
	# 	frappe.msgprint("Student Created Successfully")
	# def on_update(self):
	# 	frappe.msgprint("Student Updated Successfully")
	
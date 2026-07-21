# Copyright (c) 2026, sab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FEES(Document):
    def validate(self):
        stu = frappe.get_doc("student-cam", self.student_name)

        stu.paid += self.amount
        stu.balance -= self.amount

        if stu.paid == stu.total:
            stu.feestatus = "PAID"
        elif stu.paid > 0:
            stu.feestatus = "PARTIAL-PAID"
        elif stu.paid == 0:
            stu.feestatus = "UNPAID"

        stu.save()
# Copyright (c) 2026, sab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class STUDENT(Document):

    # def before_insert(self):
    #     self.status = "ACTIVE"
    # def before_insert(self):
    #     self.status = "PENDING"

    # def before_validate(self):
    #     self.total = self.mark1 + self.mark2

    # def validate(self):
    #     frappe.msgprint(("Student {0} is validating !!!").format(self.name))

    # def before_save(self):
    #     frappe.msgprint("Before Save")

    # def after_insert(self):
    #     frappe.sendmail(
    #         recipients=[self.email],
    #         subject="Welcome to Our College",
    #         message=f"""
    #             <h3>Welcome, {self.name}!</h3>

    #             <p>Your student account has been created successfully.</p>

    #             <p><b>Department:</b> {self.dept}</p>

    #             <p>We wish you all the best in your studies.</p>

    #             <br>

    #             <p>Regards,<br>
    #             College Administration</p>
    #         """,
    #         now=True
    #     )

    # def on_update(self):
    #     frappe.msgprint("Data Saved Successfully")

    # def on_change(self):
    #     frappe.msgprint("Document Changed")

    # def before_submit(self):
    #     if self.document != "aadhar":
    #         frappe.msgprint("Please attach Aadhar document before submitting.")

    # def on_submit(self):
    #     frappe.msgprint("Submitted Successfully")

    # def before_cancel(self):
    #     if self.document == "aadhar":
    #         frappe.msgprint("Aadhar document is attached. You cannot cancel this invoice.")

    # def on_cancel(self):
    #     frappe.msgprint("Document Cancelled")

    # def on_trash(self):
    #     if self.document == "aadhar":
    #         frappe.throw("Cannot delete an aadhar student")

    # def after_delete(self):
    #     frappe.logger().info("Student deleted")


    def validate(self):
      

        att = frappe.new_doc("STUDENT")
        att.name = "SAMIII"
        att.insert()
        frappe.msgprint(f"Inserted: {att.name}")
    

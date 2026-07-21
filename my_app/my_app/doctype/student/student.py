# Copyright (c) 2026, sab and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class STUDENT(Document):

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

    # def before_validate(self):
    #     std = frappe.get_doc("STUDENT","STD-CSE-007")
    #     frappe.msgprint(std.name)

    # def validate(self):
    #     if self.flags.get("loops"):
    #         return

        # std = frappe.new_doc("STUDENT")
        # std.age=99
        # std.flags.loops=True
        # std.insert(ignore_permissions=True)


    # def on_submit(self):
    #     # frappe.delete_doc("STUDENT","STD-CSE-007",force=1)
    #     frappe.msgprint("dlts")

    # def after_insert(self):
    #     self.get_insert()
    
    # def get_insert(self):
    #     if self.flags.get("loops"):
    #         return
    #     stu = frappe.new_doc("STUDENT");
    #     stu.name="SABIII"
    #     stu.age=99
    #     stu.flags.loops=True
    #     stu.insert(ignore_permissions=True)
    #     # stu.insert();
    
    # def on_change(self):
    #     self.get_save()
    # def get_save(self):
    #     if self.flags.get("loops"):
    #         return
       
    #     stu =frappe.get_doc("STUDENT","STD-CSE-003")
    #     stu.age = 99
    #     stu.flags.loops=True
    #     stu.save()

    # def on_submit(self):
    #     self.get_del()
    # def get_del(self):
    #     frappe.delete_doc("STUDENT","STD--010",force=1)
    #     frappe.msgprint("STUDENT-003-DELETE")


#   def validate(self):
#     self.get_vals()

#   def get_vals(self):
#     frappe.db.set_value("STUDENT", "STD-CSE-003", "AGE",111)

#     name, age = frappe.db.get_value(
#         "STUDENT",
#         "CSE-00003",
#         ["name", "AGE"]
#     )
#     frappe.msgprint(str(age
#     ))

    # def validate(self):
    #     if frappe.db.exists("STUDENT","STD-CSE"):
    #         frappe.msgprint("YES!!!!!!!!!!!!!!!")
    #     else:
    #         frappe.msgprint("NO!!!!!!!!!!!!!!!!")
    

    # def validate(self):
    #     counts = frappe.db.count("STUDENT",{'dept':"CSE"})
    #     frappe.msgprint(("counts{0}").format(counts))

    # def validate(self):
    #     data = frappe.db.sql("""select age from `tabSTUDENT` where dept = 'CSE'""",as_dict=1)
    #     for d in data:
    #         frappe.msgprint(("AGE IS {0}").format(d.age))

import frappe
from frappe.model.document import Document

class STUDENT(Document):
    @frappe.whitelist()
    def show_message(self):
        frappe.msgprint("hello")
    pass

@frappe.whitelist()
def say_hello(name):
    return f"Hello {name}"
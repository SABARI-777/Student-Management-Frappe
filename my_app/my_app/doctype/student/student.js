// Copyright (c) 2026, sab and contributors
// For license information, please see license.txt
frappe.ui.form.on("STUDENT", {
    refresh(frm) {
        frm.call("show_message")
    },
});

frappe.ui.form.on("STUDENT", {
    refresh(frm) {
        frappe.call({
            method: "my_app.my_app.doctype.student.student.say_hello",
            args: {
                name: "Sabari"
            },
            callback: function(r) {
                frappe.msgprint(r.message);
            }
        });
    }
});
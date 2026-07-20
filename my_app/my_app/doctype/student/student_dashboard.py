from frappe import _

def get_data():
    return {
        "fieldname": "student",
        "transactions": [
            {
                "label": _("Academic"),
                "items": [
                    "ATTENDANCE",
                    "EXAMFEES"
                ]
            }
        ]
    }
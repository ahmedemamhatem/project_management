from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import datetime, timedelta, date



@frappe.whitelist()
def before_insert(doc, method=None):
    pass
@frappe.whitelist()
def after_insert(doc, method=None):
    pass
@frappe.whitelist()
def onload(doc, method=None):
    pass
@frappe.whitelist()
def before_validate(doc, method=None):
    pass
@frappe.whitelist()
def validate(doc, method=None):
    # Get today's date
    today = datetime.today().date()

    # Calculate three days ago
    three_days_ago = today - timedelta(days=3)

    for item in doc.items:
        if item.batch_no and item.manufacturing_date and item.manufacturing_date <= three_days_ago:
            frappe.throw(_(f"Manufacturing Date cannot be more than 3 days before today's date for Batch {item.batch_no} of Item {item.item_code} (Row {item.idx})."))
@frappe.whitelist()
def on_submit(doc, method=None):
    pass
@frappe.whitelist()
def on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update(doc, method=None):
    pass

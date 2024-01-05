from __future__ import unicode_literals
import frappe
from frappe import _


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
    if not doc.project:
        frappe.throw(_("Please select a project."))
    if not doc.items and doc.custom_get_item_from_project:
        # Fetching approved items using SQL query
        approved_items = frappe.db.sql("""
            SELECT item_code, item_name, brand, description, qty, uom, rate
            FROM `tabSystems Approved`
            WHERE parent = %s
        """, doc.project, as_dict=1)

        # Adding fetched items to the Sales Order
        for item in approved_items:
            doc.append("items", {
                "item_code": item.item_code,
                "item_name": item.item_name,
                "brand": item.brand,
                "description": item.description,
                "qty": item.qty,
                "uom": item.uom,
                "rate": item.rate,
                "delivery_date": doc.delivery_date,
                "conversion_factor": 1,
                "amount": item.qty * item.rate,
                # Add other necessary fields from the child table
            })
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

@frappe.whitelist()
def get_items(sales_order_name, project=None, method=None):
    pass

   
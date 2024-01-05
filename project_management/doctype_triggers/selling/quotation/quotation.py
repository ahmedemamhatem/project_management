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
    if not doc.items:
        items_list = frappe.db.sql(""" select item_code, 
                                        item_name,
                                        description,
                                        item_group,
                                        brand,
                                        stock_uom
                                                from `tabItem`
                                                where disabled = 0
                                                and is_sales_item = 1
                                    """, as_dict=1)
        for x in items_list:
            offered_item1 = doc.append("items", {})
            offered_item1.item_code = x.item_code
            offered_item1.item_name = x.item_name
            offered_item1.description = x.description
            offered_item1.item_group = x.item_group
            offered_item1.brand = x.brand
            offered_item1.uom = x.stock_uom
            offered_item1.stock_uom = x.stock_uom
            offered_item1.qty = 1
            offered_item1.conversion_factor = 1
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

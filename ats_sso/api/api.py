import frappe

@frappe.whitelist(allow_guest=True)
def sso_logout():
    # 1. Vidhi ka active session khatam karein
    if frappe.session.user and frappe.session.user != "Guest":
        frappe.local.login_manager.logout()
        frappe.db.commit()
    
    # 2. Query parameter se dynamic URL receive karein (agar na mile toh default ATS login)
    redirect_to = frappe.form_dict.get("redirect_to") or "https://ats.vaaman.in/Login"
    
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = redirect_to
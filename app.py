from flask import Flask, render_template, request, redirect, url_for, flash
import db  # our db.py file


from init_db import init_db 

app = Flask(__name__)
app.secret_key = "sravani_secret_code_9784464483"  # needed for flash messages

# Always ensure schema exists (DROP TABLE IF EXISTS inside schema.sql keeps it safe)
init_db()

# -------- HOME: LIST CONTACTS --------
@app.route("/")
def list_contacts():
    q = request.args.get("q", "").strip()  # read ?q= from URL

    if q:
        contacts = db.search_contacts(q)
    else:
        contacts = db.get_all_contacts()

    return render_template("list_contacts.html", contacts=contacts, q=q)
    #contacts = db.get_all_contacts()
    #return render_template("list_contacts.html", contacts=contacts)


# -------- CREATE CONTACT --------
@app.route("/contacts/new", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        address = request.form.get("address", "")

        if not name.strip():
            flash("Name is required", "danger")
            return redirect(url_for("add_contact"))

        db.create_contact(name, email, phone, address)
        flash("Contact added successfully!", "success")
        return redirect(url_for("list_contacts"))

    return render_template("add_contact.html")


# -------- EDIT CONTACT --------
@app.route("/contacts/<int:contact_id>/edit", methods=["GET", "POST"])
def edit_contact(contact_id):
    contact = db.get_contact(contact_id)
    if contact is None:
        flash("Contact not found", "warning")
        return redirect(url_for("list_contacts"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        address = request.form.get("address", "")

        if not name.strip():
            flash("Name is required", "danger")
            return redirect(url_for("edit_contact", contact_id=contact_id))

        db.update_contact(contact_id, name, email, phone, address)
        flash("Contact updated successfully!", "success")
        return redirect(url_for("list_contacts"))

    return render_template("edit_contact.html", contact=contact)


# -------- DELETE CONTACT --------
@app.route("/contacts/<int:contact_id>/delete", methods=["POST"])
def delete_contact_route(contact_id):
    db.delete_contact(contact_id)
    flash("Contact deleted successfully!", "info")
    return redirect(url_for("list_contacts"))


if __name__ == "__main__":
    app.run(debug=True)
#if __name__ == "__main__":
   # app.run(debug=True, ssl_context="adhoc")


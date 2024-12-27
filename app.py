from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import os
import json
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# JSON file path
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def find_contact_by_id(contacts, contact_id):
    for contact in contacts:
        if contact['id'] == contact_id:
            return contact
    return None

@app.route('/')
def index():
    contacts = load_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        new_contact = {
            'id': str(uuid4()),
            'name': request.form.get('name'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
            'address': request.form.get('address'),
            'category': request.form.get('category'),
            'notes': request.form.get('notes'),
            'favorite': 'favorite' in request.form,
            'created_at': datetime.utcnow().isoformat()
        }
        
        contacts = load_contacts()
        contacts.append(new_contact)
        save_contacts(contacts)
        
        flash('Contact added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_contact.html')

@app.route('/edit_contact/<string:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contacts = load_contacts()
    contact = find_contact_by_id(contacts, id)
    
    if not contact:
        flash('Contact not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        contact.update({
            'name': request.form.get('name'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
            'address': request.form.get('address'),
            'category': request.form.get('category'),
            'notes': request.form.get('notes'),
            'favorite': 'favorite' in request.form
        })
        save_contacts(contacts)
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_contact.html', contact=contact)

@app.route('/delete_contact/<string:id>')
def delete_contact(id):
    contacts = load_contacts()
    contacts = [c for c in contacts if c['id'] != id]
    save_contacts(contacts)
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle_favorite/<string:id>')
def toggle_favorite(id):
    contacts = load_contacts()
    contact = find_contact_by_id(contacts, id)
    
    if contact:
        contact['favorite'] = not contact['favorite']
        save_contacts(contacts)
        return jsonify({'status': 'success', 'favorite': contact['favorite']})
    
    return jsonify({'status': 'error', 'message': 'Contact not found'}), 404

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    contacts = load_contacts()
    
    if query:
        contacts = [
            contact for contact in contacts
            if query in contact['name'].lower() or
               query in contact['phone'].lower() or
               (contact['email'] and query in contact['email'].lower())
        ]
    
    return render_template('search_results.html', contacts=contacts, query=query)

if __name__ == '__main__':
    app.run(debug=True)

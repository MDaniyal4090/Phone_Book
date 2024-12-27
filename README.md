# Phone Book Application

A modern and feature-rich contact management system built with Flask, featuring a clean and responsive user interface.

## Features

- 📞 Contact Management
  - Add, edit, and delete contacts
  - Store multiple details: name, phone, email, address
  - Add personal notes for each contact
  - Categorize contacts (Family, Friend, Work, Emergency)
  - Mark contacts as favorites

- 🔍 Advanced Search
  - Search across all contact fields
  - Real-time search results
  - Clear search result display

- 💫 Modern UI/UX
  - Clean and responsive design
  - Intuitive navigation
  - Card-based contact display
  - Smooth animations and transitions
  - Mobile-friendly layout

- 🛠️ Technical Features
  - JSON-based data storage
  - No database setup required
  - Easy data backup and transfer
  - Lightweight and portable

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd phone-book
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
Phone Book/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── contacts.json      # Contact data storage
├── static/
│   ├── css/
│   │   └── style.css  # Custom styles
│   └── js/
│       └── main.js    # JavaScript functionality
└── templates/
    ├── base.html      # Base template
    ├── index.html     # Home page
    ├── add_contact.html    # Add contact form
    ├── edit_contact.html   # Edit contact form
    └── search_results.html # Search results page
```

## Dependencies

- Flask 3.0.0
- Flask-WTF 1.2.1
- email-validator 2.1.0.post1
- Werkzeug 3.0.1

## Usage

1. **Adding Contacts**
   - Click "Add New Contact" button
   - Fill in contact details
   - Click "Add Contact" to save

2. **Editing Contacts**
   - Click "Edit" on any contact card
   - Modify the details
   - Click "Update Contact" to save changes

3. **Deleting Contacts**
   - Click "Delete" on any contact card
   - Confirm deletion in the popup modal

4. **Searching Contacts**
   - Use the search bar in the navigation
   - Results update as you type
   - Search works across name, phone, and email fields

5. **Managing Favorites**
   - Click the star icon to toggle favorite status
   - Favorites are highlighted with a filled star

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Bootstrap for the UI components
- Bootstrap Icons for the icon set
- Flask community for the excellent web framework

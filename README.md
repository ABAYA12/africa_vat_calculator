# VAT Calculator Web Application

This project is a web-based VAT (Value Added Tax) calculator for 54 African countries. It can calculate the VAT amount for given prices and countries, and also provide the VAT rate for a specific country.

## Project Structure
vat_calculator/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── static/
│ │ └── styles.css
│ └── templates/
│ ├── base.html
│ ├── index.html
│ ├── rate.html
│ └── about.html
├── vat_rates.py
├── requirements.txt
└── README.md

### Files and Their Functions

- **`app/__init__.py`**: Initializes the Flask application.
- **`app/routes.py`**: Contains the routes for handling user requests.
- **`app/static/styles.css`**: CSS file for styling the web pages.
- **`app/templates/base.html`**: Base HTML template for the application.
- **`app/templates/index.html`**: HTML template for the main page.
- **`app/templates/rate.html`**: HTML template for checking VAT rates.
- **`app/templates/about.html`**: HTML template for the about page.
- **`vat_rates.py`**: Contains a dictionary with the VAT rates for 54 African countries.
- **`README.md`**: Provides detailed documentation for the project.
- **`requirements.txt`**: Lists the dependencies required to run the project.

## Requirements

- Flask
- Python

Install the required packages using the following command:

`pip install -r requirements.txt`

# Run the program
- `flask run`

# Usage
- Open a web browser and navigate to http://127.0.0.1:5000/.
## Home Page
- Enter prices separated by commas.
- Select one or more countries from the dropdown menu.
- Click "Calculate VAT" to see the results.
## Check VAT Rate
- Navigate to the "Check VAT rate" page.
- Select a country from the dropdown menu.
- Click "Check VAT Rate" to see the VAT rate for the selected country.

# About
- Navigate to the "About" page to learn more about the application.



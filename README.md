# PDF Creator - Flask Data Entry and PDF Export

A simple Flask web app to:

- Collect user data (name, email, message) from a web form
- Save submitted data to a local JSON file (`data_store.json`)
- Generate a downloadable PDF report of all stored records

## Features

- Minimal data entry form UI
- Persistent local storage using JSON
- PDF export using ReportLab
- Lightweight and easy to run locally

## Tech Stack

- Python
- Flask
- ReportLab
- HTML/CSS (template in `templates/index.html`)

## Project Structure

```text
pdf creator/
|-- App.py
|-- data_store.json
`-- templates/
    `-- index.html
```

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Open terminal in the project folder:

```powershell
cd "c:\pdf creator"
```

2. (Optional but recommended) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install flask reportlab
```

## Run the App

```powershell
python App.py
```

The app starts in debug mode and is usually available at:

- http://127.0.0.1:5000/

## How to Use

1. Open the home page.
2. Fill in Name, Email, and Message.
3. Click **Save Data** to store the entry in `data_store.json`.
4. Click **Generate and Print All Data as PDF** to download `stored_data_report.pdf`.

## Available Routes

- `GET /` - Render the main form page
- `POST /submit` - Save form data to `data_store.json`
- `GET /print_pdf` - Generate and download PDF report from saved data

## Notes

- Data is stored in a local JSON file and is not encrypted.
- `App.py` runs with `debug=True`; disable debug mode for production use.

## Future Improvements

- Add input validation and error handling
- Add database storage (SQLite/PostgreSQL)
- Add pagination/styling for long PDF reports
- Add tests for routes and PDF generation

## License

Add your preferred license (for example, MIT) in a `LICENSE` file.

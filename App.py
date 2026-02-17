from flask import Flask, render_template, request, send_file
import json
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
DATA_FILE = 'data_store.json'

# Helper function to load data
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Helper function to save data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    # This will look for a template file in a 'templates' folder
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    new_entry = {
        'name': request.form['name'],
        'email': request.form['email'],
        'message': request.form['message']
    }
    data = load_data()
    data.append(new_entry)
    save_data(data)
    return "Data submitted successfully! <a href='/'>Go Home</a>"

# --- ALL ROUTES MUST BE DEFINED ABOVE THIS LINE ---

@app.route('/print_pdf')
def print_pdf():
    data = load_data()
    
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    
    # Create the PDF object, using the buffer as its file.
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Stored Application Data Report")
    p.drawString(100, 730, f"Total Records: {len(data)}")

    y_position = 700
    for item in data:
        if y_position < 100:
            p.showPage()
            y_position = 750 # Reset position for new page
        
        p.drawString(100, y_position, f"Name: {item['name']}, Email: {item['email']}")
        p.drawString(120, y_position - 15, f"Message: {item['message'][:50]}...")
        y_position -= 40
        
    # Close the PDF object cleanly.
    p.showPage()
    p.save()
    
    # File pointer seeks back to the beginning to send the data.
    buffer.seek(0)
    
    return send_file(buffer, 
                     mimetype='application/pdf', 
                     as_attachment=True,         
                     download_name='stored_data_report.pdf')

if __name__ == '__main__':
    app.run(debug=True)


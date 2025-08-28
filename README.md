## Resume-AI

An AI-powered tool to extract keywords from job descriptions and match them against resumes. It also extracts emails and phone numbers from the uploaded resume.

### Overview
- Input a PDF resume and a job description
- Compute a match score and see which keywords were found/missing
- Extract contact information (emails, phone numbers)

---

## Prerequisites
- Python 3.9+ recommended
- pip (Python package manager)
- Git (optional, for cloning)

---

## Installation

### 1) Clone the repository
```bash
git clone https://github.com/yourusername/Resume-AI.git
cd Resume-AI
```

### 2) (Optional) Create and activate a virtual environment
```bash
# Create
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the App

### Start the Streamlit server
```bash
streamlit - python -m streamlit run UI.py --server.headless true --server.port 8501
```

Then open your browser at `http://localhost:8501` (Streamlit will also open it automatically).

---

## Usage
1. Upload a PDF resume (ensure it is text-based, not scanned-only images)
2. Paste the job description text in the sidebar (or upload a `.txt` file if supported)
3. Click "Compute Match Score" to get:
   - Match percentage
   - Keywords found and missing
   - Suggestions to improve
4. Click "Extract Contacts" to detect emails and phone numbers

---

## Project Structure
```text
Resume-AI/
├── UI.py                # Streamlit UI and orchestration
├── matcher.py           # Core matching and keyword extraction logic
├── requirements.txt     # Python dependencies
├── resume/              # (Optional) Sample resumes or test data
├── job_description/     # (Optional) Sample resumes or test data
├── main.py              # Runs the Resume AI from the command line without the UI.
└── README.md            # Documentation
```

---

## Development
- Run formatting/linting if configured
- Add unit tests for new logic where applicable
- Keep `requirements.txt` updated when adding dependencies

### Common Commands
```bash
# Install deps
pip install -r requirements.txt

# Run app
streamlit run app.py

# Export exact versions (optional)
pip freeze > requirements.txt
```

---

## Troubleshooting
- If the PDF is image-only, use OCR tools to convert to text first
- If `streamlit` command is not found, ensure the virtual environment is activated
- If port 8501 is busy, Streamlit will prompt to use another port

---

## Contributing
1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "feat: add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License
MIT License

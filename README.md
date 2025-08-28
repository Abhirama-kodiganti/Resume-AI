# ==============================================
# Resume Keyword Matcher AI – RAFT3DCC5
# ==============================================
# An AI-powered tool to extract keywords from job descriptions
# and match them against resumes. Also extracts contact info.
# ==============================================

# ----------------------------------------------
# Step 1: Clone the repository
# ----------------------------------------------
git clone https://github.com/yourusername/RAFT3DCC5.git
cd RAFT3DCC5

# ----------------------------------------------
# Step 2: (Optional) Create a Python virtual environment
# ----------------------------------------------
python -m venv venv                # create virtual environment
# Linux / Mac
source venv/bin/activate           
# Windows
# venv\Scripts\activate

# ----------------------------------------------
# Step 3: Install required dependencies
# ----------------------------------------------
pip install -r requirements.txt

# ----------------------------------------------
# Step 4: Run the Streamlit application
# ----------------------------------------------
streamlit run app.py
# The app will open in your browser at http://localhost:8501

# ----------------------------------------------
# Step 5: Using the Application
# ----------------------------------------------
# 1️⃣ Upload Resume
#    - Upload your PDF resume (must be text-based)
#    - Supported formats: .pdf
#
# 2️⃣ Enter Job Description
#    - Paste the job description in the sidebar or upload a .txt file
#
# 3️⃣ Compute Match Score
#    - Click “Compute Match Score”
#    - Output shows:
#       • Match percentage
#       • Keywords found
#       • Suggestions to improve
#
# 4️⃣ Extract Contacts
#    - Click “Extract Contacts”
#    - Emails and phone numbers will be detected

# ----------------------------------------------
# Step 6: Project Structure
# ----------------------------------------------
# RAFT3DCC5/
# ├── app.py                # Streamlit frontend
# ├── matcher.py            # Core AI logic
# ├── requirements.txt      # Python dependencies
# ├── data/                 # Optional test resumes
# └── README.md             # Documentation

# ----------------------------------------------
# Step 7: Example Run
# ----------------------------------------------
# streamlit run app.py
# Upload resume.pdf, enter job description, click Compute Match Score
# Sample Output:
# Match Score: 85%
# Suggested Keywords to Add: Python, AWS, Docker
# Contacts Found:
# - Email: example@gmail.com
# - Phone: +91 9876543210

# ----------------------------------------------
# Step 8: Contributing
# ----------------------------------------------
# 1. Fork the repository
# 2. Create a branch: git checkout -b feature/your-feature
# 3. Make changes and commit: git commit -m "Add feature"
# 4. Push: git push origin feature/your-feature
# 5. Open a Pull Request

# ----------------------------------------------
# Step 9: License
# ----------------------------------------------
# MIT License

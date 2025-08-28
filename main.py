import os
from matcher import extract_text_from_pdf, get_keywords, match_score

# Paths
resume_path = "resumes/sample_resume.pdf"
job_desc_folder = "job_descriptions/"

if not os.path.exists(resume_path):
    raise FileNotFoundError(f"Resume not found at {resume_path}")

# Extract resume keywords
resume_text = extract_text_from_pdf(resume_path)
resume_keywords = get_keywords(resume_text)

"""Process job descriptions in .pdf or .txt format."""
for filename in os.listdir(job_desc_folder):
    if not (filename.endswith(".pdf") or filename.endswith(".txt")):
        continue

    jd_path = os.path.join(job_desc_folder, filename)

    if filename.endswith(".txt"):
        try:
            with open(jd_path, "r", encoding="utf-8", errors="ignore") as f:
                job_text = f.read()
        except Exception:
            job_text = ""
    else:
        job_text = extract_text_from_pdf(jd_path)

    if not job_text.strip():
        print(f"--- {filename} ---")
        if filename.endswith(".pdf"):
            print("Could not read PDF (skipped). Only text-based PDFs are supported.")
        else:
            print("Could not read text file (skipped).")
        print()
        continue

    job_keywords = get_keywords(job_text)
    score, matched = match_score(resume_keywords, job_keywords)

    print(f"--- {filename} ---")
    print(f"Resume Match Score: {score:.2f}%")
    print("Matched Keywords:", sorted(matched))
    print()

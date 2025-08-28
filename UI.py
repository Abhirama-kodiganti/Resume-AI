import streamlit as st
from matcher import extract_text_from_pdf, get_keywords, match_score, extract_contacts

# --- Page setup ---
st.set_page_config(
    page_title="Resume Keyword Matcher",
    page_icon="📄",
    layout="wide"
)

# --- Sidebar ---
st.sidebar.title("💡 Tips for Best Results")
st.sidebar.markdown("""
- Use a **text-based PDF** for your resume (no scanned images).  
- Job descriptions should be **plain text (.txt)**.  
- Keep your resume updated with **skills and keywords** matching the role.  
""")

# --- Title & Description ---
st.title("📄 Resume Keyword Matcher")
st.markdown("""
**Description:**  
Upload your **resume (PDF)** and one or more **job description (.txt)** files.  
The tool will analyze your resume against each job description and show a match score with key matching skills/keywords.
""")

# --- File upload ---
col1, col2 = st.columns(2)
with col1:
    resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
with col2:
    job_files = st.file_uploader(
        "Upload Job Description(s) (.txt)", type="txt", accept_multiple_files=True
    )

# --- Pretty contacts helpers ---
def shorten_text(text, max_len=32):
    if not text:
        return "-"
    if len(text) <= max_len:
        return text
    return text[: max_len // 2] + "…" + text[-max_len // 2 :]

def normalize_url(url: str) -> str:
    if not url:
        return ""
    url = url.strip()
    if url.startswith("mailto:") or url.startswith("tel:"):
        return url
    if url.startswith("http://") or url.startswith("https://"):
        return url
    # If it's a bare domain, assume https
    return "https://" + url

def chip(label: str, value: str, href: str | None = None, color: str = "#3B82F6"):
    display = shorten_text(value)
    target = normalize_url(href or value)
    if not value:
        display = "-"
        target = ""
    chip_html = f"""
    <a href='{target}' target='_blank' style='
        text-decoration:none; margin-right:8px;'
        title='{value}'>
      <span style='
          display:inline-flex; align-items:center; gap:8px;
          background:{color}1A; color:{color}; border:1px solid {color}33;
          padding:8px 12px; border-radius:999px; font-weight:600; font-size:14px;'>
        <span style='opacity:.9'>{label}</span>
        <span style='max-width:260px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;'>
          {display}
        </span>
      </span>
    </a>
    """
    st.markdown(chip_html, unsafe_allow_html=True)

# Global minimal CSS polish
st.markdown(
    """
    <style>
      .block-container {padding-top: 1.5rem;}
      h1, h2, h3 {letter-spacing: 0.2px}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Run Analysis ---
if st.button("Run Analysis"):
    if not resume_file or not job_files:
        st.warning("Please upload a Resume PDF and at least one Job Description TXT.")
    else:
        # Resume text + contacts
        resume_text = extract_text_from_pdf(resume_file)
        resume_keywords = get_keywords(resume_text)
        contacts = extract_contacts(resume_text, resume_file)

        st.subheader("👤 Extracted Contacts")
        c1, c2 = st.columns([2, 3])
        with c1:
            chip("🔗 LinkedIn", contacts.get("linkedin") or "", href=contacts.get("linkedin"), color="#0A66C2")
            chip("💻 GitHub", contacts.get("github") or "", href=contacts.get("github"), color="#24292F")
        with c2:
            # mailto: and tel: links
            email_value = contacts.get("email") or ""
            phone_value = contacts.get("phone") or ""
            chip("✉️ Email", email_value, href=("mailto:" + email_value if email_value else None), color="#10B981")
            chip("📞 Phone", phone_value, href=("tel:" + phone_value if phone_value else None), color="#F59E0B")

        # Multi JD comparison
        st.subheader("📊 Results")
        for job_file in job_files:
            try:
                job_text = job_file.read().decode("utf-8", errors="ignore")
            except Exception:
                job_text = ""

            if not job_text.strip():
                st.error(f"Could not read the job description file: {job_file.name}")
                continue

            job_keywords = get_keywords(job_text)
            score, matched = match_score(resume_keywords, job_keywords)

            # Color coding
            if score >= 50:
                score_color = "green"
            else:
                score_color = "orange"

            with st.expander(f"{job_file.name}: Match Details"):
                # Show score big and colored with a gradient badge
                st.markdown(
                    f"""
                    <div style='display:flex;align-items:center;gap:12px;'>
                      <div style='font-size:28px;font-weight:800;color:{score_color};'>
                        {score:.2f}% Match
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown("**Matched Keywords:**")
                st.write(", ".join(sorted(matched)))

                cols = st.columns(2)
                with cols[0]:
                    st.markdown("**Resume Text**")
                    st.write(resume_text)
                with cols[1]:
                    st.markdown("**Job Description Text**")
                    st.write(job_text)

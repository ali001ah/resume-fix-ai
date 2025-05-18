
import streamlit as st
import requests

st.set_page_config(page_title="ResumeFix AI", page_icon="🧠")
st.title("🧠 ResumeFix AI")
st.write("Enhance your resume instantly using powerful AI.")

with st.expander("ℹ️ How it works"):
    st.markdown("""
    1. Paste your resume into the box.
    2. Enter the job title you're targeting.
    3. Click 'Enhance Resume' to get an improved version tailored to your role.
    """)

resume_input = st.text_area("📄 Paste your current resume here:")
job_title = st.text_input("🎯 What job are you applying for?")

if st.button("✨ Enhance Resume"):
    if not resume_input or not job_title:
        st.warning("Please provide both a resume and a job title.")
    else:
        with st.spinner("Contacting AI..."):
            prompt = f"""
            I have the following resume:\n\n{resume_input}\n\n
            Please improve and tailor it for a job titled '{job_title}'.
            Make it professional, keyword-optimized, and ATS-friendly.
            """

            headers = {
                "Authorization": "Bearer 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",
                "Content-Type": "application/json"
            }

            data = {
                "model": "mistral:instruct",
                "messages": [{"role": "user", "content": prompt}]
            }

            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
                response.raise_for_status()
                enhanced_resume = response.json()["choices"][0]["message"]["content"]
                st.success("✅ Resume enhanced successfully!")
                st.text_area("💡 Enhanced Resume:", value=enhanced_resume, height=400)
            except Exception as e:
                st.error(f"❌ Error: {e}")

import streamlit as st
import requests

def generate_image(prompt, openai_api_key):
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        json={
            "model": "dall-e-3",
            "prompt": prompt,
            "size": "1024x1024",
            "quality": "standard",
            "n": 1,
        },
        headers={
            "Authorization": f"Bearer {openai_api_key}",
        },
    )
    response.raise_for_status()
    return response.json().get("data", [{}])[0].get("url", "")

st.title("Text to Image using DALL-E 3")

# Add a sidebar
with st.sidebar:
    st.subheader("Settings")
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

prompt = st.text_input("Enter a description to generate an image")

if st.button("Generate Image"):
    if prompt and openai_api_key:
        image_url = generate_image(prompt, openai_api_key)
        if image_url:
            st.image(image_url, use_column_width=True)
        else:
            st.warning("Failed to generate image. Please try again.")
    else:
        st.warning("Please enter a description and your OpenAI API Key.")

# Profile footer HTML for sidebar
sidebar_footer_html = """
<div style="text-align: left;">
    <p style="font-size: 16px;"><b>Author: 🌟 Rizwan Rizwan 🌟</b></p>
    <a href="https://github.com/Rizwankaka"><img src="https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github" alt="GitHub"/></a><br>
    <a href="https://www.linkedin.com/in/rizwan-rizwan-1351a650/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a><br>
    <a href="https://twitter.com/RizwanRizwan_"><img src="https://img.shields.io/badge/Twitter-Profile-blue?style=for-the-badge&logo=twitter" alt="Twitter"/></a><br>
    <a href="https://www.facebook.com/RIZWANNAZEEER"><img src="https://img.shields.io/badge/Facebook-Profile-blue?style=for-the-badge&logo=facebook" alt="Facebook"/></a><br>
    <a href="mailto:riwan.rewala@gmail.com"><img src="https://img.shields.io/badge/Gmail-Contact%20Me-red?style=for-the-badge&logo=gmail" alt="Gmail"/></a>
</div>
"""

# Render profile footer in sidebar at the "bottom"
st.sidebar.markdown(sidebar_footer_html, unsafe_allow_html=True)
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/6847584/pexels-photo-6847584.jpeg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://images.pexels.com/photos/6101958/pexels-photo-6101958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""

# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p>Credit: Dr. Aammar Tufail | Phd | Data Scientist | Bioinformatician (<a href="https://www.youtube.com/@Codanics" target="_blank">CODANICS</a>)</p>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)
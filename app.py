import streamlit as st
from PIL import Image
from image_desc import generate_image_caption
from caption_generator import generate_captions
from hashtag import suggest_hashtags

st.set_page_config(page_title="Instagram Caption Assistant", layout="centered", page_icon="📸")

st.markdown("""
    <style>
    body, .main {
        background-color: #1e1e2f;
        color: #f1f1f1;
    }
    .stApp {
        background-color: #1e1e2f;
    }
    .stMarkdown h1 {
        font-size: 38px !important;
        text-align: center;
        color: #f8f8f2;
        margin-bottom: 0;
    }
    .stMarkdown h2, .stMarkdown h3 {
        color: #ffb86c;
    }
    label[data-testid="stFileUploaderLabel"] {
        font-size: 22px !important;
        font-weight: 600;
        color: #f1f1f1 !important;
    }
    .generated-captions span {
        font-size: 20px;
        color: #ffffff;
        background: #3a3a4f;
        padding: 10px;
        border-radius: 8px;
        display: block;
    }
    .stTextInput, .stTextArea {
        font-size: 18px !important;
    }
    div.stButton > button:first-child {
        background-color: #3d3d5c;
        color: #ffffff;
        border: 1px solid transparent;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 600;
        transition: color 0.3s ease, border 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        color: red;
        border: 1px solid red;
        background-color: #3d3d5c;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📸 Instagram Caption Generator")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)


    if st.button("Generate Captions and Hashtags"):
        with st.spinner("Analyzing image and generating captions..."):
            image_desc = generate_image_caption(image)
            captions = generate_captions(image_desc)
            hashtags = suggest_hashtags(image_desc)

        st.subheader("📝 Auto-generated Description")
        st.write(f"<div style='color:#f1f1f1;font-size:18px;'>{image_desc}</div>", unsafe_allow_html=True)

        st.subheader("✨ Captions")
        for i, cap in enumerate(captions, 1):
            st.markdown(f'<div class="generated-captions" style="margin-bottom: 20px;"><span>{i}. {cap}</span></div>', unsafe_allow_html=True)

        st.subheader("🔥 Hashtags")
        st.markdown(f'<div style="font-size: 18px; color: #50fa7b;">{" ".join(hashtags)}</div>', unsafe_allow_html=True)

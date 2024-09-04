from PIL import Image
import streamlit as st
import base64

def load_image(image_file):
    """Convert image to Base64"""
    try:
        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()
        return encoded_string
    except FileNotFoundError:
        st.error(f"File not found: {image_file}")
        return ""

st.set_page_config(page_title="Personal Portfolio", page_icon=":star:", layout="wide")

background_image_path = "mountains.png"  
background_image_base64 = load_image(background_image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{background_image_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4 = st.tabs(["Home", "About Me", "Hobbies", "Skills"])

with tab1:
    col1, col2 = st.columns([1, 1])
    st.balloons()
    with col1:
        
        st.markdown(
            """
            <div>
            <h1 style='color: #DAE2EB'>WELCOME TO MY PORTFOLIO!</h1>
            <h1 style='color: #DAE2EB'>I'm John Rodolph Bacalso</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        try:
            img = Image.open("jr.jpg")
            img = img.resize((500, 500))
            st.image(img, use_column_width=False)
        except FileNotFoundError:
            st.error("Image 'jr.jpg' not found.")

with tab2:
    st.balloons()
    st.markdown(
        """
        <div style="text-align: center; padding: 20px; background-color: rgba(240, 240, 240, 0.8);">
            <h1 style="color: #000000;">About Me</h1>
            <h3 style="color: #000000;">I'm a 4th-year IT student at Cebu Institute of Technology, living in Talisay City, Cebu. I love technology and aim to work as a software developer or tech support.</h3>
            <h3 style="color: #000000;">I have experience in coding with JavaScript, React, C++, and more. I am eager to expand my knowledge in web development, web design, and game development.</h3>
            <h3 style="color: #000000;">I’m passionate about using my skills to create exciting new tech and am always ready to take on challenges and learn new things. To keep improving, I regularly take online courses.</h3>
            <div style="margin-top: 20px;">
                <a href="https://github.com/johnrodolph" target="_blank">
                    <img src="https://img.icons8.com/ios/50/000000/github.png" alt="GitHub" style="margin: 0 10px;" />
                </a>
                <a href="mailto:johnradbacalso@gmail.com" target="_blank">
                    <img src="https://img.icons8.com/ios/50/000000/gmail.png" alt="Gmail" style="margin: 0 10px;" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tab3:
    st.balloons()
  
    st.markdown(
        """
        
        <div style="text-align: center; padding: 20px; background-color: rgba(240, 240, 240, 0.8);">
        <h1 style="color: #000000;">Hobbies</h1>
        <h3 style="color: #000000;">🏀 Enjoy playing sports like basketball and volleyball.</h1>
        <h3 style="color: #000000;">🎮 Passionate about online gaming.</h1>
        <h3 style="color: #000000;">🎨 Love drawing anime characters in my spare time.</h1>
        <h3 style="color: #000000;">💻 Dedicate some of my free time to practicing new programming languages.</h1>
    
    
    </div>
        """,
        unsafe_allow_html=True
    )
  
with tab4:
    st.snow()
    st.markdown(
        """
            <h1 style="color: #DAE2EB;">SKILLS</h1>
            <h3 style="color: #DAE2EB;">Here’s a breakdown of my expertise in various programming languages and tools:</h3>
            
        """,
        unsafe_allow_html=True
    )


    skills = {
        "HTML": 75,
        "JavaScript": 72,
        "C++": 90,
        "MySQL": 80,
        "React": 60,
        "Python": 70
    }

    for skill, percentage in skills.items():
        st.markdown(f"<h2 style='color: #DAE2EB'>{skill}</h2>", unsafe_allow_html=True)
        st.progress(percentage)
        st.markdown(f"<h4 style='color: #DAE2EB'>{percentage}%</h4>", unsafe_allow_html=True)
        
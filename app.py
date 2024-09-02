from PIL import Image
import streamlit as st

# Set page configuration with dark theme
st.set_page_config(page_title="Personal Portfolio", page_icon=":star:", layout="wide")

# Create tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(["Home", "About Me", "Hobbies", "Skills"])

# Define the content for each tab
with tab1:
    # Create a two-column layout
    col1, col2 = st.columns([1, 1])  # Adjust the ratio as needed
    st.balloons()
    with col1:
          
        st.write('''
               # WELCOME TO MY PORTFOLIO!
            ''')  
        st.markdown(
        """
        <div>
        <h1>John Rodolph Bacalso</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
 
    with col2:
      # Open the image file
        img = Image.open("jr.jpg")
        # Resize the image
        img = img.resize((500, 500))
        # Display the resized image
        st.image(img, use_column_width=False)

with tab2:
     st.balloons()
     st.markdown(
        """
        <div style="text-align: center; padding: 20px; background-color: #f0f0f0;">
            <h1 style="color: #333;">About Me</h1>
            <h3 style="color: #666;">I'm a 4th-year IT student at Cebu Institute of Technology, living in Talisay City, Cebu. I love technology</h3>
            <h3 style="color: #666;">and want to work as a software developer or tech support. I've learned a lot about coding in JavaScript,</h3>
            <h3 style="color: #666;">React,C++ and more.</h3>
            <h3 style="color: #666;">I also want to learn more about web development, web designing, and Game Development . I want to use my</h3>
            <h3 style="color: #666;">skills to help create new and exciting tech. I’m always eager to learn new things and take on challenges.</h3>
            <h3 style="color: #666;">I also take online courses to keep learning and improving.</h3>
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
    st.title("Hobbies")
    items = ["I play sports such as Basketball and Volleyball", "I also love playing Online Games", "Draw anime characters ", "I also spend my free time practing new programming languages"]
    markdown_text = "\n".join([f"- {item}" for item in items])
    st.markdown(markdown_text)


with tab4:
    st.snow()
    st.title("Skills")
    
    # Define skill names and their percentages
    skills = {
        "HTML": 75,
        "JavaScript": 72,
        "C++": 90,
        "MySQL": 80,
        "React": 60,
        "Python": 70
    }
    
    # Display each skill with a progress bar
    for skill, percentage in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(percentage)
        st.markdown(f"{percentage}%")
        st.markdown("---")

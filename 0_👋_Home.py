import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Santiago Jerez Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** Santiago Jerez")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Santiago Jerez</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "Foto cv.jpeg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Passionate about data analysis and with a solid background in Business Administration and Management, I have dedicated my career to exploring the world of Big Data and Data Analytics. I have pursued my career and my current Master's in Big Data and Data Analytics in English, which has provided me with a high level of competence in this language, essential in the global business and technology field."   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a Data Analyst with a strategic profile

- 🛩️ Previous experience: Data Analys intern in Heretat Oller del Mas and final grade project focused on Data Analytics

- ❤️ Data Science, Statistics, Programming, Investing and Managing

- 🤖 Bot for identifying current real estate opportunities in Barcelona and Madrid

- 🏂 Investing in the stock market, crypto market, program tools, manage an online store

- 📫 How to reach me: SantiJC21101@gmail.com

- 💼 Linkedin URL: https://www.linkedin.com/in/santiago-jerez-castro/

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.

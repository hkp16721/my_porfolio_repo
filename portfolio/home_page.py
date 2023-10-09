import streamlit as st
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu

# Setting page
st.set_page_config(
    page_title="Hemant's Portfolio",
    layout="wide",
    # initial_sidebar_state="expanded",

)
about_me = """<b><u>About Me</u></b>

Hello, I'm Hemant, and I'm passionate about leveraging my diverse skill set to excel in a Software Development Engineer (SDE) role. With a deep-rooted proficiency in Python, GUI development, web technologies (HTML, CSS, JavaScript), and database management (Oracle SQL and PostgreSQL), I bring a comprehensive skill set to the table.

<b><u>Technical Expertise</u></b>
- *Python:* I have a profound understanding of Python and have successfully applied it in various domains. Whether it's scripting, automation, or building complex applications, Python is my go-to language.

- *GUI Development:* My experience extends to creating intuitive graphical user interfaces (GUIs) using libraries like Tkinter, streamlining user interactions and enhancing the overall user experience.

- *Web Technologies:* I am well-versed in HTML, CSS, and JavaScript, allowing me to develop responsive and dynamic web applications.

- *Database Management:* My proficiency in both Oracle SQL and PostgreSQL ensures that I can design efficient database systems, optimize queries, and manage data effectively.

- *Automation:* I have a deep knowledge of automation frameworks like Selenium, which I have used to streamline testing processes, saving time and resources.

- *Dashboard Creation:* I have expertise in creating insightful and interactive dashboards using tools like Quicksight and Google Data Studio, helping businesses make data-driven decisions with ease.

- *Other Technologies:* I am also experienced in technologies like PySimpleGui and streamlit, enabling me to develop versatile and user-friendly applications.
"""
image = Image.open("hemant.jpg")

# option menu
selected = option_menu(
    menu_title=None,
    options=["Home","About Me","Work Ex", "Projects", "Achievements", "Contact"],
    icons=["house","person","building", "folder", "trophy", "phone"],
    orientation="horizontal",
    styles=""""""

)

# Styling
st.markdown(
    """<style>
    img{
    border-radius:10%;
    border:0.5px solid red;
    width :100%;
    }
    .st-emotion-cache-7ym5gk{
    background:#10294a;
    color:white;
    border:0.5px solid red;
    }
    div.st-emotion-cache-1wf8rl4:nth-child(1) > div:nth-child(1){
    background:#2c3e50;
    }
    div.st-emotion-cache-meqk23:nth-child(1) > div:nth-child(1){
    background:#2c3e50;
    }
    .main{
    background:#2c3e50;
    }
    body{
    background-color:#2c3e50;
    }
    div.element-container:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1){

    border:2px solid red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

left_columns, right_columns = st.columns([0.2, 0.8], gap='small')

# Selecting Home
if selected == "About Me":
    # """Personal Details"""
    with left_columns:
        file = open("Resume (2).pdf", "rb")
        st.image(image)
        st.markdown(""":white[<b><u>HEMANT KUMAR</u></b><br>‍💻Business Analyst and SSA Tool Developer
        <br>🏢AMAZON DEVELOPMENT CENTER
        <br>📱 +917989230543<br>
        🏙️Bangalore]""",
                    unsafe_allow_html=True)
        st.download_button("Download CV", data=file, file_name="Hemant's_Resume.pdf")
    with right_columns:
        st.markdown(f"""<p><i>{about_me}</p><br><br>
                """, unsafe_allow_html=True)


if selected == "Projects":
    "On the way"

if selected == "Achievements":
    st.markdown("""<b><u>Achievements</u></b>

At Amazon, I received the prestigious Eureka and Beyond award for developing an automation tool that revolutionized the workflow. This tool had a profound impact on the business, reducing manpower requirements from 50 to just 1 while maintaining 100% accuracy. My ability to innovate and create efficient solutions is a testament to my commitment to excellence.

Furthermore, I am a certified FLM manager, showcasing my leadership and management capabilities.

<b><u>Beyond Work</u></b>

In my student days, I excelled in sports and extracurricular activities. I played at the national level in both basketball and handball, demonstrating my dedication, teamwork, and competitive spirit. I also attended the Asia-level scout competition, Jamboori, where I cleared with an A+ grade. Additionally, I hold an A+ certification in National Adventure Training by Bharat Scout, underscoring my commitment to personal development and adventure.

I am excited to bring my technical expertise, problem-solving abilities, and dedication to excellence to a dynamic and forward-thinking team. My diverse background and achievements in both technology and extracurricular activities have equipped me with a unique perspective and skill set that I am eager to apply to new challenges. Let's connect and explore how I can contribute to your organization's success.
""",
                unsafe_allow_html=True)

if selected == "Work Ex":
        left, right = st.columns([40, 60])
        work_history = {
            "Company": ["Cynosure", "Wipro", "Wipro", "Amazon"],
            "Job Role": ["Guidwire Intern", "T&S Associate", "Team Leader", "BA SSA"],
            "Year": ["(Aug-Nov)2017", "(Dec_2017-April_2019)", "(April_2019-May_2021)",
                     "(June-2021-Currently Working)"],
        }

        experties = {
            "Technology" : ["Python", "TKinter", "PySimpleGui","Streamlit","Oracle Sql", "HTML", "CSS", "JS"],
            "Rate My Skill" : ["🌟🌟🌟🌟","🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟","🌟🌟🌟","🌟🌟🌟","🌟🌟🌟","🌟🌟🌟"],
            "Rated out of" : ["🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟","🌟🌟🌟🌟🌟"]
        }
        with left:
            """Work Experience"""
            df_wrkex = pd.DataFrame(work_history)
            st.dataframe(df_wrkex, use_container_width=True, height=320)
        with right:
            """Technology Expertise Rating"""
            df_experties = pd.DataFrame(experties)
            st.dataframe(df_experties, use_container_width=True)


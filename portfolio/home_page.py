from time import sleep

import numpy as np
import streamlit as st
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu
import smtplib

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
    options=["Home", "About Me", "Work Ex", "Projects", "Achievements", "Contact"],
    icons=["house", "person", "building", "folder", "trophy", "phone"],
    orientation="horizontal",
    styles=""""""

)

# Styling
st.markdown(
    """<style>
    img{
    border-radius:2%;
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

# link_din = Image.open("linkedin-logo-png-1837.png")
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
    "GUI Projects"
    c1 = st.container()
    c2 = st.container()
    c3 = st.container()
    c4 = st.container()
    p1 = Image.open("P1.png")
    p2 = Image.open("P2.png")
    p3 = Image.open("P3.png")
    with c1:
        with c1.expander("D EXTRACTER"):
            "GUI Tool, Functionality and Package used"
            lft, rgt = st.columns([.5, .5], gap="small")
            with lft:
                st.image(p1)
            with rgt:
                st.code(body=f"""
    import ctypes
    import datetime
    import os
    import random
    from tkinter import *
    from tkinter import filedialog
    from tkinter import ttk
    import customtkinter
    import pandas as pd
    from CTkMessagebox import CTkMessagebox
    from tkcalendar import Calendar
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.firefox.service import Service
    from shareplum import Site
    from requests_negotiate_sspi import HttpNegotiateAuth
    'This tool uses selenium to extract data , pandas and GUI to perform analysis and display the data.'""", language="python")
    with c2:
        with c2.expander("OUTREACH"):
            "Project is based on 'eel' to communicate between python backend and 'HTML,CSS and JS based UI'"
            lft1, rgt1 = st.columns([.5, .5], gap="small")
            with lft1:
                st.code(body="""
import eel
from os import getlogin
import win32api
import win32net
from PySimpleGUI import popup_get_file
import datetime
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from time import sleep
from openpyxl import load_workbook
import pandas as pd""", language="python")
            with rgt1:
                st.image(p2)
    with c3:
        with st.expander("Portfolio"):
            "Project is based on Streamlit, HTML and CSS"
            lft2, rgt2 = st.columns([.5, .5], gap="small")
            with lft2:
                st.image(p3)
            with rgt2:
                st.code("""
from time import sleep
import numpy as np
import streamlit as st
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu               
                """, language='python')
    # with c4:
    #     lft3, rgt3 = c1.columns([.5, .5], gap="small")

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
        "Technology": ["Python", "TKinter", "PySimpleGui", "Streamlit", "Oracle Sql", "HTML", "CSS", "JS"],
        "Rate My Skill": ["🌟🌟🌟🌟", "🌟🌟🌟🌟", "🌟🌟🌟🌟🌟", "🌟🌟🌟", "🌟🌟🌟", "🌟🌟🌟", "🌟🌟🌟", "🌟🌟🌟"],
        "Rated out of": ["🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟",
                         "🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"]
    }
    with left:
        """Work Experience"""
        df_wrkex = pd.DataFrame(work_history)
        st.dataframe(df_wrkex, use_container_width=True, height=320)
    with right:
        """Technology Expertise Rating"""
        df_experties = pd.DataFrame(experties)
        st.dataframe(df_experties, use_container_width=True)

if selected == "Contact":
    "Feel free to reach out to me by filling below form :"
    rt, md, lft = st.columns([20, 60, 20], gap='small')


    def validate():
        d_list = [f_name, l_name, email]
        print(d_list)


    with md:
        with st.form(key="form", clear_on_submit=True):
            f_name = st.text_input("First Name", type="default")
            l_name = st.text_input("Last Name", type="default")
            email = st.text_input("Email", type="default")
            body = st.text_area("Request/Feedback if any")
            submitted = st.form_submit_button("Submit", on_click=validate)
            if submitted:
                d_list = [f_name, l_name, email]
                if ["", "", ""] != d_list:
                    st.success("Request Submited :thumbsup:")
                else:
                    st.error(":thumbsdown: Hey Anonymous, Provide some detail boss :smile: ")

if selected == 'Home':
    # name = 'Hi, I am Hemant Kumar'
    # a,b,c,d,e = st.columns([.02,.02,.02,.02,.02], gap='small')
    # for item, cont in zip('Hi, I am Hemant Kumar'.split(), [a,b,c,d,e]):
    #     cont.title(item)
    #     sleep(0.5)
    progress_bar = st.progress(0)
    status_text = st.empty()
    chart = st.line_chart(np.random.randn(10, 2))

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)

        new_rows = np.random.randn(10, 2)

        # Update status text.
        status_text.text(
            'The latest random number is: %s' % new_rows[-1, 1])

        # Append data to the chart.
        chart.add_rows(new_rows)

        # Pretend we're doing some computation that takes time.
        sleep(0.1)

    status_text.text('Done!')
    chart = st.title("Hi, I am Hemant Kumar")
    st.balloons()

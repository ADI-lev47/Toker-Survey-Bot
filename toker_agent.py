import os
import time
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
import streamlit as st
# מפתחות (תוודאי שהם מודבקים כאן)
os.environ["SERPER_API_KEY"] = st.secrets ["SERPER_API_KEY"]
os.environ["OPENAI_API_KEY"] = st.secrets ["OPENAI_API_KEY"]

# 1. הגדרת הצוות (RAG + כתיבה)
search_tool = SerperDevTool()

researcher = Agent(
role='חוקר אקטואליה',
goal='למצוא ידיעה חמה מה-24 שעות האחרונות במגזר החרדי',
backstory='עיתונאי שסורק אתרים מגזריים למידע עדכני.',
tools=[search_tool],
verbose=True
)

writer = Agent(
role='קופירייטר',
goal='לנסח סקר ויראלי לוואטסאפ',
backstory='מומחה לניסוח סקרים משעשעים בסגנון של מנחם טוקר.',
verbose=True
)

# 3. הגדרת המשימות (עם expected_output כדי למנוע את השגיאה)
task1 = Task(
description='חפש נושא אקטואלי חם מהיום במגזר החרדי.',
expected_output='סיכום קצר של הידיעה החדשותית שמצאת.',
agent=researcher
)

task2 = Task(
description='נסח סקר ויראלי מוכן לשליחה לוואטסאפ. בסוף ההודעה תוסיף את המשפט: "לעוד סקר בלחיצת כפתור: [https://toker-survey-bot-bwxhj2s2zrxzfnvlgdmsk7.streamlit.app/]"',
expected_output='הודעה סופית לוואטסאפ שכוללת שאלה ו-5 אפשרויות.',
agent=writer
)

# 2. הרצת ה-AI
crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
result = str(crew.kickoff())

# 3. שלב השליחה (כאן הקסם קורה)
print("\n" + "="*30)
print("הסקר מוכן! ממתין 15 שניות...")
print("עברי עכשיו לוואטסאפ, כנסי לצ'אט ולוודא שהסמן מהבהב בתיבת הטקסט!")
print("="*30)

time.sleep(15)


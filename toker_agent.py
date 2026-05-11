import os
import time
import pyautogui
import pyperclip
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# מפתחות (תוודאי שהם מודבקים כאן)
os.environ["SERPER_API_KEY"] = "1f61d2caeedc52bec794e98ae819f238b33920b6"
os.environ["OPENAI_API_KEY"] = "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"


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
description='נסח סקר ויראלי מוכן לשליחה לוואטסאפ. בסוף ההודעה תוסיף את המשפט: "לעוד סקר בלחיצת כפתור: [כאן יבוא הלינק]"',
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

# העתקה והדבקה לתוך החלון הקיים
pyperclip.copy(result)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')

print("בוצע!")

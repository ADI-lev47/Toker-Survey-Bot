import os
import time
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
import pyautogui
import pyperclip
from dotenv import load_dotenv   

load_dotenv(dotenv_path=".env")
load_dotenv(dotenv_path="env")

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY", "")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# בדיקה אם המפתחות ריקים
if not os.environ["SERPER_API_KEY"] or not os.environ["OPENAI_API_KEY"]:
 print("❌ שגיאה: המפתחות לא נטענו! ודאי שקובץ ה-env מכיל את המפתחות הנכונים.")
 exit()

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

task1 = Task(
    description='חפש נושא אקטואלי חם מהיום במגזר החרדי.',
    expected_output='סיכום קצר של הידיעה החדשותית שמצאת.',
    agent=researcher
)

task2 = Task(
    description='נסח סקר ויראלי מוכן לשליחה לוואטסאפ. בסוף ההודעה תוסיף את המשפט: "לעוד סקר בלחיצת כפתור: [https://toker-survey-bot-2gupxpbtnc52as8ds5ecgn.streamlit.app/]"',
    expected_output='הודעה סופית לוואטסאפ שכוללת שאלה ו-5 אפשרויות.',
    agent=writer
)

def run_whatsapp_bot():
    crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
    result = str(crew.kickoff())

    print("\n" + "="*30)
    print("הסקר מוכן! ממתין 15 שניות...")
    print("עברי לוואטסאפ וודאי שהסמן מהבהב בתיבת הטקסט!")
    print("="*30)

    time.sleep(15)
     
    pyperclip.copy(result) 
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    print("✅ הסקר נשלח בהצלחה!")

if __name__ == "__main__":
    run_whatsapp_bot()

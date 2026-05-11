import streamlit as st
import os

st.set_page_config(page_title="מחולל הסקרים של טוקר", page_icon="🎙️")

st.title("🎙️ המערכת של טוקר: יצירת סקרים באיי")
st.write("לחץ על הכפתור כדי להפעיל את צוות הסוכנים ולשלוח סקר חדש לוואטסאפ.")

if st.button("🚀 צור סקר עכשיו"):
 with st.spinner("הסוכנים חוקרים וכותבים..."):
 # הפקודה הזו מריצה את הקוד הקיים שלך (toker_agent.py)
  os.system("python toker_agent.py")
  st.success("הסקר נוצר ונשלח לוואטסאפ!")
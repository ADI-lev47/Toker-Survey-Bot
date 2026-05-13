import streamlit as st
from openai import OpenAI

# הגדרת דף
st.set_page_config(page_title="מחולל הסקרים של אדי", page_icon="📝")

st.title("📝 מחולל הסקרים של טוקר")
st.write("רוצים סקר חדש ומעניין? לחצו על הכפתור למטה!")

# שימוש במפתח מה-Secrets של Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if st.button("ייצרו לי סקר חדש עכשיו! 🚀"):
    with st.spinner("הסוכנים של אדי חושבים על רעיון..."):
        # קריאה ישירה ל-OpenAI (במקום CrewAI הכבד)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "כתוב סקר ויראלי קצר ומצחיק לוואטסאפ בנושא אקטואליה חרדית, כולל 5 אפשרויות בחירה ואמוג'ים."}]
        )
        survey_text = response.choices[0].message.content
        
        st.success("הסקר מוכן!")
        st.text_area("הסקר שלך:", value=survey_text, height=200)
        
        # כפתור שיתוף בוואטסאפ
        whatsapp_url = f"https://wa.me/?text={survey_text}"
        st.markdown(f'[הפצת הסקר בוואטסאפ 📱]({whatsapp_url})')
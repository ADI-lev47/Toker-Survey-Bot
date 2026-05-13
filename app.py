__import__('pydantic').v1.models.BaseModel.model_rebuild = lambda *args, **kwargs: None
import streamlit as st
import streamlit as st
from toker_agent import run_crew
import urllib.parse

st.title("🤖 מחולל הסקרים של אדי")
st.write("לחצי על הכפתור כדי ליצור סקר ויראלי חדש!")

if st.button("🚀 צור סקר עכשיו"):
    with st.spinner("הסוכנים חוקרים וכותבים..."):
        # הרצת הסוכנים
        result = run_crew()

        if result:
            st.success("✅ הסקר נוצר בהצלחה!")
            # הצגת הטקסט של הסקר על המסך
            st.text_area("הסקר שלך:", value=result, height=300)

            # יצירת לינק לוואטסאפ (URL Encoding)
            encoded_text = urllib.parse.quote(str(result))
            whatsapp_url = f"https://wa.me/?text={encoded_text}"
            
            # הצגת כפתור שליחה ירוק ומעוצב
            st.markdown(f'''
                <a href="{whatsapp_url}" target="_blank">
                    <button style="
                        background-color: #25D366;
                        color: white;
                        padding: 15px 32px;
                        text-align: center;
                        font-size: 18px;
                        font-weight: bold;
                        margin: 10px 0;
                        border: none;
                        border-radius: 10px;
                        cursor: pointer;
                        width: 100%;
                        display: block;
                    ">
                        📱 שלח עכשיו לוואטסאפ
                    </button>
                </a>
            ''', unsafe_allow_html=True)

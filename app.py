import streamlit as st

st.set_page_config(page_title="Emotion Detection", page_icon="😊")
st.title("😊 AI Emotion Detection by Text")
st.write("Mee Final Year Project")

def check_emotion(t):
    t = t.lower()
    if any(w in t for w in ["happy", "good", "love", "great", "awesome", "santhosham", "bagundi", "super"]):
        return "😊 Happy / Santhosham", "success"
    if any(w in t for w in ["sad", "bad", "cry", "badha", "dukham", "boring"]):
        return "😢 Sad / Badha", "warning"
    if any(w in t for w in ["angry", "mad", "kopam", "chiraku"]):
        return "😠 Angry / Kopam", "error"
    return "😐 Normal / Neutral", "info"

user_text = st.text_area("Mee text ikkada rayandi:", placeholder="Ex: I am very happy today")

if st.button("Emotion Check Cheyyi 🔍"):
    if user_text:
        emo, typ = check_emotion(user_text)
        if typ == "success":
            st.success(f"Result: {emo}")
            st.balloons()
        elif typ == "warning":
            st.warning(f"Result: {emo}")
        elif typ == "error":
            st.error(f"Result: {emo}")
        else:
            st.info(f"Result: {emo}")
    else:
        st.warning("First text type cheyyi!")

st.sidebar.success("✅ Project Ready")
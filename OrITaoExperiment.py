import streamlit as st
import gettext

localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

st.title(_("Cavendish-Experiment"))

st.video("images/Cavendish.mp4")


import streamlit as st
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_evol = _('''                                                                                                                                                                                
The ten thousand things carry yin and embrace yang. (Tao Te Ching 道德經 42)

'''
)

de_evol = _('''                                                                                                                                                                                
Die zehntausend Dinge tragen das Yin und umfangen das Yang. (Tao Te Ching 道德經 42)

'''
)

ru_evol = _('''                                                                                                                                                                                
Десять тысяч вещей несут в себе инь и объемлют ян. (Дао Дэ Цзин 道德經 42)

'''
)

evol = {"en":en_evol, "de":de_evol, "ru":ru_evol, }

st.title(_("Evolution"))

st.write(evol[st.session_state.itaolang])





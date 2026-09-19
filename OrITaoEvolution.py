
import streamlit as st
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_evol = _('''                                                                                                                                                                                
42 The ten thousand things carry yin and embrace yang.

'''
)

de_evol = _('''                                                                                                                                                                                
42 Die zehntausend Dinge tragen das Yin und umfangen das Yang.

'''
)

ru_evol = _('''                                                                                                                                                                                
42 Десять тысяч вещей несут в себе инь и объемлют ян.

'''
)

evol = {"en":en_evol, "de":de_evol, "ru":ru_evol, }

st.title(_("Evolution"))

st.write(evol[st.session_state.itaolang])






import streamlit as st
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_invol = _('''                                                                                                                                                                                
42 The Tao begot One.
One begot Two.
Two begot Three.
And Three begot the ten thousand things.

'''
)

de_invol = _('''                                                                                                                                                                                
42 Das Tao brachte das Eine hervor.
Das Eine brachte das Zwei hervor.
Das Zwei brachte das Drei hervor.
Und das Drei brachte die zehntausend Dinge hervor.

'''
)

ru_invol = _('''                                                                                                                                                                                
42 Тао породило Одно.
Одно породило Два.
Два породило Три.
А Три породило десять тысяч вещей.

'''
)

invol = {"en":en_invol, "de":de_invol, "ru":ru_invol, }

st.title(_("Involution"))

st.write(invol[st.session_state.itaolang])





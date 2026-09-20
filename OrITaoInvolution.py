
import streamlit as st
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_invol = _('''                                                                                                                                                                                
The Tao begot One.
One begot Two.
Two begot Three.
And Three begot the ten thousand things. (Tao Te Ching 道德經 42)

'''
)

de_invol = _('''                                                                                                                                                                                
Das Tao brachte das Eine hervor.
Das Eine brachte das Zwei hervor.
Das Zwei brachte das Drei hervor.
Und das Drei brachte die zehntausend Dinge hervor. (Tao Te Ching 道德經 42)

'''
)

ru_invol = _('''                                                                                                                                                                                
Тао породило Одно.
Одно породило Два.
Два породило Три.
А Три породило десять тысяч вещей. (Дао Дэ Цзин 道德經 42)

'''
)

invol = {"en":en_invol, "de":de_invol, "ru":ru_invol, }

st.title(_("Involution"))

st.write(invol[st.session_state.itaolang])





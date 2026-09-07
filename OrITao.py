
import streamlit as st
#from streamlit_image_coordinates import streamlit_image_coordinates
import gettext

localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 



en_itao = _('''

'''
)

de_itao = _('''

'''
)
 

ru_itao = _('''

'''
)

itao = {"en":en_itao, "de":de_itao, "ru":ru_itao, }

st.title("☯ iTao ")
#st.title("☯ iTao " + _("I am Tao"))

    
if __name__=='__main__':
    tab1, tab2 = st.tabs([_("World structure"), _("Involution"),])
    with tab1:
        st.write(itao[st.session_state.itaolang])
    with tab2:
        st.image("images/tao.png")




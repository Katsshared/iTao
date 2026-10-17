'''

# create .mo
msgfmt -o locales/en/LC_MESSAGES/messages.mo locales/en/LC_MESSAGES/messages.po
msgfmt -o locales/de/LC_MESSAGES/messages.mo locales/de/LC_MESSAGES/messages.po
msgfmt -o locales/ru/LC_MESSAGES/messages.mo locales/ru/LC_MESSAGES/messages.po
# update .po ASCII - UTF-8
msgmerge -U locales/en/LC_MESSAGES/messages.po locales/messages.pot
msgmerge -U locales/de/LC_MESSAGES/messages.po locales/messages.pot
msgmerge -U locales/ru/LC_MESSAGES/messages.po locales/messages.pot
#create .po
msginit -l en_EN.UTF8 -o locales/en/LC_MESSAGES/messages.po -i locales/messages.pot --no-translator
msginit -l de_DE.UTF8 -o locales/de/LC_MESSAGES/messages.po -i locales/messages.pot --no-translator
msginit -l ru_RU.UTF8 -o locales/ru/LC_MESSAGES/messages.po -i locales/messages.pot --no-translator

#generate .pot
xgettext -d messages -o locales/messages.pot OrITaoMain.py --from-code UTF-8

#setup gettext
https://gnuwin32.sourceforge.net/packages/gettext.htm
sudo apt install gettext

cd /home/cat/eclipse-workspace/Orientaion/ITAO/
streamlit run /home/cat/eclipse-workspace/Orientaion/ITAO/OrITaoMain.py

'''

import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import gettext

import glob
import os

langs = ['en ' + "🇬🇧", 'de ' + "🇩🇪", 'ru ' + "🇷🇺",]

with st.sidebar:
    lang_sel = st.selectbox(label=" ", options=langs, key="iTaoMain", index=0)

st.session_state.itaolang = lang_sel[0:2]
    
localizator = gettext.translation('messages', localedir='locales', languages=[lang_sel[0:2]])    
localizator.install() 
_ = localizator.gettext 

#st.write("道")

if "PQRSTfig" not in st.session_state:
    st.session_state.PQRSTfig = "fig.png"

@st.dialog("道 iTao", dismissible=True, on_dismiss="rerun")
def on_tao():
#    st.image("images/TaoChina.png")
    st.header("🇨🇳" + " 我是道")
    st.header("🇬🇧" + " I am Tao") 
    st.header("🇩🇪" + " Ich bin Tao")
    st.header("🇷🇺" + " Я есть Тао")

with st.sidebar:
    streamlit_image_coordinates(source="images/TaoChina.png", on_click=on_tao)    

FIGPNGDIR = "images/"

def listPngs():
    # https://www.pythonmorsels.com/datetime-arithmetic/    
    from datetime import datetime
    from datetime import timedelta
    
    res = glob.glob(FIGPNGDIR + "fig*.png", recursive=False)
    res = sorted(res, reverse=True)

    for file in res:
        c_timestamp = os.path.getctime(file)
        c_datestamp = datetime.fromtimestamp(c_timestamp)
#        minutes = timedelta(minutes=1)
        hours = timedelta(hours=12)
#        days = timedelta(days=7)
        
        if file == "images/fig.png" or file == FIGPNGDIR+st.session_state.PQRSTfig:
            continue
        
        if datetime.now() - hours > c_datestamp:
            os.unlink(file)
#            print("UNLINK", file)          

@st.fragment(run_every=360, parallel=True)
def delFig():
    listPngs()
    
# ☯✉️∞️♾️☯☯️⏳道 🌀 🦿 ♈♉♊♋♌♍♎♏♐♈♒♓        
pg = st.navigation([
    st.Page("OrITao.py", title=_("I am Tao"), icon="☯️"),
    st.Page("OrITaoInvolution.py", title=_("Involution"), icon="🌀"),
    st.Page("OrITaoEvolution.py", title=_("Evolution"), icon="☯"),
    st.Page("OrITaoPath.py", title=_("Path"), icon="❤️"),
    st.Page("OrITaoScience.py", title=_("Science and Reality"), icon="⚛️"),
    st.Page("OrITaoExperiment.py", title=_("Cavendish-Experiment"), icon="⚖️"),
    st.Page("OrITaoEarth.py", title=_("Earth"), icon="🌎"),
    st.Page("OrITaoPQRST.py", title=_("PQRST"), icon="♾️"),
    st.Page("OrITaoLibrary.py", title=_("Library"), icon="📖"),
    st.Page("OrITaoContact.py", title=_("Contact"), icon="✉️"),
])

pg.run()

    
if __name__=='__main__':
    delFig()




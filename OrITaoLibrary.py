'''
Created on 04.09.2026

@author: cat

https://github.com/hreikin/streamlit-uploads-library

https://hreikin-streamlit-uploads-library-home-ar6h9h.streamlit.app/

https://rsarchive.org/Volumes.html


https://docs.kanaries.net/topics/Streamlit
https://docs.kanaries.net/topics/Streamlit/streamlit-upload-file

'''

import streamlit as st
#from streamlit_image_coordinates import streamlit_image_coordinates
import gettext

localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

st.title(_("Library"))

en_books = {
    1:["Kat Salomon Spirit and Consciousness", f"kat-salomon-spirit-and-consciousness_en",],
    2:["Rudolf Steiner About Cabbala", f"RudolfSteinerAboutCabbala_en",],
}
de_books = {    
    1:["Kat Salomon Der Geist und das Bewusstsein", f"kat-salomon-spirit-and-consciousness_de",],
    2:["Rudolf Steiner Über Die Kabbala", f"RudolfSteinerÜberDieKabbala_de",],
    3:["Rudolf Steiner Die Drei Wege Der Einweihung", f"RudolfSteinerDieDreiWegeDerEinweihung_de",],
    4:["Rudolf Steiner, Emil Bock Das Johannes-Evangelium", f"RudolfSteinerEmilBockJohannesEvangelium_de",],
    5:["Rudolf Steiner, Emil Bock Die Offenbarung des Johannes", f"RudolfSteinerEmilBockOffenbarungJohannes_de",],
}
ru_books = {
    1:["Кэт Саломон Дух и Сознание", f"kat-salomon-spirit-and-consciousness_ru",],
    2:["Рудольф Штайнер О Каббале", f"РудольфШтайнерОКаббале_ru",],
    3:["Рудольф Штайнер Три Пути Посвящения", f"РудольфШтайнерТриПутиПосвящения_ru",],
    4:["Рудольф Штайнер, Емиль Бок Евангелие Иоанна", f"РудольфШтайнерЕмильБокЕвангелиеИоанна_ru",],
}

books = {"en":en_books, "de":de_books, "ru":ru_books, }

    
def makeData(label, fname, key):
#    print("MAKE DATA", label, fname, key)
    with open(fname, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
        st.download_button(label=_("💾 " + _("Download") + " " + label), key=key,
                            data=PDFbyte,
                            file_name=fname,
                            mime='application/octet-stream')
    
def renderBook(label, fname, key):
    with st.form("LibForm"+key):
        st.form_submit_button(label=label, on_click=makeData, args=[label, fname, key])
                       
def renderBookCopy(label, fname, key):
    with open(fname, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
        st.download_button(label=_("💾 " + label), key=key,
                            data=PDFbyte,
                            file_name=fname,
                            mime='application/octet-stream')
    
def renderBooks():
    bks = books[st.session_state.itaolang]
    sz = len(bks)
#    print(bks)
    for i in range(1, sz+1):
        key = "lbry_"+str(i) 
        ar = bks[i]
        label = ar[0]
        fname = "books/" + ar[1] + ".pdf"
#        print(label, fname, key)
        renderBook(label, fname, key)

if __name__ == '__main__':
    renderBooks()


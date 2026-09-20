'''

https://laotzu.xyz/chapter/display?id=53
https://www.wussu.com/laotzu/laotzu53.html

'''

import streamlit as st
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_path = _('''                                                                                                                                                                                
Great Tao (Path) is smooth and plain, yet people prefer the devious bypaths. (Tao Te Ching 道德經 53) 

'''
)

de_path = _('''                                                                                                                                                                                
Das große Tao (Pfad) ist eben und schlicht, doch die Menschen bevorzugen die verschlungenen Seitenpfade. (Tao Te Ching 道德經 53)

'''
)

ru_path = _('''                                                                                                                                                                                
 Великий Дао (Путь) ровен и прост, но люди предпочитают окольные пути. (Дао Дэ Цзин 道德經 53)

'''
)

path = {"en":en_path, "de":de_path, "ru":ru_path, }

st.title(_("Path"))

st.write(path[st.session_state.itaolang])





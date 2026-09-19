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
53 Great Tao is smooth and plain, yet people prefer the devious bypaths.

'''
)

de_path = _('''                                                                                                                                                                                
53 Das große Tao ist eben und schlicht, doch die Menschen bevorzugen die verschlungenen Seitenpfade.

'''
)

ru_path = _('''                                                                                                                                                                                
53 Великий Дао ровен и прост, но люди предпочитают окольные тропы.

'''
)

path = {"en":en_path, "de":de_path, "ru":ru_path, }

st.title(_("Path"))



st.write(path[st.session_state.itaolang])





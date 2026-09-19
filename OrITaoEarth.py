import streamlit as st
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_earth = _('''                                                                                                                                                                                
Kepler in The Harmony of the World (Harminices Mundi) describes the Earth as an animated being. To be alive means to have consciousness. The Earth does not attracts objects as unconscious mass, but it acts consciously like man would act when he puts consciously his arm on his forehead. The Earth has consciousness that could be perceived in the rhythmic processes of the Earth. It was announced that the gravitational waves had been registered. What was registered however is a rhythmic process that has period of 36-38 years. 

The life of man in physical body depends on life of the Earth. It is not difficult to notice, that man who returns back to the Earth after visiting the space station, becomes weak, cannot walk without assistance and needs help. A pilot of a jet plane who can experience the same or even much bigger overstress but at much smaller distance from the surface of the Earth does not need such help and is able to walk without assistance immediately after landing. Therefore essential is not the overstress caused by flight but the connection of man to the Earth. It is possible to verify that connection of man to the Earth is inversely related to the distance from the Earth. The distance from the Earth where man in physical body cannot be alive is between seven and twelve radiuses of the Earth. 

There is a general concept that if man can exist in the diving suit under water on the Earth and in the spacesuit at some distance from the Earth it is also possible for man to exist at any distance from the Earth, e.g. on the Moon. Thereby it is ignored, that if one dives under water, one stays on the Earth and preserves the connection to the Earth, and if one moves far enough away from the Earth, one loses the connection to the Earth. All so-called proofs, that man in physical body was on the Moon, can be created without presence of man on the Moon. To reach the distance from the Earth that is less than distance between the Earth and the Moon and which is between seven and twelve radiuses of the Earth would be lethal for man. It is approximately where the geostationary orbit begins. 

The life of man depends on the life of the Earth in such a degree that man in physical body became an inseparable part of the Earth. This means that man in physical body cannot exist without the Earth. The manned spacecraft or spacecraft with higher animals aboard should try to reach the distance from the Earth which is between seven and twelve radiuses of the Earth. It is necessarily to carry out such experiment in order to eliminate wrong concepts of existence and reality. 



The idea of gravitation

It is not possible to explain the interaction of two pairs of masses in Cavendish experiment using an idea of universal gravitation, because this idea does not correspond to the reality. Before conclusions about an existence of gravitation can be drawn, one must try to distinguish to what extent the observed phenomenon is separated from other phenomena and to what extent it forms a part of the whole. In such a way the Solar system must be considered as a whole and the planets as inseparable parts of the Solar system.

It is well known that the Newton’s law of gravitation was derived from the Kepler’s law for the planets of the Solar system. Such derivation and calculation is possible because the Kepler’s law contains the Newton’s law without masses. The Kepler’s law states that the squares of the orbital periods of the planets are proportional to the cubes of the semi-major axles of their orbits (1). 

(1)     t1\*\*2 : t2\*\*2 = r1\*\*3 : r2\*\*3

It is possible to rewrite (1) as (2).

t1\*\*2 / r1  :  t2\*\*2 / r2 = r1\*\*2 : r2\*\*2 

(2)     1 / r1\*\*2  : 1  / r2\*\*2 = r1 / t1\*\*2 : r2 / t2\*\*2

Taking for simplicity the accelerations for circular motion of planets one gets (3).

a = v2 / r

v = 2πr / t

a = 4π2r / t2 

(3)     r1 / t1\*\*2  :  r2 / t2\*\*2 = a1  : a2   

Combining (2) and (3) one gets that accelerations are inversely proportional to the square of distances (4).

(4)     1 / r1\*\*2  : 1 / r2\*\*2 = a1  : a2  

In such a way the Kepler’s law (2) is actually the Newton’s law without masses: accelerations are inversely proportional to the square of distances (4). Using the second Newton’s law one gets the Newton’s law with masses (5). The forces involved in motion of planets are proportional to the masses of planets and inversely proportional to the square of the distances.

f = m a

(5)     m1 / r1\*\*2  : m2  / r2\*\*2 = f1  : f2  

The expression (5) does not mean that any masses attract each other. It means that the planets are moving in compliance with the Kepler’s law (2). If an object falls on a planet it moves in compliance with the motions of the planets, but it does not mean that an object attracts a planet. There is neither such evidence nor evidence that all objects on some planet attract each other. The planets of the Solar system do not exist by themselves they exist only together in combination with other planets of the Solar system. As well as the combinations of two pairs of masses in Cavendish experiment can cause the movement of masses, likewise the combinations of the planets of the Solar system can cause the motion of the planets. 


'''
)

de_earth = _('''                                                                                                                                                                                
53 Das große Tao ist eben und schlicht, doch die Menschen bevorzugen die verschlungenen Seitenpfade.

'''
)

ru_earth = _('''                                                                                                                                                                                
53 Великий Дао ровен и прост, но люди предпочитают окольные тропы.

'''
)

earth = {"en":en_earth, "de":de_earth, "ru":ru_earth, }

st.title(_("Earth"))


st.write(earth[st.session_state.itaolang])


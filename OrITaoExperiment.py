import streamlit as st
import gettext

localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

en_caexp = _('''
It is not difficult to verify that the real cause of the rotation of torsion balance in Cavendish experiment is not gravitational force between masses, but the interaction of two pairs of masses. It is amazing that this cause was not properly investigated.

If to place on one line the small equal masses (m) of torsion balance symmetrically between the suspended big equal masses (M), then the rotation of torsion balance will take place anticlockwise viewing from top. The rotation will depend on symmetry, an intersection between two lines connecting two pairs of masses, the masses and distances between them. Other combinations where masses are placed on one line can cause rotation also.

There will be no rotation if only one suspended big mass of any weight is used. The insertion of the second big mass will cause rotation again.
    
The procedure is simple:

1. Place two big equal masses in proper positions and let oscillating stop.    
    
2. Remove one big mass and let oscillating stop.    
    
3. Remove second big mass and let oscillating stop.

The symmetry and equal (identical) masses are important for the rotation of torsion balance. Even the standard torsion balance with the swivel support can be used to prove this. In such a case the symmetric swivel support must be set perpendicular to the bob arm of torsion balance and stay without masses during an experiment. To achieve the best results the swivel support must be removed and only two suspended pairs of masses are used. 

The calculations can be correct but their interpretations wrong. Even though the Cavendish experiment allows make calculations of so called gravitational constant, it disproves an existence of gravitation between any two masses. However it proves that certain combinations of masses can cause the motion of masses. Such combinations of objects where two identical objects define the behavior of a symmetrical system of objects are also not difficult to find in the phenomena of electricity and magnetism.

The misfortunate attempt to invent gravitation using electric current is shown on the following video.

'''
)

de_caexp = _('''                                                                                                                                                                                
Es ist nicht schwer nachzuweisen, dass die eigentliche Ursache für die Drehung der Torsionswaage im Cavendish-Experiment nicht die Gravitationskraft zwischen den Massen ist, sondern die Wechselwirkung zweier Massenpaare. Es ist erstaunlich, dass diese Ursache nicht eingehend untersucht wurde.

Werden die kleinen, gleich großen Massen (m) der Torsionswaage symmetrisch auf einer Linie zwischen den aufgehängten großen, gleich großen Massen (M) angeordnet, so erfolgt eine Drehung der Torsionswaage – von oben betrachtet – entgegen dem Uhrzeigersinn. Diese Drehung hängt von der Symmetrie, dem Schnittpunkt der beiden Verbindungslinien zwischen den jeweiligen Massenpaaren sowie von den Massen selbst und deren Abständen ab. Auch andere Anordnungen, bei denen die Massen auf einer Linie liegen, können eine Drehung hervorrufen.

Es findet keine Rotation statt, wenn nur eine einzige aufgehängte große Masse beliebigen Gewichts verwendet wird. Das Einbringen der zweiten großen Masse bewirkt hingegen wieder eine Rotation.

Das Verfahren ist einfach:

1. Platzieren Sie zwei große, gleich große Massen an den entsprechenden Positionen und lassen Sie die Schwingung stoppen.

2. Entfernen Sie eine der großen Massen und lassen Sie die Schwingung stoppen.

3. Entfernen Sie die zweite große Masse und lassen Sie die Schwingung stoppen.

Für die Drehung der Torsionswaage sind Symmetrie und gleiche (identische) Massen wichtig. Als Beweis dafür kann bereits die serienmäßige Torsionswaage mit Schwenklager herangezogen werden. In einem solchen Fall muss die symmetrische Drehhalterung senkrecht zum Schwenkarm der Torsionswaage stehen und während eines Experiments ohne Massen bleiben. Um die besten Ergebnisse zu erzielen, muss die Schwenkhalterung entfernt werden und nur noch zwei aufgehängte Massenpaare verwendet werden.

Die Berechnungen mögen korrekt sein, doch ihre Interpretation ist falsch. Obwohl das Cavendish-Experiment Berechnungen der sogenannten Gravitationskonstante ermöglicht, widerlegt es die Existenz einer Gravitation zwischen beliebigen zwei Massen. Es belegt jedoch, dass bestimmte Massenkombinationen eine Bewegung von Massen hervorrufen können. Solche Objektkombinationen, bei denen zwei identische Objekte das Verhalten eines symmetrischen Systems bestimmen, lassen sich auch bei elektrischen und magnetischen Phänomenen finden.

Das folgende Video zeigt den missglückten Versuch, Gravitation mithilfe von elektrischem Strom zu erfinden.

'''
)

ru_caexp = _('''                                                                                                                                                                                
Нетрудно убедиться, что подлинной причиной поворота крутильных весов в опыте Кавендиша является не гравитационное взаимодействие между массами, а взаимодействие двух пар масс. Удивительно, что эта причина не была должным образом исследована.

Если расположить малые равные массы (m) крутильных весов на одной линии симметрично между подвешенными большими равными массами (M), то глядя сверху будет наблюдаться поворот крутильных весов против часовой стрелки. Характер поворота будет зависеть от симметрии, взаимного расположения линий, соединяющих пары масс, а также от величины самих масс и расстояний между ними. Поворот может возникать и при иных вариантах взаимного расположения масс на одной линии.

Поворота не произойдет, если используется лишь одна подвешенная большая масса (независимо от ее веса); добавление второй большой массы вновь вызовет поворот.

Процедура проста:

1. Разместите две большие равные массы в соответствующих положениях и дождитесь прекращения колебаний.

2. Уберите одну большую массу и дождитесь прекращения колебаний.

3. Уберите вторую большую массу и дождитесь прекращения колебаний.

Симметрия и равенство (идентичность) масс играют важную роль во вращении крутильных весов. Это можно продемонстрировать даже с помощью стандартных крутильных весов, оснащенных поворотной опорой. В таком случае симметричную поворотную опору следует установить перпендикулярно коромыслу весов и оставить без грузов на время эксперимента. Для достижения наилучших результатов опору лучше убрать, используя лишь две подвешенные пары масс.

Расчеты могут быть верными, а их интерпретация — ошибочной. Хотя эксперимент Кавендиша позволяет вычислить так называемую гравитационную постоянную, он опровергает существование гравитации между любыми двумя массами. Вместе с тем он доказывает, что определенные комбинации масс способны приводить их в движение. Подобные сочетания объектов, где два идентичных тела определяют поведение симметричной системы, нетрудно найти также в явлениях электричества и магнетизма.

На следующем видео показана неудачная попытка изобрести гравитациё с помощью электрического тока.

'''
)

st.title(_("Cavendish-Experiment"))

st.image("images/torsion.png")
#st.image("images/Cavendish 2.png")

caexp = {"en":en_caexp, "de":de_caexp, "ru":ru_caexp, }


st.write(caexp[st.session_state.itaolang])

st.video("images/Cavendish_english_subtitles_burned.mp4")

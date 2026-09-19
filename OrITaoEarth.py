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

(1)     t1² : t2² = r1³ : r2³

It is possible to rewrite (1) as (2).

t1² / r1 : t2² / r2 = r1² : r2²

(2)     1 / r1² : 1 / r2² = r1 / t1² : r2 / t2²

Taking for simplicity the accelerations for circular motion of planets one gets (3).

a = v² / r

v = 2πr / t

a = 4π²r / t²

(3)     r1 / t1² : r2 / t2² = a1 : a2

Combining (2) and (3) one gets that accelerations are inversely proportional to the square of distances (4).

(4)     1 / r1² : 1 / r2² = a1 : a2 

In such a way the Kepler’s law (2) is actually the Newton’s law without masses: accelerations are inversely proportional to the square of distances (4). Using the second Newton’s law one gets the Newton’s law with masses (5). The forces involved in motion of planets are proportional to the masses of planets and inversely proportional to the square of the distances.

f = m a

(5)     m1 / r1² : m2 / r2² = f1 : f2 

The expression (5) does not mean that any masses attract each other. It means that the planets are moving in compliance with the Kepler’s law (2). If an object falls on a planet it moves in compliance with the motions of the planets, but it does not mean that an object attracts a planet. There is neither such evidence nor evidence that all objects on some planet attract each other. The planets of the Solar system do not exist by themselves they exist only together in combination with other planets of the Solar system. As well as the combinations of two pairs of masses in Cavendish experiment can cause the movement of masses, likewise the combinations of the planets of the Solar system can cause the motion of the planets. 

'''
)

de_earth = _('''                                                                                                                                                                                
In seinem Werk Harmonice Mundi (Die Weltharmonik) beschreibt Kepler die Erde als ein beseeltes Wesen. Lebendig zu sein bedeutet, über ein Bewusstsein zu verfügen. Die Erde zieht Objekte nicht als bewusstlose Masse an, sondern sie handelt bewusst – vergleichbar mit einem Menschen, der sich bewusst die Hand an die Stirn legt. Die Erde besitzt ein Bewusstsein, das sich in ihren rhythmischen Prozessen wahrnehmen lässt. Es wurde bekannt gegeben, dass Gravitationswellen registriert worden seien; tatsächlich registriert wurde jedoch ein rhythmischer Prozess mit einer Periode von 36 bis 38 Jahren.

Das Leben des Menschen im physischen Körper hängt vom Leben der Erde ab. Es ist unschwer zu erkennen, dass ein Mensch, der von einem Aufenthalt auf einer Raumstation zur Erde zurückkehrt, geschwächt ist, nicht ohne fremde Hilfe gehen kann und Unterstützung benötigt. Ein Pilot, der – wenn auch in geringerem Abstand zur Erdoberfläche – ähnlichen oder sogar weitaus stärkeren Belastungen ausgesetzt ist, benötigt eine solche Hilfe nicht und kann unmittelbar nach der Landung ohne Unterstützung gehen. Entscheidend ist also nicht die durch den Flug verursachte Belastung, sondern die Verbindung des Menschen zur Erde. Es lässt sich nachweisen, dass diese Verbindung umgekehrt proportional zum Abstand von der Erde ist. Jener Abstand von der Erde, bei dem ein Mensch im physischen Körper nicht mehr überleben kann, liegt im Bereich des Sieben- bis Zwölffachen des Erdradius.

Es herrscht die weitverbreitete Auffassung, dass der Mensch – da er in einem Taucheranzug unter Wasser und in einem Raumanzug in gewissem Abstand zur Erde existieren kann – auch in jeder beliebigen Entfernung von der Erde, etwa auf dem Mond, leben könne. Dabei wird jedoch außer Acht gelassen, dass man beim Tauchen unter Wasser auf der Erde verbleibt und die Verbindung zu ihr aufrechterhält, während man diese Verbindung verliert, sobald man sich weit genug von der Erde entfernt. Sämtliche sogenannten Beweise für die Anwesenheit des Menschen im physischen Körper auf dem Mond lassen sich auch ohne eine solche Anwesenheit erbringen. Das Erreichen einer Entfernung von der Erde, die geringer ist als der Abstand zwischen Erde und Mond, aber im Bereich des Sieben- bis Zwölffachen des Erdradius liegt, wäre für den Menschen tödlich. Dies entspricht etwa dem Bereich, in dem die geostationäre Umlaufbahn beginnt.

Das Leben des Menschen hängt in einem solchen Maße vom Leben der Erde ab, dass der Mensch im physischen Körper zu einem untrennbaren Teil der Erde geworden ist. Das bedeutet, dass der Mensch in seinem physischen Körper nicht ohne die Erde existieren kann. Bemannte Raumfahrzeuge – oder solche, die höhere Tiere an Bord haben – sollten versuchen, eine Entfernung von sieben bis zwölf Erdradien zur Erde zu erreichen. Die Durchführung eines solchen Experiments ist notwendig, um falsche Vorstellungen von Existenz und Realität auszuräumen.

Die Vorstellung von der Gravitation

Es ist nicht möglich, die Wechselwirkung zweier Massenpaare im Cavendish-Experiment mithilfe der Vorstellung einer universellen Gravitation zu erklären, da diese Vorstellung nicht der Realität entspricht. Bevor Schlussfolgerungen über die Existenz von Gravitation gezogen werden können, muss man zu unterscheiden versuchen, inwieweit das beobachtete Phänomen von anderen Phänomenen abgegrenzt ist und inwieweit es einen Teil des Ganzen bildet. So muss beispielsweise das Sonnensystem als Ganzes und die Planeten als untrennbare Bestandteile des Sonnensystems betrachtet werden.

Es ist allgemein bekannt, dass das Newtonsche Gravitationsgesetz aus den Keplerschen Gesetzen für die Planeten des Sonnensystems abgeleitet wurde. Eine solche Ableitung und Berechnung ist möglich, weil das Keplersche Gesetz das Newtonsche Gesetz ohne Berücksichtigung der Massen enthält. Das Keplersche Gesetz besagt, dass sich die Quadrate der Umlaufzeiten der Planeten wie die Kuben der großen Halbachsen ihrer Umlaufbahnen verhalten (1).

(1)     t1² : t2² = r1³ : r2³

Es ist möglich, (1) in (2) umzuformen.

t1² / r1 : t2² / r2 = r1² : r2²

(2)     1 / r1² : 1 / r2² = r1 / t1² : r2 / t2²

Betrachtet man der Einfachheit halber die Beschleunigungen bei der Kreisbewegung der Planeten, so erhält man (3).

a = v² / r

v = 2πr / t

a = 4π²r / t²

(3)     r1 / t1² : r2 / t2² = a1 : a2

Durch Kombination von (2) und (3) ergibt sich, dass die Beschleunigungen umgekehrt proportional zum Quadrat der Abstände sind (4).

(4)     1 / r1² : 1 / r2² = a1 : a2

Auf diese Weise stellt das Keplersche Gesetz (2) eigentlich das Newtonsche Gesetz ohne Massen dar: Die Beschleunigungen sind umgekehrt proportional zum Quadrat der Abstände (4). Unter Anwendung des zweiten Newtonschen Gesetzes gelangt man zu dem Newtonschen Gesetz unter Berücksichtigung der Massen (5). Die bei der Planetenbewegung wirkenden Kräfte sind proportional zu den Massen der Planeten und umgekehrt proportional zum Quadrat der Abstände.

f = m a

(5)     m1 / r1² : m2 / r2² = f1 : f2

Der Ausdruck (5) bedeutet nicht, dass sich beliebige Massen gegenseitig anziehen. Er besagt vielmehr, dass sich die Planeten im Einklang mit dem Keplerschen Gesetz (2) bewegen. Fällt ein Objekt auf einen Planeten, so bewegt es sich zwar in Übereinstimmung mit der Planetenbewegung, doch bedeutet dies nicht, dass das Objekt den Planeten anzieht. Es gibt hierfür ebenso wenig einen Beleg wie für die Annahme, dass sich alle Objekte auf einem Planeten gegenseitig anziehen. Die Planeten des Sonnensystems existieren nicht isoliert, sondern nur im Verbund mit den anderen Planeten des Sonnensystems. So wie die Kombinationen zweier Massenpaare im Cavendish-Experiment eine Bewegung der Massen hervorrufen können, so können auch die Kombinationen der Planeten des Sonnensystems deren Bewegung bewirken.


'''
)

ru_earth = _('''                                                                                                                                                                                
В своем труде «Гармония мира» (Harmonices Mundi) Кеплер описывает Землю как одушевленное существо. Быть живым — значит обладать сознанием. Земля притягивает объекты не как лишенная сознания масса; она действует осознанно — подобно тому, как человек сознательно кладет руку на лоб. Земля обладает сознанием, которое можно ощутить через ее ритмические процессы. Было объявлено о регистрации гравитационных волн; однако на самом деле был зафиксирован ритмический процесс с периодом 36–38 лет.

Жизнь человека в физическом теле зависит от жизни Земли. Нетрудно заметить, что человек, возвращающийся на Землю после пребывания на космической станции, оказывается ослабленным, не может ходить без посторонней помощи и нуждается в поддержке. Пилот реактивного самолета, испытывающий такие же или даже гораздо более сильные перегрузки (но находящийся гораздо ближе к поверхности Земли), в подобной помощи не нуждается и способен ходить самостоятельно сразу после посадки. Следовательно, решающее значение имеют не перегрузки, вызванные полетом, а связь человека с Землей. Можно убедиться, что эта связь обратно пропорциональна расстоянию до Земли. Расстояние, на котором человек в физическом теле уже не может существовать, составляет от семи до двенадцати земных радиусов.

Существует распространенное мнение: если человек может находиться под водой в водолазном костюме или на некотором удалении от Земли в скафандре, то он способен существовать и на любом другом расстоянии от Земли — например, на Луне. При этом упускается из виду, что при погружении под воду человек остается на Земле и сохраняет связь с ней, тогда как при значительном удалении от планеты эта связь утрачивается. Все так называемые доказательства пребывания человека в физическом теле на Луне могут быть созданы и без реального присутствия там человека. Удаление от Земли на расстояние, меньшее, чем дистанция до Луны, но попадающее в диапазон от семи до двенадцати земных радиусов, стало бы для человека смертельным. Именно здесь, приблизительно, начинается геостационарная орбита.

Жизнь человека настолько зависит от жизни Земли, что человек в физическом теле стал неотъемлемой частью Земли. Это означает, что человек в физическом теле не может существовать без Земли. Пилотируемому космическому кораблю или кораблю с высшими животными на борту следует попытаться достичь расстояния от Земли, составляющего от семи до двенадцати земных радиусов. Проведение такого эксперимента необходимо для устранения неверных представлений о существовании и реальности.

Идея гравитации

Объяснить взаимодействие двух пар масс в эксперименте Кавендиша с помощью идеи всемирного тяготения невозможно, поскольку эта идея не соответствует действительности. Прежде чем делать выводы о существовании гравитации, необходимо попытаться определить, в какой мере наблюдаемое явление обособлено от других явлений и в какой мере оно составляет часть целого. Так, Солнечную систему следует рассматривать как единое целое, а планеты — как неотъемлемые части этой системы.

Хорошо известно, что закон всемирного тяготения Ньютона был выведен на основе законов Кеплера для планет Солнечной системы. Такой вывод и расчет возможны, поскольку закон Кеплера фактически содержит в себе закон Ньютона, но без учета масс. Согласно закону Кеплера, квадраты периодов обращения планет пропорциональны кубам больших полуосей их орбит (1).

(1)     t1² : t2² = r1³ : r2³

Соотношение (1) можно переписать в виде (2).

t1² / r1 : t2² / r2 = r1² : r2²

(2)     1 / r1² : 1 / r2² = r1 / t1² : r2 / t2²

Если для простоты рассмотреть ускорения при круговом движении планет, получим (3).

a = v² / r

v = 2πr / t

a = 4π²r / t²

(3)     r1 / t1² : r2 / t2² = a1 : a2

Объединив (2) и (3), приходим к выводу, что ускорения обратно пропорциональны квадратам расстояний (4).

(4)     1 / r1² : 1 / r2² = a1 : a2

Таким образом, закон Кеплера (2) — это, по сути, закон Ньютона без учета масс: ускорения обратно пропорциональны квадратам расстояний (4). Используя второй закон Ньютона, можно получить закон Ньютона, учитывающий массы (5). Силы, определяющие движение планет, пропорциональны массам планет и обратно пропорциональны квадратам расстояний.

f = m a

(5)     m1 / r1² : m2 / r2² = f1 : f2

Выражение (5) не означает, что любые массы притягиваются друг к другу. Оно означает, что планеты движутся в соответствии с законом Кеплера (2). Если какой-либо объект падает на планету, он движется в соответствии с закономерностями движения планет, однако это не означает, что сам объект притягивает планету. Не существует ни таких доказательств, ни свидетельств того, что все объекты на планете притягиваются друг к другу. Планеты Солнечной системы не существуют обособленно; они существуют лишь во взаимосвязи с другими планетами Солнечной системы. Подобно тому как взаимодействие двух пар масс в опыте Кавендиша может вызывать движение этих масс, так и взаимодействие планет Солнечной системы может обусловливать движение самих планет.


'''
)

earth = {"en":en_earth, "de":de_earth, "ru":ru_earth, }

st.title(_("Earth"))


st.write(earth[st.session_state.itaolang])



import streamlit as st
#from streamlit_image_coordinates import streamlit_image_coordinates

import numpy as np
import math

import matplotlib.pyplot as plt

import neurokit2 as nk
import gettext


localizator = gettext.translation('messages', localedir='locales', languages=[st.session_state.itaolang])
localizator.install() 
_ = localizator.gettext 

FIGPNGFILENAME = "images/fig.png"

en_pqrst = _('''                                                                                                                                                                                
The application based on neurokit2 package demonstrates the behavior of the PQRST complex as a whole.
Instead of usual PQRST peaks, the vertical half-lemniscates are used.
The height of half-lemniscate is equal to the height of usual PQRST peak.
The values of the PQRST peaks and percentage of half-lemniscates squares are shown.
The Q and S peaks can have negative values.
It allows to see, that any change of one part of PQRST peak leads to the change of the whole PQRST complex.

'''
)

de_pqrst = _('''                                                                                                                                                                                
Die auf dem Paket „neurokit2“ basierende Anwendung veranschaulicht das Verhalten des PQRST-Komplexes als Ganzes. 
Anstelle der üblichen PQRST-Zacken werden vertikale Halblemniskaten verwendet. 
Die Höhe der Halblemniskate entspricht dabei der Höhe der jeweiligen PQRST-Zacke. 
Angezeigt werden die Werte der PQRST-Zacken sowie die Flächeninhalte der Halblemniskaten (in Prozent). 
Die Q- und S-Zacken können negative Werte aufweisen. 
Dies macht deutlich, dass jede Veränderung eines Teils einer PQRST-Zacke zu einer Veränderung des gesamten PQRST-Komplexes führt.
'''
)

ru_pqrst = _('''                                                                                                                                                                                
Приложение, разработанное на основе пакета neurokit2, демонстрирует поведение комплекса PQRST в целом. 
Вместо привычных пиков PQRST используются вертикальные полулемнискаты; высота полулемниската соответствует высоте стандартного пика PQRST. 
Отображаются значения пиков PQRST и площади полулемнискатов (в процентах). 
Пики Q и S могут принимать отрицательные значения. 
Это позволяет наглядно увидеть, что изменение любой части пика PQRST влечет за собой изменение всего комплекса PQRST.
'''
)

pqrst = {"en":en_pqrst, "de":de_pqrst, "ru":ru_pqrst, }

st.title(_("PQRST"))

if "PQRSTidx" not in st.session_state:
    st.session_state.PQRSTidx = 0
if "sigidx" not in st.session_state:
    st.session_state.sigidx = 0
if "pauseidx" not in st.session_state:
    st.session_state.pauseidx = 0
if "figrun" not in st.session_state:
    st.session_state.figrun = False
    
def msg(msg):
    placeholder = st.empty()
    with placeholder.container():
        st.write(msg)

def percentage(part, whole):
    if whole == 0:
        return 0
    return 100 * float(part)/float(whole)


def CassiniXY(x, y):
#(x**2 + y**2)**2 - 2*a**2*(x**2 - y**2) + a**4 - b**4 = 0
#a == b
#(x**2 + y**2)**2 = 2*a**2*(x**2 - y**2)
#a = np.sqrt((x**2 + y**2)**2 / 2*(x**2 - y**2))
    
#    valid = 2*(x**2 - y**2)
#    a = np.sqrt((x**2 + y**2)**2 / valid)
#    return np.abs(a)    

    return np.abs(x/np.sqrt(2))  
   

# plt.savefig("plot.png", format="png")
#https://mathcurve.com/courbes2d.gb/cassini/cassini.shtml
#https://stackoverflow.com/questions/71684763/plot-cassini-ovals-in-python-using-numpy-and-matplotlib
def CassiniSteinerShort(a, b, clr=None, vertical=True, half=False, upper=False, linestyle='-', show=True, N=1000000):

#    y = np.sqrt(np.abs(np.sqrt(b**4  + 4*a**2*x**2 ) - (a**2 + x**2)))
#    y = np.sqrt(np.abs(np.sqrt(b**4  + 4*a**2*x**2 ) - (a**2 + x**2)))
#    If a ≤ b ≤ a√2 the "ovals" look no more like circles. 
#    Here a is one, b goes from 1 to √2 (inclusively)               

#    print ("CassiniSteinerShort")    
    t = np.linspace(-a + np.sqrt(a**2 + b**2), a + np.sqrt(a**2 + b**2), N)
    if a >= b:
        t = np.linspace(a + np.sqrt(a**2 - b**2), a + np.sqrt(a**2 + b**2), N)
    x = (b**4 - t**4)/(4*a*(t**2))
    y = np.sqrt(np.abs(t**2 - ((x-a)**2)))
    
#        plt.scatter(x, y, c='red', s=2, zorder=2)
    if vertical == True:
        if upper == False:
            plt.plot(y, x, clr, ls=linestyle) # right part
            plt.plot(-y, x, clr, ls=linestyle) # left part
            if half == False:
                plt.plot(-y, -x, clr, ls=linestyle) # right part
                plt.plot(y, -x, clr, ls=linestyle) # left part
        else:
            plt.plot(y, -x, clr, ls=linestyle) # right part
            plt.plot(-y, -x, clr, ls=linestyle) # left part                        
            if half == False:
                plt.plot(-y, x, clr, ls=linestyle) # right part
                plt.plot(y, x, clr, ls=linestyle) # left part            
    else:
        plt.plot(x, y, clr, ls=linestyle) # left upper part
        plt.plot(x, -y, clr, ls=linestyle) # left lower part        
        if half == False:
            plt.plot(-x, y, clr, ls=linestyle) # right upper part
            plt.plot(-x, -y, clr, ls=linestyle) # right lower part
        
    
    if show == True:
        fig = plt.gcf()
        st.pyplot(fig)
        plt.savefig(FIGPNGFILENAME, format="png")
        st.image(FIGPNGFILENAME)
#        plt.show()


def square_lemniscate(val):
    S = val**2
    return S
 
def volume_lemniscate(val):
    sq = math.sqrt(2)
    V = 2 * ((math.pi * val**3) / 4) * (sq * math.log(sq + 1) - 2/3)
#    V = 2 * ((math.pi * val**3) / 4) * math.floor(sq * math.log(sq + 1) - 2/3)
    return V
 
def zero_NaN(peaks, val=0):
    for x in range(len(peaks)):
        if math.isnan(peaks[x]) == True:
            peaks[x] = val
        
#    https://discuss.streamlit.io/t/continuously-updating-image-content/86954/2
@st.fragment(run_every=1)
def draw_image(pause, algorithm_name, data_name, samplerate):
    if pause == 0:
        return None

    st.image(FIGPNGFILENAME)
    if st.session_state.figrun == False:
        r0, r1, r2, r3, r4, r5 = initComplex(pause, algorithm_name, data_name, samplerate)
        st.session_state.figrun = True
        st.session_state.itaor0 = r0
        st.session_state.itaor1 = r1
        st.session_state.itaor2 = r2
        st.session_state.itaor3 = r3
        st.session_state.itaor4 = r4
        st.session_state.itaor5 = r5
    if st.session_state.figrun == True:
        updateComplex(st.session_state.itaor0, st.session_state.itaor1, st.session_state.itaor2, 
                      st.session_state.itaor3, st.session_state.itaor4, st.session_state.itaor5)
        plt.savefig(FIGPNGFILENAME, format="png")      
        

def initComplex(pause, algorithm_name, data_name, samplerate):
    
    msg('Retrieving data ' + data_name + ' (neurokit2)')
#        bio_eventrelated_100hz bio_resting_8min_100hz bio_resting_5min_100hz samplerate = 100
#        samplerate = 100
    data = nk.data(dataset=data_name)
#        data = nk.data(dataset="bio_resting_5min_100hz")
    ecg_signal = data["ECG"]
        
    msg('Retrieving EKG peaks (neurokit2)')

    # Extract R-peaks locations nabian2018 elgendi2010 martinez2004 neurokit
    sigs, rpeaks = nk.ecg_peaks(ecg_signal, method=algorithm_name, sampling_rate=samplerate)
                
    msg('Delineating EKG (neurokit2)')

    # Delineate the ECG signal method = peak cwt dwt
    sigs, waves_peak = nk.ecg_delineate(ecg_signal, rpeaks, sampling_rate=samplerate, method="peak")
    
    r0 = ecg_signal
    r1 = waves_peak['ECG_P_Peaks']
    r2 = waves_peak['ECG_Q_Peaks']
    r3 = rpeaks['ECG_R_Peaks']
    r4 = waves_peak['ECG_S_Peaks']
    r5 = waves_peak['ECG_T_Peaks']               
    
    minLen = min(len(waves_peak['ECG_P_Peaks']), len(waves_peak['ECG_Q_Peaks'])-1, len(rpeaks['ECG_R_Peaks'])-1, len(waves_peak['ECG_S_Peaks'])-1, len(waves_peak['ECG_T_Peaks'])-1)
    if st.session_state.PQRSTidx in range(0, minLen):
        if pause == 0:
#            print("PAUSE")
            return None, None, None, None, None, None
    return r0, r1, r2, r3, r4, r5
    
                       
def updateComplex(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks):
    idx = st.session_state.sigidx
    if idx == 0:
#        msg('Plotting PQRST')
        update_PQRST(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks)        
    elif idx == 1:
#        msg('Plotting BLOOD')
        update_BLOOD(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks)        
    elif idx == 2:
#        msg('Plotting SIGNAL')
        update_SIGNAL(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks)        

               
def update_PQRST(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks):
    plt.clf()
            
    zero_NaN(p_peaks)
    zero_NaN(q_peaks)
    zero_NaN(r_peaks)
    zero_NaN(s_peaks)
    zero_NaN(t_peaks)
    
    minLen = min(len(p_peaks), len(q_peaks)-1, len(r_peaks)-1, len(s_peaks)-1, len(t_peaks)-1)
    if st.session_state.PQRSTidx >= minLen:
#            print('update limit reached idx=' + str(idxs))
        st.session_state.PQRSTidx = 0

#        print('update idx=' + str(idxs))
    
    idx = st.session_state.PQRSTidx
    
    clrP = 'orange'
    clrQ = 'green'
    clrR = 'red'
    clrS = 'blue'
    clrT = 'brown'
    
    total_sum = np.abs(unfiltered_ecg[p_peaks[idx]]) + np.abs(unfiltered_ecg[q_peaks[idx]]) + np.abs(unfiltered_ecg[r_peaks[idx]]) + np.abs(unfiltered_ecg[s_peaks[idx]]) + np.abs(unfiltered_ecg[t_peaks[idx]])
    
    a = CassiniXY(unfiltered_ecg[p_peaks[idx]], 0)
    CassiniSteinerShort(a, a, clr=clrP, half=True, upper=True, show=False)
    a = CassiniXY(unfiltered_ecg[q_peaks[idx]], 0)
    CassiniSteinerShort(a, a, clr=clrQ, half=True, upper=False, show=False)
    a = CassiniXY(unfiltered_ecg[r_peaks[idx]], 0)
    CassiniSteinerShort(a, a, clr=clrR, half=True, upper=True, show=False)
    a = CassiniXY(unfiltered_ecg[s_peaks[idx]], 0)
    CassiniSteinerShort(a, a, clr=clrS, half=True, upper=False, show=False)
    a = CassiniXY(unfiltered_ecg[t_peaks[idx]], 0)
    CassiniSteinerShort(a, a, clr=clrT, half=True, upper=True, show=False)
    
    fs = 8
    x = 0.5
    y = 0.5
    
    perc_p = ' ' + str(abs(round(percentage(unfiltered_ecg[p_peaks[idx]], total_sum), 2))) +'% '
    perc_q = ' ' + str(abs(round(percentage(unfiltered_ecg[q_peaks[idx]], total_sum), 2))) +'% '
    perc_r = ' ' + str(abs(round(percentage(unfiltered_ecg[r_peaks[idx]], total_sum), 2))) +'% '
    perc_s = ' ' + str(abs(round(percentage(unfiltered_ecg[s_peaks[idx]], total_sum), 2))) +'% '
    perc_t = ' ' + str(abs(round(percentage(unfiltered_ecg[t_peaks[idx]], total_sum), 2))) +'% '

    label = 'P ' + str(unfiltered_ecg[p_peaks[idx]]) + perc_p 
    plt.plot(x, y, clrP, label=label)
    label = 'Q ' + str(unfiltered_ecg[q_peaks[idx]]) + perc_q 
    plt.plot(x, y, clrQ, label=label)
    label = 'R ' + str(unfiltered_ecg[r_peaks[idx]]) + perc_r
    plt.plot(x, y, clrR, label=label)
    label = 'S ' + str(unfiltered_ecg[s_peaks[idx]]) + perc_s
    plt.plot(x, y, clrS, label=label)
    label = 'T ' + str(unfiltered_ecg[t_peaks[idx]]) + perc_t
    plt.plot(x, y, clrT, label=label)        
    plt.legend(fontsize=str(fs), loc='lower right')
                    
    plt.title("PQRST plot " + str(st.session_state.PQRSTidx))
    
#    plt.pause(1)
    
    st.session_state.PQRSTidx += 1

               
def update_BLOOD(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks):
    plt.clf()
            
    zero_NaN(p_peaks)
    zero_NaN(q_peaks)
    zero_NaN(r_peaks)
    zero_NaN(s_peaks)
    zero_NaN(t_peaks)
    
    minLen = min(len(p_peaks), len(q_peaks)-1, len(r_peaks)-1, len(s_peaks)-1, len(t_peaks)-1)
    if st.session_state.PQRSTidx >= minLen:
#            print('update limit reached idx=' + str(idxs))
        st.session_state.PQRSTidx = 0

#        print('update idx=' + str(idxs))
    
    idx = st.session_state.PQRSTidx          
    
    dblf = 25 # display blood factor
    
    clrP = 'orange'
    clrQ = 'green'
    clrR = 'pink'
    clrS = 'blue'
    clrT = 'brown'
    
    total_sum = np.abs(unfiltered_ecg[p_peaks[idx]]) + np.abs(unfiltered_ecg[q_peaks[idx]]) + np.abs(unfiltered_ecg[r_peaks[idx]]) + np.abs(unfiltered_ecg[s_peaks[idx]]) + np.abs(unfiltered_ecg[t_peaks[idx]])
    
    a = CassiniXY(unfiltered_ecg[p_peaks[idx]], 0)
    a *= dblf
    CassiniSteinerShort(a, a, clr=clrP, half=True, upper=True, show=False)
    a = CassiniXY(unfiltered_ecg[q_peaks[idx]], 0)
    a *= dblf
    CassiniSteinerShort(a, a, clr=clrQ, half=True, upper=False, show=False)
    a = CassiniXY(unfiltered_ecg[r_peaks[idx]], 0)
    a *= dblf
    CassiniSteinerShort(a, a, clr=clrR, half=True, upper=True, show=False)
    a = CassiniXY(unfiltered_ecg[s_peaks[idx]], 0)
    a *= dblf
    CassiniSteinerShort(a, a, clr=clrS, half=True, upper=False, show=False)
    a = CassiniXY(unfiltered_ecg[t_peaks[idx]], 0)
    a *= dblf
    CassiniSteinerShort(a, a, clr=clrT, half=True, upper=True, show=False)

    clrPQRST = 'white'
    clrBLOOD = 'red'
    
    ls='--'
    bloodc =  (18 * total_sum) # total energy of blood circulation
    if idx % 4 == 0:
        ls='-'
    
    a = 18.5 
#    a = CassiniXY(bloodc, 0)
    b = np.sqrt(np.abs(bloodc**2 - a**2))
    print(str(idx) + ' a='+ str(a)  + ' b='+ str(b))

#    print(str(idx) + ' a='+ str(a)  + ' b='+ str(bloodc))
    CassiniSteinerShort(a, b, clr=clrBLOOD, vertical=True, half=False, upper=True, linestyle=ls, show=False)
    
    fs = 8
    x = 0.5
    y = 0.5
    
    label = 'PQRST ' + str(total_sum)
    plt.plot(x, y, clrPQRST, label=label)
    label = 'BLOOD ' + str(bloodc)
    plt.plot(x, y, clrBLOOD, label=label)
    plt.legend(fontsize=str(fs), loc='lower right')
                    
    plt.title("BLOOD plot " + str(st.session_state.PQRSTidx))
    
#    plt.pause(1)
    
    st.session_state.PQRSTidx += 1
               
def update_BLOOD_2(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks):
    plt.clf()
            
    zero_NaN(p_peaks)
    zero_NaN(q_peaks)
    zero_NaN(r_peaks)
    zero_NaN(s_peaks)
    zero_NaN(t_peaks)
    
    minLen = min(len(p_peaks), len(q_peaks)-1, len(r_peaks)-1, len(s_peaks)-1, len(t_peaks)-1)
    if st.session_state.PQRSTidx >= minLen:
#            print('update limit reached idx=' + str(idxs))
        st.session_state.PQRSTidx = 0

#        print('update idx=' + str(idxs))
    
    clrS = 'blue'
    clrB = 'red'

    idx = st.session_state.PQRSTidx          
    
    total_sum = np.abs(unfiltered_ecg[p_peaks[idx]]) + np.abs(unfiltered_ecg[q_peaks[idx]]) + np.abs(unfiltered_ecg[r_peaks[idx]]) + np.abs(unfiltered_ecg[s_peaks[idx]]) + np.abs(unfiltered_ecg[t_peaks[idx]])
    
    a = CassiniXY(total_sum, 0)
    CassiniSteinerShort(a, a, clr=clrS, vertical=True, half=True, upper=False, show=False)
    
    ls='--'
    bloodc =  (18 * total_sum) # total energy of blood circulation
    if idx % 4 == 0:
        ls='-'
        
    a = CassiniXY(bloodc, 0)
#    print(str(idx) + ' a='+ str(a)  + ' b='+ str(bloodc))
    CassiniSteinerShort(a, a, clr=clrB, vertical=True, half=True, upper=True, linestyle=ls, show=False)
    
    fs = 8
    x = 0.5
    y = 0.5
    
    label = 'PQRST ' + str(total_sum)
    plt.plot(x, y, clrS, label=label)
    label = 'BLOOD ' + str(bloodc)
    plt.plot(x, y, clrB, label=label)
    plt.legend(fontsize=str(fs), loc='lower right')
                    
    plt.title("BLOOD plot " + str(st.session_state.PQRSTidx))
    
#    plt.pause(1)
    
    st.session_state.PQRSTidx += 1
    
               
def update_SIGNAL(unfiltered_ecg, p_peaks, q_peaks, r_peaks, s_peaks, t_peaks):
    plt.clf()
            
    zero_NaN(p_peaks)
    zero_NaN(q_peaks)
    zero_NaN(r_peaks)
    zero_NaN(s_peaks)
    zero_NaN(t_peaks)
                    
    minLen = min(len(p_peaks), len(q_peaks)-1, len(r_peaks)-1, len(s_peaks)-1, len(t_peaks)-1)
    if st.session_state.PQRSTidx >= minLen:
#            print('update limit reached idx=' + str(idxs))
        st.session_state.PQRSTidx = 0

#        print('update idx=' + str(idxs))
            
    step = 1000

    upper_limit = len(unfiltered_ecg)
#        print('idxs[0]=' + str(idxs[0]) + " upper_limit=" + str(upper_limit))
                   
    if (st.session_state.PQRSTidx - 1) * step >= upper_limit:
#            print('upper limit reached idx=' + str(idxs))
        st.session_state.PQRSTidx = 0

#        print('upper idx=' + str(idxs))
    
    idx = st.session_state.PQRSTidx
    if idx > 1:
        y = unfiltered_ecg[(idx - 1) * step : idx * step]
        l = len(unfiltered_ecg[(idx - 1) * step : idx * step])
        if l < step:
#                print('l=' + str(l) + ' is less than 1000')
            x = np.linspace((idx - 1) * step, idx * step, l)
        else:
            x = np.linspace((idx - 1) * step, idx * step, step)
    else:
        y = unfiltered_ecg[0 : step]
#            l = len(unfiltered_ecg[0 : 1000])
        x = np.linspace(0, step, step)
    
#        xcoo = [n for n in range(len(y))]
#        plt.scatter(x, y, c='red', s=2, zorder=2)
    
    plt.plot(x, y)
                            
    plt.title("SIGNAL plot " + str(st.session_state.PQRSTidx))
    
#    plt.pause(1)
    
    st.session_state.PQRSTidx += 1
        

def main(): 
    algorithms = ('christov2004', 'elgendi2010', 'engzeemod2012', 
                  'gamboa2008', 'hamilton2002', 'kalidas2017', 
                  'koka2022', 'manikandan2012', 'martinez2004', 
                  'nabian2018', 'neurokit',  'pantompkins1985', 
                  'promac', 'rodrigues2021', 'zong2003')
    
    data_names = ('bio_eventrelated_100hz', 
                  'bio_resting_8min_100hz', 
                  'bio_resting_5min_100hz')
    with st.container(horizontal=True, horizontal_alignment="left"):
        pause_sel = st.radio(_(" "), ("Pause", "Run"), key = "itao_pause", horizontal=True, index=0)
        rate_sel = st.select_slider(_("Sample rate"), options=[100, 200, 300, 400, 500,],)
        dist_sel = st.number_input(_("Insert interval"), min_value=10.0, max_value=50.0, step=0.1) 
    with st.container(horizontal=True, horizontal_alignment="left"):
        alg_sel = st.selectbox(label=_("Algorithm"), options=algorithms, key="itao_algs", index=10)    
        data_sel = st.selectbox(label=_("Data name"), options=data_names, key="itao_datas", index=1)    
        sig_sel = st.radio(_("Plot"), ("PQRST", "BLOOD", "SIGNAL"), key = "itao_sig", horizontal=True, index=0)
    if sig_sel== "PQRST":
        st.session_state.sigidx = 0 
    if sig_sel== "BLOOD":
        st.session_state.sigidx = 1 
    if sig_sel== "SIGNAL":
        st.session_state.sigidx = 2
    
            
    def run_algorithm(): 
#        print("Selected algorithm: {}".format(alg_sel))
#        print("Data name {}".format(data_sel))
#        print("Sample rate {}".format(rate_sel))
                 
        msg('Running algorithm ' + alg_sel + ', Data ' + data_sel + ', Rate ' + str(rate_sel) + ' ' + sig_sel)
        draw_image(st.session_state.pauseidx, alg_sel, data_sel, rate_sel)
#        initComplex(st.session_state.pauseidx, alg_sel, data_sel, rate_sel)
        
        if st.session_state.PQRSTidx == 0:
            msg('Finished')
            msg('Select algorithm, data name, sample rate and press Run button')
        
        return None
        
    if pause_sel == "Pause":
        st.session_state.pauseidx = 0
    elif pause_sel == "Run":
        st.session_state.pauseidx = 1
        run_algorithm()
      
    st.write(pqrst[st.session_state.itaolang])
        
if __name__ == '__main__':
    main()        
            

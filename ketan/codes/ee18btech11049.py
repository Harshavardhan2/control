# License
'''
Code by Laxman Reddy
April 22,2020
Released under GNU GPL
'''

#Bode plot using scipy in python
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([75,0.2*75], [1, 16 ,100,0]) #Transfer Function = 75(1+0.2s)/s(s^2+16s+100)

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
# plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.axhline(y = 0,xmin=0,xmax= .35,color = 'r',linestyle='dashed')
plt.axvline(x = .22,ymin=0,color='k',linestyle='dashed')
plt.plot(.22,0,'o')
plt.text(0.757,0, '({}, {})'.format(0.757,-220.15))
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
# plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.axhline(y = -180,xmin=0,color = 'r',linestyle='dashed')

plt.grid() 




#if using termux
plt.savefig('./figs/ee18btech11049.pdf')
plt.savefig('./figs/ee18btech11049.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11049.pdf"))
#else
#plt.show()


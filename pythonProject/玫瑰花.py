from matplotlib import cm
from matplotlib.font_manager import FontProperties
font=FontProperties(fname='D:/PY/玫瑰花.ttc',size=25)
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.gca(projection='3d')
[x,t]=np.meshgrid(np.array(range(25))/24.0,np.arange(0,575.5,0.5)/575*17*np.pi-2*np.pi)
p=np.pi/2*np.exp(-t/(8*np.pi))
u=1-(1-np.mod(3.6*t,2*np.pi)/np.pi)**4/2
y=2*(x**2-x)**2*np.sin(p)
r=u*(x*np.sin(p)+y*np.cos(p))
surf=ax.plot_surface(r*np.cos(t),r*np.sin(t),u*(x*np.cos(p)-y*np.sin(p)),\
                     rstride=1,cstride=1,cmap=cm.gist_heat,linewidth=0,antialiased=True)
plt.title=(u'',fontproperties=font,)
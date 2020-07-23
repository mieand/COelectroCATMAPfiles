from catmap import ReactionModel
import matplotlib.pyplot as plt
import numpy as np
from ase.units import _e

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)

nelectrons = 2
ACu = (3.61E-8/np.sqrt(2.))**2 * np.sqrt(3)/2.
APt = (3.92E-8/np.sqrt(2.))**2 * np.sqrt(3)/2.

#Pt
mkm_file = 'TafelPt.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables += ['production_rate']
model.run()

Vs = []
TOFs = []
for i in model.production_rate_map:
    Vs.append(i[0][1])
    TOFs.append(i[1][0])

TOFsPt = [x*nelectrons*_e*1E6/APt for _,x in sorted(zip(Vs,TOFs))]
VsPt = [x for x,_ in sorted(zip(Vs,TOFs))]

ax.plot(VsPt,TOFsPt,color='g')

#Cu
mkm_file = 'TafelCu.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables += ['production_rate']
model.run()

Vs = []
TOFs = []
for i in model.production_rate_map:
    Vs.append(i[0][1])
    TOFs.append(i[1][0])

TOFsCu = [x*nelectrons*_e*1E6/ACu for _,x in sorted(zip(Vs,TOFs))]
VsCu = [x for x,_ in sorted(zip(Vs,TOFs))]

ax.plot(VsCu,TOFsCu,color='r')

#Cuadatom
mkm_file = 'TafelCuadatom.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables += ['production_rate']
model.run()

Vs = []
TOFs = []
for i in model.production_rate_map:
    Vs.append(i[0][1])
    TOFs.append(i[1][0])

TOFsPt = [x*nelectrons*_e*1E6/ACu for _,x in sorted(zip(Vs,TOFs))]
VsPt = [x for x,_ in sorted(zip(Vs,TOFs))]

ax.plot(VsPt,TOFsPt,color='b')

plt.yscale("log")
plt.ylim([1e-15, 1e6])
plt.xlim([-0.2, 1.7])

#Plot exp data
#Vs = []
#js = []
#with open('COOx-rawdata-selected.txt') as infile:
#    lines = infile.readlines()
#    for line in lines[1:]:
#        if line.strip():
#            values = line.strip().split('\t')
#            Vs.append(values[0])
#            js.append(values[1])

#ax.plot(Vs,js,'k--',linewidth=2)

#Plot Cu adatom - Pt potential difference
plt.annotate(s='', xy=(1.02,1E-10), xytext=(0.61,1E-10), arrowprops=dict(arrowstyle='<->'))
ax.text(0.69,3E-10,'410 meV',color='k')

plt.ylabel(ur"log$_{10}$($i$ / $\mu$A cm$^{-2}$)")

ax2 = ax.twiny()
ax2.set_xticks(np.arange(-0.2, 1.8, step=0.2))
ax2.set_xlim([-0.2, 1.7])
ax2.set_xlabel(ur"$E$ / V$_{\rm RHE}$")
ax.set_xticks(np.arange(-0.13, 1.87, step=0.2))
ax.set_xticklabels(np.arange(-0.9, 1.1, step=0.2))
ax.set_xlabel(ur"$E$ / V$_{\rm SHE}$")

ax.text(0.17,3E-13,'Pt(111)',color='g')
ax.text(-0.11,3E-12,'Cu(111)',color='r')
ax.text(-0.08,1E-4,'Cu adatom',color='b')
#ax.text(0.2,1E2,'exp.',color='k')

plt.subplots_adjust(bottom=0.1, top=0.9, right=0.99, left=0.11)
plt.savefig('Tafel.png')

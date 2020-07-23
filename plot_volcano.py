from catmap import ReactionModel
import matplotlib.pyplot as plt
import numpy as np
from catmap import analyze
from ase.units import _e

nelectrons = 2
ACu = (3.61E-8/np.sqrt(2.))**2 * np.sqrt(3)/2.

mkm_file = 'Volcano.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables += ['production_rate']
model.run()

fig = plt.figure(figsize=(3.5,2.5))
ax = fig.add_subplot(111)

vm = analyze.VectorMap(model)
rate_map = model.production_rate_map
for res in rate_map:
    res[1][0] *= nelectrons*_e*1E6/ACu
vm.production_rate_map = rate_map
vm.plot_variable = 'production_rate'
vm.include_labels = ['CO2_g']
vm.log_scale = True #rates should be plotted on a log-scale
vm.min = 1e-20 #minimum rate to plot
vm.max = 1e6 #maximum rate to plot

vm.descriptor_labels = [ur'$\Delta E^{\rm CO}$ / eV', ur'$\Delta E^{\rm OH}$ / eV']
vm.colorbar = True
vm.colorbar_label=ur"log$_{10}$($i$ / $\mu$A cm$^{-2}$)"

vm.plot(ax_list=[ax])

#Pt
xp = -1.4130
yp = 0.5629
ax.plot([xp],[yp],'og')
ax.text(xp-0.05,yp+0.05,'Pt(111)')

#Cu
xp = -0.4782
yp = -0.1539
ax.plot([xp],[yp],'or')
ax.text(xp-0.35,yp+0.05,'Cu(111)')

#Cu adatom
xp = -0.7853
yp = 0.2046
ax.plot([xp],[yp],'ob')
ax.text(xp-0.3,yp+0.05,'Cu adatom')

ax.text(-1.53,-0.2,ur'-0.40 V$_{\rm SHE}$',color='w',size=14)

ax.set_title('')
ax.set_xticks([-1.4130,-1.4130+0.5,-1.4130+1.0])
ax.set_xticklabels([0,0.5,1.0])
ax.set_yticks([0.5629-0.5,0.5629])
ax.set_yticklabels([-0.5,0.])
ax.axis('equal')
ax.axis([-1.6, -0.3, -0.3, 0.8])

plt.subplots_adjust(bottom=0.165, top=0.95, right=0.83, left=0.195)

fig.savefig('Volcano.png')


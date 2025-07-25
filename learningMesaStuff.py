import mesa_data as mr
import mkipp
import kipp_data
import matplotlib.pyplot as plt
import numpy as np
import os

#create mesa reader object

h = mr.mesa_data('LOGS/accretion_e-5_LOGS/history.data')

# Get list of valid profile files
profile_dir = 'LOGS/accretion_e-5_LOGS/'
profile_files = sorted([
    os.path.join(profile_dir, f) 
    for f in os.listdir(profile_dir) 
    if f.startswith('profile') and f.endswith('.data')
])
profile_files = np.sort(profile_files)
#create kipp args object
k = mkipp.Kipp_Args(history_paths = ['LOGS/accretion_e-5_LOGS/history.data'],
                    logs_dirs = ['LOGS/accretion_e-5_LOGS/'],
                    profile_paths = profile_files,
                    xaxis= 'star_age',
                    yaxis= 'radius')

fig,ax = plt.subplots(nrows = 1,
                      ncols = 2,
                      figsize = (10,4),
                      layout = 'constrained')
#add sublots_adjust to add whitespace
mkipp.kipp_plot(kipp_args = k,
                axis = ax[0])


#testing out plotting a hr diagram using 
#data from mesa reader and matplotlib
lumin = h.get('log_L') #getting log luminosity from history data
temps = h.get('log_Teff') #getting log temperature from hist data
#dir(plt)
#starting to plot hr
ax[1].plot(temps, lumin, color = 'blue', linewidth = 3)
ax[1].set_xlabel('Log_Teff')
ax[1].set_ylabel('Log_L')
ax[1].invert_xaxis()
#plt.savefig('accretion_10-5.png')
#plt.clf()
plt.show()

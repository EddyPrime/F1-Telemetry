"""Gear shifts TRACES
=======================

Plot which gear is being used at which point of the track
"""

##############################################################################
# Import FastF1 and load the data

import fastf1

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np


fastf1.Cache.enable_cache('../doc_cache')  # replace with your cache directory

session = fastf1.get_session(2021, 'Spanish Grand Prix', 'Qualifying')
session.load()

lap = session.laps.pick_fastest()
tel = lap.get_telemetry()
# sphinx_gallery_defer_figures

fig, ax = plt.subplots()
ax.plot(tel['Distance'], tel['nGear'])

ax.set_xlabel('Distance in m')
ax.set_ylabel('Gear')

#ax.legend()

plt.suptitle(f"Gear Shifts\n "
             f"{session.event['EventName']} {session.event.year} Qualifying")

plt.show()

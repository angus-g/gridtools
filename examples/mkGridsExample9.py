#!/usr/bin/env python

# Open the land mask editor for an existing
# ROMS grid

import os, sys
from gridtools.gridutils import GridUtils
from gridtools.grids import roms
from pyproj import Proj
import cartopy.crs as ccrs

# Set a place to write files
os.environ["PYROMS_GRIDID_FILE"] = "/import/AKWATERS/jrcermakiii/configs/Arctic6/roms/gridid.txt"
wrkDir = '/import/AKWATERS/jrcermakiii/configs/zOutput'
inputDir = os.path.join(wrkDir, 'INPUT')

grd = GridUtils()

romsObj = roms.ROMS()
romsGrd = romsObj.get_ROMS_grid('ARCTIC6')

PROJSTRING = "+proj=stere +lon_0=160.0"
map = Proj(PROJSTRING, preserve_units=False)
crs = ccrs.Stereographic(central_latitude=90.0, central_longitude=160.0)
#map = cartopy.crs.NorthPolarStereo(central_longitude=160.0)

#breakpoint()
plotObj = romsObj.edit_mask_mesh(romsGrd.hgrid, proj=map, crs=crs)

'''
 (lon)
[[ 131.90054918  131.95830076  132.01611442 ... -159.16478639
  -159.12234478 -159.07996543]
 [ 131.86969889  131.92751306  131.98536865 ... -159.12805839
  -159.08561678 -159.04322572]
 [ 131.83878634  131.8966422   131.95453963 ... -159.09127986
  -159.04883042 -159.00643165]
 ...
 [  13.65039644   13.58628753   13.52206311 ...  -67.13567871
   -67.17843869  -67.22113252]
 [  13.60782738   13.54371847   13.4795344  ...  -67.08960332
   -67.13236844  -67.17506227]
 [  13.56531342   13.50126481   13.43712128 ...  -67.04359923
   -67.08636434  -67.12906585]]
   (lat)
[[46.30970955 46.33097973 46.35221283 ... 39.89697169 39.86878072
  39.84060048]
 [46.34958047 46.37088238 46.39214283 ... 39.92952203 39.90133106
  39.87311507]
 [46.389451   46.41078035 46.43206822 ... 39.96208387 39.93386453
  39.90562017]
 ...
 [52.36683799 52.39283444 52.41882112 ... 44.73025274 44.6974876
  44.66473208]
 [52.32766945 52.3536659  52.37961743 ... 44.69984059 44.66710715
  44.63435163]
 [52.28852586 52.31448215 52.34039861 ... 44.66943333 44.63669989
  44.60398325]]

  (x)
[[34681742.35534516 34688164.03540023 34694592.61821859 ...
   2316768.95858781  2321488.24805473  2326200.61372873]
 [34678311.96129423 34684740.60110116 34691173.84523138 ...
   2320852.92342532  2325572.21289224  2330285.88108898]
 [34674874.64363986 34681307.91916076 34687745.8170721  ...
   2324942.50773207  2329662.66794807  2334377.19355566]
 ...
 [21532931.48692559 21525802.90473083 21518661.47876239 ...
  12549934.01741877 12545179.32658853 12540431.99100027]
 [21528198.02620061 21521069.44400584 21513932.50453996 ...
  12555057.36404173 12550302.10250697 12545554.76691871]
 [21523470.69183435 21516348.81470634 21509216.38258372 ...
  12560172.78339321 12555417.52185845 12550669.33286248]]
  (y)
[[65370399.42068778 65373824.04711322 65377244.03216704 ...
  64392357.21470809 64388272.16414933 64384190.34690855]
 [65376819.96856485 65380252.20687301 65383679.09996624 ...
  64397076.05659151 64392989.06517298 64388900.12996078]
 [65383245.14079945 65386684.31244529 65390118.1357889  ...
  64401798.8124599  64397705.7611507  64393610.77190327]
 ...
 [66405847.12696747 66410582.64207248 66415319.16630597 ...
  65119715.09729563 65114588.21069191 65109465.727423  ]
 [66398717.44081534 66403448.76009569 66408174.68095139 ...
  65114956.29533788 65109837.05590197 65104717.25657883]
 [66391598.60209461 66396318.43295664 66401033.78403042 ...
  65110200.75647804 65105084.20187449 65099973.15592262]]
'''


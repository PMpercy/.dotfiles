#from Darker import MaterialDarker
#from DeepOcean import MaterialOcean
#from Material import MaterialGeneral
from .Material.Material import *
from .Material.Darker import *
from .Material.DeepOcean import *

#material = 'Darker'
### Select theme
# Material, OneDark
#theme = 'Material'

#Select sub theme of  material
#DeepOcean, Darker
material = 'Darker'



focus = MaterialGeneral[8]
active = MaterialGeneral[7] #white
urgent = MaterialGeneral[1] #red
inactive = MaterialGeneral[9]
color1 = MaterialGeneral[2] #green
color2 = MaterialGeneral[5]
color3 = MaterialGeneral[3] #yellow
color4 = MaterialGeneral[4] #blue
color5 = MaterialGeneral[5] #magenta
color6 = MaterialGeneral[6] #cyan
color7 = MaterialGeneral[10]
color8 = MaterialGeneral[11]
color9 = MaterialGeneral[12]

if material == 'Darker':
    bg = MaterialDarker[0]
    fg = MaterialDarker[1]
    text = MaterialDarker[2]
elif material == 'DeepOcean':
    bg = MaterialOcean[0]
    fg = MaterialOcean[1]



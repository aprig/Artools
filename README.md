# Artools

## What is it about? 

Artools is just some usefull scripts to compute interannual anomalies of a timeserie and take subdomains of a large dataset.

## Example data_sub.py
```bash
import xarray as xr
import numpy as np
import Artools.my_functions as Atools
from pydap.client import open_url
import matplotlib.pyplot as plt
```
### Load SST data
```bash
sst = xr.open_dataset('https://icdc.cen.uni-hamburg.de/thredds/dodsC/reynolds_sst_anomalies_1982_2001',
                      engine="pydap")
```

### Take subdomain
```bash
sst_sub = Atools.data_sub(sst,0,90,-30,10)
```
### Plot maps
```bash
f,ax = plt.subplots(1,2,figsize=[10,5])
cmap = plt.cm.RdYlBu_r
bounds = np.arange(-2,2.2,0.2)
ax=ax.ravel()

ax[0].set_title('All domain')
ax[0].contourf(sst.lon,sst.lat,sst.anomaly[0,:,:],cmap=cmap,levels=bounds)


ax[1].set_title('Subdomain')
ax[1].contourf(sst_sub.lon,sst_sub.lat,sst_sub.anomaly[0,:,:],cmap=cmap,levels=bounds)
```


![data sub function ](notebooks/example_subdomain.png)



## Installation 
Create an environment :
```bash
conda create -n Artools_env
```


Then install Artools : 
```bash
source activate Artools_env
pip install git+https://github.com/aprig/Artools.git
```

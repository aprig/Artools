def ano_norm_tc(ds):
    
    '''Compute the anomalies by removing the monthly means. 
    The anomalies are normalized by their corresponding month.
    
    Parameters
    ----------
    
    ds : xarray_like
    Timeserie or 3d field.
    
    Returns
    -----------
    
    ano : xarray_like
    Returns the anomalies of var relative the climatology.
    
    ano_norm : xarray_like
    Returns the anomalies of var relative the climatology normalized by the standard deviation.
    
    '''
    
    
    clim     = ds.groupby('time_counter.month').mean('time_counter')
    clim_std = ds.groupby('time_counter.month').std('time_counter')
    ano      = ds.groupby('time_counter.month') - clim
    ano_norm = xr.apply_ufunc(lambda x, m, s: (x - m) / s,
                                    ds.groupby('time_counter.month'),
                                    clim, clim_std)
    
    return ano, ano_norm

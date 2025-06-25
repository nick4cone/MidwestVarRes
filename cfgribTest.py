import xarray as xr
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# path = "/glade/derecho/scratch/nforcone/HRRR_data/hrrr/20200810/hrrr.t00z.wrfsfcf00.grib2"
# path = "/glade/derecho/scratch/nforcone/HRRR_testing/hrrr/20200810/hrrr.t00z.wrfsfcf00.grib2"
path = "/glade/derecho/scratch/nforcone/HRRR_google/hrrr/20200810/hrrr.t00z.wrfsfcf00.grib2"

ds_sfc_instant = xr.open_dataset(path, engine='cfgrib', backend_kwargs={'filter_by_keys': {'stepType': 'instant', 'typeOfLevel': 'surface'}})
print(ds_sfc_instant.data_vars)

ds_isobaricInhPa = xr.open_dataset(path, engine='cfgrib', filter_by_keys={'typeOfLevel': 'hybrid'})
print(ds_isobaricInhPa.data_vars)

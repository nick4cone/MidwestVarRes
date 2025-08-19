from vapor import session, renderer, dataset
from vapor.animation import Animation
import os
import uxarray as ux

ses = session.Session()
print(dataset.Dataset.GetDatasetTypes())

data_file = "/glade/derecho/scratch/nforcone/CAM_6_4_025_20240829_topo_bw_dry_ne0MIDWESTne30x32_ne0MIDWESTne30x32/run/CAM_6_4_025_20240829_topo_bw_dry_ne0MIDWESTne30x32_ne0MIDWESTne30x32.cam.h0i.0001-01-06-13014.nc"
data = ses.OpenDataset(dataset.CF, [data_file])

print("Data Variables:")
vars = ["U", "T"]
for var in data.GetDataVarNames():
    if var in vars:
        print(f" {var}")
        print(f"    Time Varying: False")
        print(f"    Dimensionality:", data.GetVarGeometryDim(var))
        print(f"    Coordinates:", data.GetVarCoordVars(var, True))
        print("     Data Range:", data.GetDataRange(var))
import uxarray as ux
import os

grid_path = "/glade/u/home/nforcone/MidwestVarRes/midwest-06-16-2025_edit22_ESMF.nc"
data_dir = "/glade/derecho/scratch/nforcone/CAM_6_4_025_20240829_topo_bw_dry_ne0MIDWESTne30x32_ne0MIDWESTne30x32/run"

data_paths = [
    os.path.join(data_dir, "CAM_6_4_025_20240829_topo_bw_dry_ne0MIDWESTne30x32_ne0MIDWESTne30x32.cam.h0i.0001-01-01-03618.nc"),
    os.path.join(data_dir, "CAM_6_4_025_20240829_topo_bw_dry_ne0MIDWESTne30x32_ne0MIDWESTne30x32.cam.h0i.0001-01-06-13014.nc")
]

uxds = ux.open_mfdataset(grid_path, data_paths)
print('read')
uxds.to_netcdf("/glade/derecho/scratch/nforcone/CAM_6_4_025_20240829_topo_bw_dry_ne0MIDWESTne30x32_ne0MIDWESTne30x32_output.nc")
print("done")
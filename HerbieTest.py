from herbie import Herbie
from herbie.toolbox import EasyMap, pc
from herbie import paint
import warnings

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

warnings.filterwarnings("ignore", category=FutureWarning)

H = Herbie(
    "2020-08-10",
    model="hrrr",
    product="nat",
    fxx=0,
)
print(H.inventory("t"))
print(H.PRODUCTS)
H.download(verbose=True)
# ds = H.xarray("TMP:2 m above")
# ax = EasyMap("50m", crs=ds.herbie.crs, figsize=[10, 8]).BORDERS().STATES().ax

# p = ax.pcolormesh(
#     ds.longitude,
#     ds.latitude,
#     ds.t2m - 273.15,
#     transform=pc,
#     **paint.NWSTemperature.kwargs2,
# )
# plt.colorbar(
#     p,
#     ax=ax,
#     orientation="horizontal",
#     pad=0.01,
#     shrink=0.8,
#     **paint.NWSTemperature.cbar_kwargs2,
# )

# ax.set_title(
#     f"{ds.model.upper()}: {H.product_description}\nValid: {ds.valid_time.dt.strftime('%H:%M UTC %d %b %Y').item()}",
#     loc="left",
# )
# ax.set_title(ds.t2m.GRIB_name, loc="right")
# plt.show()
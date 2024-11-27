import pandas as pd

from hydtank import build_hydtank_from_dataset, Dataset, TIME_SERIES, PRECIPITATION, EVAPOTRANSPIRATION, DISCHARGE

df = pd.read_csv('data.csv')

_dataset = Dataset(
    time_series=df[TIME_SERIES].tolist(),
    precipitation=df[PRECIPITATION].tolist(),
    evapotranspiration=df[EVAPOTRANSPIRATION].tolist(),
    discharge=df[DISCHARGE].tolist(),
)

tank = build_hydtank_from_dataset(
    open('NuiLe_GiaUi.basin').read(),
    _dataset
)

tank2 = tank.copy()

print(tank == tank2)
print(tank.get_basin_def_by_name('NuiLe') == tank2.get_basin_def_by_name('NuiLe'))
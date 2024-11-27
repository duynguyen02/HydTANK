from hydtank import build_hydtank
from hydtank.bsd_junction import Junction
from hydtank.bsd_reach import Reach
from hydtank.bsd_sink import Sink
from hydtank.bsd_subbasin import Subbasin
from hydtank.parameters import SubbasinParameters, ReachParameters

with open('data.csv') as file1, open('NuiLe_GiaUi.basin') as file2:
    tank = build_hydtank(
        file1.read(),
        file2.read()
    )

nui_le: Subbasin = tank.get_basin_def_by_name('NuiLe')
giaui_local: Subbasin = tank.get_basin_def_by_name('GiaUi_Local')
reach1: Reach = tank.get_basin_def_by_name('Reach1')
junction1: Junction = tank.get_basin_def_by_name('Junction1')
sink: Sink = tank.get_basin_def_by_name('Sink1')

tank.optimize([nui_le, reach1, giaui_local])

tank.plot_basin_network().save('GiaUi_NuiLe_Basin_Network.png')
tank.plot_headwater_q().save('GiaUi_NuiLe_Headwater.png')
tank.plot_q().save('GiaUi_NuiLe_Qsim.png')
tank.plot_subbasin(nui_le).save('GiaUi_NuiLe_NuiLe_Subbasin.png')
tank.plot_subbasin(giaui_local).save('GiaUi_NuiLe_GiaUiLocal_Subbasin.png')

print(reach1.parameters)
print(nui_le.parameters)
print(giaui_local.parameters)
print(nui_le.stats)

params = reach1.parameters.copy()
params.k = 0.9235288521736096
tank.reconfig_parameters(reach1.name, params)
tank.reconfig_parameters(reach1.name, ReachParameters())

tank.reconfig_parameters(nui_le.name, SubbasinParameters())

tank.to_dataframe().to_csv('GiaUi_NuiLe_TANK.csv', index=False)

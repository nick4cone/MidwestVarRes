# MidwestVarRes
## Mesh
```
<domain name="ne0np4.MIDWEST.ne30x32">
  <nx>316010</nx> <ny>1</ny>
  <mesh driver="nuopc">/glade/u/home/nforcone/MidwestVarRes/midwest-06-16-2025_edit22_ESMF.nc</mesh>
  <desc>Spectral Elem 1-deg grid with a 1/32 deg refined region over the Midwestern United States</desc>
</domain>
```
```
<model_grid alias="ne0MIDWESTne30x32_ne0MIDWESTne30x32" not_compset="_POP">
  <grid name="atm">ne0np4.MIDWEST.ne30x32</grid>
  <grid name="lnd">ne0np4.MIDWEST.ne30x32</grid>
  <grid name="ocnice">ne0np4.MIDWEST.ne30x32</grid>
  <mask>tx0.1v2</mask>
</model_grid>
```
## CAM_6_4_025 Topo BW Cases
| case name                                                                     | STOP_OPTION | STOP_N     | sim time |se_tstep      | n nodes | runtime | se_nu_top | ATM_NCPL | n lev |
| --                                                                            | --          | --         | --       |--            | ------- | --      | --        | --       | --    |
| StormSPEED.stormspeed_refmesh_FHISTC_LTso_ne0MIDWESTne30x32_ne0MIDWESTne30x32 | nsteps      | 15         | 24 min   |8             | 8       | 0.15 hr | 1e4       | 900      | 58    |
## Atmosphere initial condition
[Herbie: Retrieve NWP Model Data](https://herbie.readthedocs.io/en/latest/index.html)

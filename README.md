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
<model_grid alias="ne16np4.WEST_ATLANTIC.ne16x2" not_compset="_POP">
  <grid name="atm">ne16np4.WEST_ATLANTIC.ne16x2</grid>
  <grid name="lnd">ne16np4.WEST_ATLANTIC.ne16x2</grid>
  <grid name="ocnice">ne16np4.WEST_ATLANTIC.ne16x2</grid>
  <mask>tx0.1v2</mask>
</model_grid>
```

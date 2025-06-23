# MidwestVarRes
## Mesh
```
<domain name="ne16np4.WEST_ATLANTIC.ne16x2">
  <nx>25886</nx> <ny>1</ny>
  <mesh driver="nuopc">/glade/u/home/nforcone/Sandy_ESMF.nc</mesh>
  <desc>NCF - ne16np4.WEST_ATLANTIC.ne16x2 is a Spectral Elem 2-deg grid with a 1/2 deg refined region over the West Atlantic</desc>
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

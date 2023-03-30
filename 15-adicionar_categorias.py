import pandas as pd

data = pd.read_csv("csv/formatted_data.csv")
models = data.Modelo.unique()

print(models)

modelos = [
  'RS Q3 2.5 TFSI Quattro S-tronic 5p',
  'Q3 2.0 TFSI Quat. 170/180cv S-tronic 5p',
  'Q3 2.0 TFSI Quat. 211/220cv S-tronic 5p',
  'X1 XDRIVE 28i Sport 2.0 ActiveFlex Aut.' 'Tiggo 2.0 16V Aut. 5p',
  'Tiggo 2.0 16V Mec. 5p' 'Classic ADVANTAGE 1.0 VHC FlexPower 4p',
  'Classic Life/LS 1.0 VHC FlexP. 4p',
  'COBALT LT 1.8 8V Econo.Flex 4p Aut.',
  'COBALT LT 1.8 8V Econo.Flex 4p Mec.',
  'COBALT LTZ 1.8 8V Econo.Flex 4p Mec.',
  'TRACKER LTZ 1.8 16V Flex 4x2 Aut.',
  'SPIN ACTIV 1.8 8V Econo. Flex 5p Aut.',
  'ONIX HATCH LT 1.4 8V FlexPower 5p Aut.',
  'ONIX HATCH LTZ 1.4 8V FlexPower 5p Aut.',
  'ONIX HATCH LT 1.4 8V FlexPower 5p Mec.',
  'PRISMA Sed. LT 1.4 8V FlexPower 4p Aut.',
  'PRISMA Sed. LTZ 1.4 8V FlexPower 4p Aut.',
  'PRISMA Sed. ADVANT. 1.0 8V FlexPower 4p',
  'SPIN ADVANTAGE 1.8 8V Econo.Flex 5p Aut.',
  'SPIN ACTIV 1.8 8V Econo. Flex 5p Mec.',
  'SPIN ADVANTAGE 1.8 8V Econo.Flex 5p Mec.',
  'CRUZE LT 1.8 16V FlexPower 4p Aut.',
  'CRUZE LTZ 1.8 16V FlexPower 4p Aut.',
  'CRUZE LT 1.8 16V FlexPower 4p Mec.',
  'AIRCROSS Exclusive 1.6 Flex 16V 5p Aut.',
  'AIRCROSS Exclusive 1.6 Flex 16V 5p Mec.',
  'C3 Picasso Excl. 1.6 Flex 16V 5p Aut.',
  'C4 LOUNGE Exclusive 1.6 Turbo 4p Aut.',
  'C4 LOUNGE Origine 2.0 Flex 4p Mec.',
  'C4 LOUNGE Tendance 2.0 Flex 4p Mec.',
  'UNO ATTRACTIVE 1.0 Fire Flex 8V 5p',
  'Idea Adv./ Adv.LOCK.Dualogic 1.8 Flex 5p',
  'Idea ATTRACTIVE 1.4 Fire Flex 8V 5p',
  'Idea Advent./ Adv.LOCKER 1.8 mpi Flex 5p',
  'Idea ELX 1.4 mpi Fire Flex 8V 5p',
  'Grand Siena ESSEN. ITALIA Dual. 1.6 Flex',
  'Grand Siena ATTRAC. 1.4 EVO F.Flex 8V',
  'Grand Siena ESSEN.SUBLIME 1.6 Flex',
  'Grand Siena TETRAFUEL 1.4 Evo F. Flex 8V',
  'LINEA ESSENCE 1.8 Flex 16V 4p',
  'EcoSport FREESTYLE 2.0 16V Flex 5p Aut.',
  'EcoSport SE 2.0 16V Flex 5p Aut.',
  'EcoSport XLT 2.0/ 2.0 Flex 16V 5p Mec.',
  'EcoSport SE 1.6 16V Flex 5p Mec.',
  'Ka 1.0 SE/SE Plus TiVCT Flex 5p',
  'Fiesta 1.6 16V Flex Aut. 5p',
  'Fiesta Sedan 1.6 16V Flex Aut.',
  'Fiesta 1.6 16V Flex Mec. 5p',
  'Fiesta 1.5 16V Flex Mec. 5p',
  'Ranger Limited 3.2 20V 4x4 CD Aut. Dies.',
  'Ranger TROPIVAN 3.2 20V 4X4 TB Dies.Aut.',
  'Ranger XLS 3.2 20V 4x4 CD Diesel Mec.',
  'Ranger XLS 2.2 4x4 CD Diesel Mec.',
  'CITY Sedan DX 1.5 Flex 16V Aut.',
  'CITY Sedan EX 1.5 Flex 16V 4p Aut.',
  'CITY Sedan DX 1.5 Flex 16V Mec.',
  'Fit DX 1.5 Flexone 16V 5p Aut.',
  'Fit CX 1.4 Flex 16V 5p Aut.',
  'Fit DX 1.5 Flexone 16V 5p Mec.',
  'Civic Sedan EXR 2.0 Flexone 16V Aut. 4p',
  'Civic Coupe Si 2.4 16V 206cv Mec. 2p',
  'HB20 C.Style/C.Plus 1.6 Flex 16V Aut.',
  'HB20 Copa do Mundo 1.6 Flex 16V Aut.',
  'HB20 C./C.Plus/C.Style 1.6 Flex 16V Mec.',
  'HB20 Copa do Mundo 1.0 Flex 12V Mec.',
  'HB20S Copa do Mundo 1.6 Flex 16V Aut.',
  'HB20S Premium 1.6 Flex 16V Aut. 4p',
  'HB20S C.Plus/C.Style 1.6 Flex 16V Mec.4p',
  'HB20S Copa do Mundo 1.0 Flex 12V Mec.',
  'ix35 GLS 2.0 16V 2WD Flex Aut.',
  'Tucson 2.0 16V Mec.',
  'COMPASS SPORT 2.0 16V 156cv 5p',
  'SOUL 1.6/ 1.6 16V FLEX Aut.',
  'Sportage 2.0 16V Aut.',
  'Cerato 1.6 16V Flex Aut.',
  'Range Rover EVOQUE Pure Tech 2.0 Aut. 5p',
  'X60 1.8 16V 128cv 5p Mec.',
  'CLA-200 Urban 1.6 TB 16V/Flex Aut.',
  'CLA-200 Vision 1.6 TB 16V Flex Aut.',
  'CLA-250 Sport 4MATIC 2.0 16V 211cv Aut.',
  'GLA 200 Vis. Black Ed. 1.6 TB 16V Aut.',
  'CLA-200 First Edition 1.6 TB 16V Aut.',
  'COOPER Countryman S 1.6 Aut.',
  'COOPER Countryman S ALL4 1.6 Aut.',
  'L200 Triton HPE 3.5 CD V6 24V Flex Aut.',
  'L200 Triton Savana 3.2 CD TBI Dies. Mec.',
  'L200 Triton HLS 2.4 Flex 16V CD Mec.',
  'ASX 2.0 16V 160cv Mec.',
  'OUTLANDER 3.0/ GT 3.0 V6 Aut.',
  'OUTLANDER 2.0 16V 160cv Aut.',
  'ASX 2.0 16V 160cv Aut.',
  'ASX 2.0 16V 4x4 160cv Aut.',
  'Lancer 2.0 16V 160cv Aut.',
  'Lancer GT 2.0 16V 160cv Aut.',
  'Lancer 2.0 16V 160cv Mec.',
  'Frontier SV AT.CD 4x4 2.5 TB Diesel Mec.',
  'VERSA SL 1.6 16V Flex Fuel 4p Mec.',
  'VERSA SV 1.6 16V Flex Fuel 4p Mec.',
  'Sentra S 2.0/ 2.0 Flex Fuel 16V Mec.',
  '208 Active Pack 1.6 Flex 16V 5p Aut.',
  '208 Griffe 1.6 Flex 16V 5p Aut.',
  '208 Griffe 1.6 Flex 16V 5p Mec.',
  'LOGAN Authentique Hi-Flex 1.0 16V 4p',
  'LOGAN Dyna. EasyR Hi-Flex 1.6 8V',
  'DUSTER Dynamique 2.0 Flex 16V Aut.',
  'DUSTER TECHROAD 2.0 Hi-Flex 16V Aut.',
  'DUSTER Dynamique 2.0 Hi-Flex 16V Mec.',
  'DUSTER 1.6 Hi-Flex 16V Mec.',
  'FLUENCE Sed. Dyn. Plus 2.0 16V FLEX Aut.',
  'FLUENCE Sed. Dynamique 2.0 16V FLEX Aut.',
  'FLUENCE Sed. Dynamique 2.0 16V FLEX Mec.',
  'ACTYON SPORTS 2.0 16V 155cv Diesel',
  'Hilux CD SR 4x2 2.7 16V/2.7 Flex Aut.',
  'Hilux CD D4-D 4x4 3.0 TDI Dies. Mec.',
  'Hilux CD 4x4 2.7 16V Flex Mec.',
  'RAV4 2.5 4x4 16V Aut.',
  'RAV4 2.0 4x2 16V Aut.',
  'Corolla ALTIS 2.0 Flex 16V Aut.',
  'Corolla GLi 1.8 Flex 16V Mec.',
  'Corolla XLi 1.6 16V 110cv Mec.',
  'ETIOS CROSS 1.5 Flex 16V 5p Mec.',
  'ETIOS PLATINUM 1.5 Flex 16V 5p Mec.',
  'ETIOS X 1.3 Flex 16V 5p Mec.',
  'PRIUS Hybrid 1.8 16V 5p Aut.',
  'CROSSFOX 1.6 Mi Total Flex 8V 5p',
  'CROSSFOX I MOTION 1.6 Mi T. Flex 8V 5p',
  'Gol (novo) 1.0 Mi Total Flex 8V 4p',
  'Gol (novo) 1.6 Mi Total Flex 8V 4p',
  'up! black/white/red 1.0 T. Flex 12V 5p',
  'up! black/white/red I MOTION 1.0 Flex 5p',
  'up! cross 1.0 T. Flex 12V 5p',
  'up! cross I MOTION 1.0 T.Flex 12V 5p',
  'AMAROK High.CD 2.0 16V TDI 4x4 Dies. Aut',
  'AMAROK SE CD 2.0 16V TDI 4x4 Diesel',
  'AMAROK Trendline CD 2.0 16V TDI 4x4 Dies',
  'SPACEFOX 1.6/ 1.6 Trend Total Flex 8V 5p',
  'SPACEFOX COMFORTLINE 1.6 Mi T.Flex 8V 5p',
  'Saveiro 1.6 Mi/ 1.6 Mi Total Flex 8V',
  'VOYAGE Trendline 1.0 T.Flex 8V 4p',
  'VOYAGE Comfortline 1.0 T.Flex 8V 4p',
  'SPACEFOX SPORTLINE/HIGHLINE 1.6 T.Flex',
  'SPACEFOX TREND I MOTION 1.6 T. Flex 8V',
  'Golf Comfortline 1.4 TSI 140cv Aut.',
  'Golf Comfortline 1.4 TSI 140cv Mec.',
]
# TR-1um Open Source PDK project (NDA-free 1um CMOS PDK)

The TR-1um Open Source PDK project, a new NDA-Free PDK ecosystem in Japan, is supported by the non-profit OpenSUSI (Open Source Utilized Silicon Initiatives). [**Tokai Rika**](https://tr-semicon.tokai-rika.co.jp/foundry-service) approved to open their PDK and manufacture the data, which is designed by the Open Source EDA tool at Tokai Rika's facility.

The original document and the DRC/LVS runsets are deliverable as-is by Tokai Rika. Yet, the OpenSUSI proposes new PDK package development based on the Drawing layer + MDP (Mask Development Preparation) procedure. Please see [Manifest](Document/Manifesto.md).

**We welcome your feedback and advice.** We are also planning the Shuttle service once any budgets are in place.

# TR-1um Directory Structure 
```
TR-1um -- openIP62 -- AnagixLoader
       |           +- IP62
       +- GDSII
       +- Schematic
       +- STDLIB ----- extracted 
       |
       +- libs.tech -- klayout
       |            +- xschem 
       |            +- ngspice
       +- Tools
       +- Document
```

Since the original DRC cannot check a full-custom layout, such as Standard Cell development, except for PCEL use, new DRC runset development is ongoing under the tech/drc directory. Additionally, the [Tutorial: How to make DRC runset for KLayout](Document/Tutorial_DRC.md) and the [Tutorial: How to make LVS runset for KLayout](Document/Tutorial_LVS.md) project are also ongoing; feel free to join as always. We welcome your feedback on the DRC result and bug report as well.

## openIP62 (AS-IS)
The directory contains the original PDKs provided by [**Tokai Rika**](https://tr-semicon.tokai-rika.co.jp/foundry-service). It includes two main subdirectories: **AnagixLoader** and **IP62**. Detailed documentation and installation manuals (in Japanese) can be found in: **openIP62/IP62/Technology/doc**

## GDSII
Final GDSII data for 2025/09/24-25 OSS hands-on seminar on Kyushu university.

## Schematic
Final schematic data for 2025/09/24-25 OSS hands-on seminar on Kyushu university.

## STDLIB
Extracted spice files from **openIP62/IP62/Basic/libraries/xxx.gds** by LVS operation which are including AD/AS/PD/PS information.

## libs.tech
**Try to align this to IIC-OSIC-TOOLS pdk directory** 

Currently working directry for Open Source Silicon community to exchange new idea and **drc** and **lvs** directories are active for KLayout DRC/LVS runset development. **TR-1um.lyp** is KLayout layer file for both **DRC** and **LVS**.
Also Xschem symbol library development is ongoing. 

### Contents
|                 | Description |
| -------         | ---------   |
| - **klayout**   | directory contain KLayout (DRC/LVS/PCells)
| - **ngspice**   | directory is tentativly a symbolic link to the originals.
| - **xschem**    | directory contain symbol library which under development.

## Tools

- Tools/IP62_to_TR-1um.py  INPUT_TR62.gds OUTPUT_TR-1um.gds

       IP62(MASK Layers) to TR-1um(Drawing Layers) conversion Python script, which is hierachically execute it bottom to top.

- Tools/DRC_csv2py.py rules_def.py

       TR-1um_DR(Design Rule Table) to Python Class file script.

- Tools/DRC_csv2drc.py run.drc

       TR-1um_DR(Design Rule Table) to KLayout DRC runset file script.

## Document

[Manifesto: PDK renewal for TR-1um technology](Document/Manifesto.md)

[New Desgin Rule Summary Manual](Document/TR-1um_DRC_summary.pdf) (PDF)

[Design Rule Table for Drawing Layers](Document/TR-1um_Drawing_Layer_DR_Table.xlsx) (XLS)

[Drawing Layer vs Mask Layer Table](Document/TR-1um_GDSII_Table.xlsx) (XLS)

[Tutorial: How to make DRC runset for KLayout](Document/Tutorials/Tutorial_DRC.md)

[Tutorial: How to make LVS runset for KLayout](Document/Tutorials/Tutorial_LVS.md) 

[Tutorial: How to make PCell python script for KLayout](Document/Tutorials/Tutorial_PCell.md) 

[Layers and Design steps: Layers reenewal for TR-1um technology](Document/Drawing_vs_Mask.md)

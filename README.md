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
**Try to alighn this to IIC-OSIC-TOOLS pdk directory** 

Currently working directry for Open Source Silicon community to exchange new idea and **drc** and **lvs** directories are active for KLayout DRC/LVS runset development. **TR-1um.lyp** is KLayout layer file for both **DRC** and **LVS**.
Also Xschem symbol library development is ongoing. 

- **klayout/drc** directory contain DRC runset files.
- **klayout/lvs** directory contain LVS runset files.
- **ngspice** directory is a symbolic link to the originals.
- **xschem** directory contain symbol library which under development.

## Tools
Preserved.

## Document

[Tutorial: How to make DRC runset for KLayout](Document/Tutorial_DRC.md)

[Tutorial: How to make LVS runset for KLayout](Document/Tutorial_LVS.md) 


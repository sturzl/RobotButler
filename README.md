# RobotButler
A robotic arm that serves various drinks! Made for a robotics and tech event hosted by Wayne State University and the [Detroit Autonomous Vehicle Group (DAVG)](https://davg.tech/). Creators: Yaro Shtyha and DAVG members [Marc Sturzl](https://github.com/sturzl/https://github.com/sturzl/), [Alex Polonsky](https://github.com/Sashulik) and Zikang Ma.

### Rough Outline
1. Raspi serves a website on local wifi
2. User connects to the site and sends in an order
3. Raspi calculates motion for the arm and sends control signals to the arduino over serial
4. Arduino state machine updates and begins moving the arm through the motor control boards
5. Arduino turns on the correct pump with a MOSFET
6. User's selection is poured through one of the 5 fingers

# Software

### Python libraries for inverse kinematics
- [https://github.com/uw-biorobotics/IKBT](https://github.com/uw-biorobotics/IKBT)
- [https://github.com/abr/abr_control](https://github.com/abr/abr_control)
- [https://github.com/Phylliade/ikpy](https://github.com/Phylliade/ikpy)

# Hardware
There is a simple solution and a more complex solution. The simple solution costs 40% more, but has half points of failure and MUCH simpler code. The simple solutions uses 5 pumps, the complex solution uses one pump and 10 solenoids which select the correct tubes.

| solution | # of parts | # of tubing joints | price |
| :--- | :--- | :--- | :--- |
| simple | 26 | 17 | $224 |
| complex | 40 | 39 | $160 |


### Parts common to both solutions

| part | quantity | total price |
|:-----|:-----|:-----|
| [NEMA 17 Stepper motors](https://www.ebay.com/itm/Stepper-Motor-Nema-17-SL42STH34-1504A-40mm-1-8A-78Oz-4-Lead-for-3D-Printers/202388518117?hash=item2f1f4bb4e5:g:fBIAAOSwd~Zbj4~G:rk:1:pf:0&LH_BIN=1) | 3 | $36  |
| [Check valve](https://www.usplastic.com/catalog/item.aspx?sku=64048&gclid=EAIaIQobChMI6-PswujD3gIVQ7jACh0_2ASsEAQYASABEgI4Z_D_BwE) | 5 | $6 |
| [Raspberry pi 0w](https://www.microcenter.com/product/486575/zero-w) | 1 | $5 |
| [Arduino motor shield](https://www.amazon.com/Compatible-Arduino-Duemilanove-Atomic-Market/dp/B00TMA4YSS/ref=asc_df_B00TMA4YSS/?tag=hyprod-20&linkCode=df0&hvadid=194019628201&hvpos=1o1&hvnetw=g&hvrand=13664937720553066793&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9016967&hvtargid=pla-340551339284&psc=1) | 2 | $18 |
| [Arduino](https://www.ebay.com/itm/UNO-R3-ATmega328P-16MHz-CH340-CH340G-USB-For-Arduino/302936647614?hash=item46886e67be:g:U2AAAOSwqM9b1SGS:rk:39:pf:0) | 1 | $6 |
| [vinyl tubing](https://www.homedepot.com/p/Everbilt-3-8-in-O-D-x-1-4-in-I-D-x-10-ft-PVC-Clear-Vinyl-Tube-702098/207144353) | 30' | $10 |
| [spool of 3D printer filament for arm enclosure](https://www.microcenter.com/product/485641/175mm-white-pla-3d-printer-filament---1kg-spool-(22-lbs)) | 1 | $15 |
| Plywood base that will be clamped to table | 1 | free |
| 12 v power supply @350 watts | 1 | free |
| Wifi device to send controls to raspi |  1  | free |
| Glue, screws, etc. | ∞ | free |
| **total** |  | $96 |

### Parts for simple solution

| part | quantity | total price |
|:-----|:-----|:-----|
| [Paristaltic pump](https://www.ebay.com/itm/DC-12-24V-Peristaltic-Pump-Large-Flow-Dosing-Pump-Vacuum-Aquarium-Lab-Analytical/273097535778?hash=item3f95e1b122:m:mUXje-wYDBR0DV0zzfXsCEQ:rk:10:pf:0) | 5 | $125 |
| [Logic level MOSFET](https://www.ebay.com/itm/20Pcs-IRLZ44N-PBF-Power-MOSFET-Logic-Level-N-Channel-0-022OHM-TO-220-IC-Chip-USA/173493492366?hash=item2865049a8e:rk:1:pf:0) | 5 | $3 |
| **total** |  | $128 |

### Parts for complex solution

| part | quantity | total price |
|:-----|:-----|:-----|
| [Solenoid valve](https://www.ebay.com/itm/DC12V-Normally-Closed-Type-Electronic-Control-Solenoid-ESHK/223170991184?hash=item33f6071450:g:fIIAAOSw0wtavF1w:rk:14:pf:0&LH_BIN=1&autorefresh=true) | 10 | $26 |
| [Paristaltic pump](https://www.ebay.com/itm/DC-12-24V-Peristaltic-Pump-Large-Flow-Dosing-Pump-Vacuum-Aquarium-Lab-Analytical/273097535778?hash=item3f95e1b122:m:mUXje-wYDBR0DV0zzfXsCEQ:rk:10:pf:0) | 1 | $25 |
| [5 to 1 splitter](https://www.ebay.com/itm/5-Way-Outlet-Metal-Aquarium-Air-Valve-Splitter-with-5mm-Tube-Diameter-YM/172053425098?hash=item280f2eebca:rk:16:pf:0) | 2 | $6 |
| [Logic level MOSFET](https://www.ebay.com/itm/20Pcs-IRLZ44N-PBF-Power-MOSFET-Logic-Level-N-Channel-0-022OHM-TO-220-IC-Chip-USA/173493492366?hash=item2865049a8e:rk:1:pf:0) | 11 | $7 |
| **total** |  | $64 |

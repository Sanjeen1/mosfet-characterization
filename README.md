# mosfet-characterization
Collection of MOSFET experiments (Id–Vg, Id–Vd, temperature effects and more) simulated in Ngspice for device behavior and VLSI research.

Mname Drain Gate Source Bulk ModelName [parameters...]

m1 vdd in 0 0 nfet l = 1u w = 0.5u

dc v_in 0 3.3 0.1 v_dd 0 3.3 1 --> This is often used in MOSFET characterization, where you want to see how the Id–Vg curve changes for different Vds values (Transfer characterisrtic).

dc v_dd 0 3.3 0.1 v_in 0 3.3 1 --> This setup gives you Id–Vd characteristics (output characterstic) at different gate voltages.

**Output Characteristic**

<img width="754" height="484" alt="image" src="https://github.com/user-attachments/assets/5d73e5e0-b0fe-4cdc-b569-ee26e613b27b" />

The above is Id vs Vd (outut characteristic) at gate voltage 0 1 2 3 (from bottom to top ) stepsize is 1.

**Transfer characteristic**

<img width="753" height="478" alt="image" src="https://github.com/user-attachments/assets/7cb6fb42-a90f-49a8-b09d-2988937e1ff4" />
The above is Id vs Vg (Transfer Characteristic) at drain voltage 0 1 2 3 (from bottom to top ) stepsize is 1.

## Threshold voltage effect -

**For different threshold voltage (vt) (plot of Id vs Vg curve)**

<img width="1220" height="587" alt="image" src="https://github.com/user-attachments/assets/2ca16f03-2b48-4beb-b061-e893d2fc1567" />

When threshold voltage increase the drain current reduced as we can see according to current eqaution also.


**For different threshold voltage (vt) (plot of Id vs Vd curve)**

<img width="1157" height="593" alt="image" src="https://github.com/user-attachments/assets/ab8a21e1-d150-40c5-8b38-331f9065b30f" />

**For different length-**

<img width="1041" height="564" alt="image" src="https://github.com/user-attachments/assets/ea927f19-53d3-4184-a319-2557455dbd5b" />

Same as current equation 

**For different width-**

<img width="1041" height="416" alt="image" src="https://github.com/user-attachments/assets/d2e5c416-ae0d-4afc-9bb6-f291ddf3c2d2" />

**Effect of channel length modulation -**

<img width="1055" height="459" alt="image" src="https://github.com/user-attachments/assets/9621d72f-4cc8-44de-a13b-71ecaa0096fd" />

**Effect of source to body voltage (Vsb) -**
Sweaping Vsb and ploting Id vs Vg for threshold voltage 

<img width="757" height="449" alt="image" src="https://github.com/user-attachments/assets/831955e6-9b5e-411e-b1ef-f01d22135de1" />

The vsb is variying from 0 (left most) to 1.8 (right most). we can see threshold voltage increases as Vsb is induced and this phenomenon is known as body effect. If Vsb = 0 then body effect is absent. When Vsb is increased then threshold voltage is induced. The Vsb is positive means source is means body is more negative than source.

**Vsb increases then threshold voltage increases or when Vbs increases threshold voltage decreases.**

**Effect of temperature -**

<img width="753" height="476" alt="image" src="https://github.com/user-attachments/assets/2c939243-9124-48b6-b344-1d7bcf50e374" />

Drain current directly proportional to mobility , mobility is inversly proportional to temperature, so for low temprature drain current will be higher for particular Vgs as shown here. 
Temperature is 20 (top pink) -- 40 (middle) -- 100 (bottom blue colour)


<img width="1043" height="571" alt="image" src="https://github.com/user-attachments/assets/6ab55148-922c-4532-be1d-059351cd517a" />

iv_data.txt will be generated. Left side is voltage value and write side is current value.

<img width="1011" height="525" alt="image" src="https://github.com/user-attachments/assets/7fbe0d19-80a4-4d6f-b103-4ed4c96f2463" />

Here sweaping step size is 0.1 as shown above.

If you want your Id vs Vgs plot to be ploted on logarithmic scale then python tool is provided here named "Plot_on_logarithmic_scale". import the iv_data.txt and run the command. we can see the plot on logarthmic scale. 













# mosfet-characterization
Collection of MOSFET experiments (Id–Vg, Id–Vd, temperature effects and more) simulated in Ngspice for device behavior and VLSI research.

Mname Drain Gate Source Bulk ModelName [parameters...]

m1 vdd in 0 0 nfet l = 1u w = 0.5u

dc v_in 0 3.3 0.1 v_dd 0 3.3 1 --> This is often used in MOSFET characterization, where you want to see how the Id–Vg curve changes for different Vds values (Transfer characterisrtic).

dc v_dd 0 3.3 0.1 v_in 0 3.3 1 --> This setup gives you Id–Vd characteristics (output characterstic) at different gate voltages.

**Output Characteristic**
<img width="754" height="484" alt="image" src="https://github.com/user-attachments/assets/5d73e5e0-b0fe-4cdc-b569-ee26e613b27b" />
The above is Id vs Vd (outut characteristic) at gate voltage 0 1 2 3 (from bottom to top ) stepsize is 1.

**Transfer chaeracteristic**
<img width="753" height="478" alt="image" src="https://github.com/user-attachments/assets/7cb6fb42-a90f-49a8-b09d-2988937e1ff4" />
The above is Id vs Vg (Transfer Characteristic) at drain voltage 0 1 2 3 (from bottom to top ) stepsize is 1.

##Threshold voltage effect -
**For different threshold voltage (vt) (plot of Id vs Vg curve)**
<img width="1220" height="587" alt="image" src="https://github.com/user-attachments/assets/2ca16f03-2b48-4beb-b061-e893d2fc1567" />
When threshold voltage increase the drain current reduced as we can see according to current eqaution also.

**For different threshold voltage (vt) (plot of Id vs Vd curve)**
<img width="1157" height="593" alt="image" src="https://github.com/user-attachments/assets/ab8a21e1-d150-40c5-8b38-331f9065b30f" />








# Hardware
This repository will eventually contain all of the various hardware to software control projects I have worked on

APD_Control contains both a GUI for using one of our APDs and also a class for controlling the APD
via one of our DAQ boards

CLS_Scan: Cavity Length Scans
This package will contain a gui that will incorporate an output from our DAQ board to control
the length of the cavity and an input into our board that is monitoring the APD signal

Gimbal_Mirror:
This package contains a gui that allows control of the Gimbal mirror mount using
our APT motors. This might be changed in the future to using Thorpy instead of Thorlabs_Apt but
we are settling for right now. The camera is controlled via UC480 drivers through instrumental
package

Power_Meter:
This will hold a class for monitoring measuring the power via the power meter box
as of right now it is controlled via ThorlabsPM100D package but this can be modified in the
future to just working with direct SCPI commands if we so desire

Thorlabs_Camera:
This is a work in progress to control the Thorlabs DC1545M cameras via the TSI drivers
Thus far it is not working but we will continue to work on that

TLB_6700:
Contains controls for controlling our velocity lasers. This is a work in progress but will eventually
allow for scanning over wavelengths and I will potentially make a GUI out of this, I am not sure yet
though. There will possibly be a White Light Scan gui instead but we will see

VCO_Control:
Contains a DAQ output that is used to control the frequency of our Voltage Controlled Oscillator

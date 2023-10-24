### Sender module

Devices to get authenticated are simulated in this module. This is set up on a Raspberry Pi device. 

### Possible workflow of this module can be seen below:
1. Prepare the device:
*  Set up a Python environment on the device and ensure it can reach the server (both devices can be in the same network, or add a router in between if they are in different subnets).
  
2. Send authentication requests to the server:
*  Depending upon the use case (intact, noisy, or corrupted responses), a device will send request to the server for authentication.
*  This is organized in various directories, namely *sender/corrupted*,*sender/intact*,*sender/noisy*. 

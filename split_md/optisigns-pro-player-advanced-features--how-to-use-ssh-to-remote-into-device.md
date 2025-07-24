## How to Use SSH to Remote Into Device

Pro Players allow remoting into devices using SSH. Here's how to set that up.

First, enable **SSH** in your Advanced Settings.



This will provide you with the SSH IP and Port number. By default, the port is **3000** , but it can be changed to whatever you like.



Now that SSH is enabled and you have the IP and Port, you can use a computer terminal to remote into the device.

Type the following command:
    
    
    SSH [optisigns@<ip-address-here>](mailto:optisigns@<ip-address-here>) -p <port-number-here>

When it asks for a password, type **optisigns**. This should connect you to the device via SSH.

To change the default password (which we _**highly**_ _**recommend**_), type:
    
    
    passwd

This will ask you to type the current password, then new, then to type in the new password again.



**NOTE**  
---  
Restarting the OptiSigns Pro Player will cause SSH to automatically disable for security purposes.  
  
That's it! You should be able to use the SSH function now.

* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/35577511423635)

---

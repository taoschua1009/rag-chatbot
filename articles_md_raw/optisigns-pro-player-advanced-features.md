# OptiSigns Pro Player Advanced Features

### In this article, we go over the Advanced Features of the new Gen 3 OptiSigns Pro Player.

**IMPORTANT**  
---  
This article applies strictly to the _OptiSigns Gen 3 Pro Player or ProMax Player_ on version **5.6.33** or later.  
  
  * OTA Updates
    * Forcing an OTA Update
  * The "About" Option
    * Device Log
    * Advanced Settings
  * How to Bring Up the System Terminal
  * How to Use SSH to Remote into Device
  * How to Perform a Factory Reset



The [**OptiSigns Pro Digital Signage Player**](https://shop.optisigns.com/collections/shop-page/products/optisigns-digital-signage-player) or **[OptiSigns ProMax Player](https://shop.optisigns.com/products/optisigns-promax-signage-player)** are mighty devices, able to leverage the full power of OptiSigns **[digital signage software](https://www.optisigns.com/)** to display your content on any screen with unparalleled visual clarity and customizability.

But there’s even more to the **[Pro Player than its standard features](https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player)** , and here we’ll explain the device’s Advanced features.

**NOTE**  
---  
If you do not see all the options listed below, we recommend performing an **OTA Update** to ensure you have the latest version of the Pro Player software. This is covered later in the article.  
  
* * *

## OTA Updates

The OptiSigns Pro Player makes use of OTA updates to receive security patches, platform enhancements, additional feature support, and more.



By default, the Pro Player can be set to check for updates once per week at a time you specify. If update is available, it will be automatically downloaded as long as the player has an internet connection. It’s also possible to force an OTA update if necessary.

### How to Force an OTA Update

If your device misses its update window, either due to being powered off, or lacking reliable network connection, it is possible to check for an OTA update to the OptiSigns Pro Player and apply it.

In order to do this, you’ll need access to the OptiSigns Portal. From the **Screens tab** , click the **3 Dots** **→ Execute Remote Commands**.



You’ll be taken to the below screen:



Target the screen you’ve paired with your OptiSigns Pro Player, then enter the **forceOTA** command in the highlighted field. After a few seconds, you should see the following:



This means the OptiSigns Pro Player has received the command and executed it. It should now be receiving its update.

**NOTE:** In order for your OptiSigns Pro Player to receive commands, it will need to be connected to the Internet.  
---  
  
* * *

## The ‘About’ Option

The **About** option provides data on your Pro Player, in addition to different options.



This lets you know everything from the name attached to your screen, to whether the Player is connected to the internet, to the storage used.

It also provides further options.

  * **Reboot** does what it says. It will reboot your device.
  * **Device Log** allows you to export your device log. More detail is provided below.
  * **WiFi Setup** lets you tweak the WiFi settings of the device. This is done the same way as on the device’s initial setup.
  * **Advanced Settings** provide additional network options. More detail is provided below.



### Device Log

The device log option allows you to export the device log into an external device. In order to use this option, you’ll need a USB drive or MicroSD card plugged into your Pro Player. When you hit the **Device Log** option with an external drive plugged in, you’ll see the following message:



You can then take your external device and do whatever you like with the device log.

### Advanced Settings



On the**Advanced Settings** screen, you can perform various functions such as enabling/disabling Network Proxy, NTP, the On-screen Keyboard, SSH, and configuring a Static IP for either WLAN or Ethernet. Selecting any of these options will enable further options in the window:



  * **Certificate File** **-** Allows you to [install a root certificate](https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens) for displaying an internal website. The certificate will need to be present locally on the device in order for it to be installed.
  * **NTP Server****-** Input server information for your Network Time Protocol (NTP). This can be used to ensure the OptiSigns Pro Player has its computer clock time with other time sources in your network.
  * **WiFi SSH IP** \- IP address associated with your SSH. Only appears when SSH is enabled.
  * **Network Proxy****-** Server information for any network proxy. This is a system or router which serves as a middleman between our Pro Player and the internet and can be used to enhance security, privacy, or efficiency.
  * **KeyBoard Layout****-** Choose between various international keyboard layouts. Default is US.
  * **Static IP Information****-** An IP address that remains the same over time. We allow two types of Static IP: WLAN or ETH. These can improve network performance. This screenshot shows WLAN; if Static ETH IP is chosen, these will be ETH IP Address, Default Gateway, Subnet Mask, and DNS Server. 
    * **IP Address -** Set the Static IP address.
    * **Default Gateway** \- Set the Default Gateway for the Static IP address. This is the IP address of your router.
    * **Subnet Mask** \- Set the Subnet Mask for the Static IP. Usually, this number is 255.255.255.0 or some variant of this.
    * **DNS Server** \- Lets you set up your DNS server for the Static IP address.



* * *

## How to Bring Up the System Terminal

The OptiSigns Pro Player has a console you can use to input commands directly. This can be accessed through the OptiSigns portal. From the **Screens tab** , click the **3 Dots** **→ Execute Remote Commands**.



You’ll be taken to the below screen:



Target the screen you’ve paired with your OptiSigns Pro Player, then enter the **showTerminal** command in the highlighted field. After a few seconds, you should see the following:



This means the OptiSigns Pro Player has received the command and executed it. Your console terminal should now be visible on your screen and can be interacted with.

* * *

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

## How to Perform a Factory Reset

Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.

To do this, attach a keyboard to the Player. Then, **Reboot** it. As it restarts, rapidly tap the **↑ arrow**. It will boot into this screen:



Here, you have several additional options. Hit **Factory Reset**. You’ll receive this prompt:



You’ll need to enter your **admin password.**

Once entered, you’ll see a screen like this:



Afterwards, your factory defaults will be restored.

### **That’s all!**

OptiSigns is a leader in[ digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).

---
Article URL: https://support.optisigns.com/hc/en-us/articles/35577511423635

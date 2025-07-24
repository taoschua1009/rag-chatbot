# OptiSigns Android Player Troubleshooting Guide

### In this article, we will troubleshoot the most common issues people encounter using our OptiSigns Android Player.

  * Identify Your Device
  * Best Practices
  * The Troubleshooting Option
  * Hardware Troubleshooting
    * Network Troubleshooting
    * Power Troubleshooting
    * HDMI & TV Connection Troubleshooting
    * Remote Control Troubleshooting
    * Changing Device Time Zone
    * Blank Screen Troubleshooting
    * How to Factory Reset the OptiSigns Android Player
  * Content Playback Troubleshooting
    * Website display or sizing issues
    * Designer or template sizing issues
    * Screen color distortion
    * Fixing the OnHold warning
    * App crashing
  * Android Player RMA Process



If you’ve got an OptiSigns Android Player and you’re having issues, you’ve come to the right place. For first time setup, see our article on how to [**Set Up the Android Digital Signage Player**](https://support.optisigns.com/hc/en-us/articles/27267311796243-OptiSigns-Android-Digital-Signage-Player).

* * *

## Identify Your Device

There have been several versions of the OptiSigns Android Stick over the years. The most common are the Gen 2 and Gen 3 devices:



Functionally, these are quite similar. Both use the latest versions of the OptiSigns software. Most of their differences lie in **Networking.**

* * *

## Best Practices

We recommend certain best practices to keep your OptiSigns Android Player running at peak efficiency:

  * Do not put too much pressure on the power cable, as this can cause the Player to get pulled from its HDMI socket.
  * Keep the player in an indoor, air conditioned environment
  * Run the Android Stick in fullscreen mode, or with a 2-3 zone Split Screen.



By default, an Android Player has an [**Operational Schedule**](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232)built in to ensure it has 8 hours of downtime per day:



If you require 24/7 uptime, more than 3 zones on a split screen, a heavy Website Dashboard (including Tableau or Power BI reports), or plan to use the player in hot or cold environments, consider the [**OptiSigns Pro Player**](https://shop.optisigns.com/products/optisigns-digital-signage-player) or [**ProMax Player**](https://shop.optisigns.com/products/optisigns-promax-signage-player).

* * *

## The Troubleshooting Page

Your first stop when running into a problem with the OptiSigns Android Player should be the **Troubleshooting Page.** This is an option on the side menu.

To access it, press the **Three-Bar button** on your remote to open the side menu of the OptiSigns app. Navigate to **Troubleshooting** under the **Advanced Options** section.



Now you can view detailed information about the app’s status and connectivity to assist with troubleshooting.



  * **Check Internet Connection** : Verifies whether the device has an active internet connection.
  * **Check Connection to API Services** : Tests the device's connection to OptiSigns services. 
    * **Note** : If this check fails, it may be due to a firewall blocking the connection. Refer to our[ **Whitelist Article**](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
  * **Check File Downloading** : Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
  * **Network Information** : Displays the current network the device is connected to. 
    * **WiFi/Ethernet Details** : Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
  * **Device Information:**
    * Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
    * Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
  * **Running Time** : Shows how long the OptiSigns app has been running on the device.
  * **Storage** : Displays used and total storage capacity.
  * **Memory** : Displays used and total memory capacity.
  * **System Time** : Shows the current system time on the device.
  * **System Time Zone** : Displays the time zone configured on the device.
  * **Assigned Content Type** : Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
  * **Assigned Content Name** : Provides the name of the content being displayed.
  * **Device Created Date** : Displays the date the device was activated.
  * **Operational Schedule Assigned** : Shows whether an operational schedule is assigned (**Y/N**).
  * **Mute Status** : Displays the current audio status of the device.
  * **Heavy Content Status** : Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (**Y/N**). This will usually result in lag.



* * *

## Hardware Troubleshooting

Here we will cover the most common hardware troubleshooting issues our support team encounters.

### Network Troubleshooting

**GEN 2** | **GEN 3**  
---|---  
2.4 GHz WiFi only | 2.4 GHz and 5 GHz WiFi  
WiFi 5 and below | WiFi 5 and below  
No Ethernet | Ethernet Capable  
  
To identify and resolve network issues:

  * Create a mobile hotspot, then have your Android Player connect with it. A successful connection indicates a problem with your general Wi-Fi connection.
  * Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.
  * Plug in an Ethernet cable to see if it can still connect.



To see what network you’re connected to, go to the Side Menu and hit **Exit**. This will close the OptiSigns app.



Next, open the menu on the side using the remote. If connected to a network, it should appear here. If not, you'll need to set that back up.



### Power Troubleshooting

One of the most common causes of device instability is not using the provided power adapters and cables.

If your device has any sort of intermittent power issues, **_please ensure it is not being powered by the USB port on your screen_**. The USB port does not provide enough power to the device to keep it running under all conditions.

In the event there is no available power outlet nearby and the USB port is your only option, keep your content load light - meaning, no videos, no large files, etc.

### HDMI & TV Connection Troubleshooting

If you’re having problems connecting your Android Player to your HDMI port or TV, here are some steps to try:

  * Try a different HDMI port on your screen
  * Try to connect the Android Player directly to your TV without the HDMI extended
  * Try a different TV or monitor to see if it will work at all



If none of these work, contact our support team at [support@optisigns.com](mailto:support@optisigns.com). 

### Remote Control Troubleshooting

The OptiSigns Android Player ships with a Remote Control. Which remote control you have depends on the version of your player, but they largely function the same with a few slight differences.

**Gen 3 Remote:**

****

**NOTE**  
---  
To pair or re-pair this remote, hold the **Back** and **Home** buttons.  
  
**Gen 2 Remote:**



**NOTE**  
---  
To pair or re-pair this remote, hold the **Return** and **OK** buttons.  
  
OptiSigns Players also support the [**Mobile Admin App**](https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App) as a Remote Control. This is our **_top recommendation,_** as not only does it function as a true remote control (allowing you to control your players from anywhere), but it has numerous other features as well.

If your remote control is having issues:

  * Ensure batteries have been installed inside your remote control, and that they are not dead
  * Re-pair your remote control with the player
  * Try a plug-in USB keyboard or mouse
  * Use the Mobile Admin app to set up Wi-Fi, or as a remote control itself



### Blank Screen Troubleshooting

If your device and screen are on, but only displays a black screen:

  * Network issues, **see above**.
  * Check to make sure there is a Playlist or Asset assigned to your screen.
  * Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.
  * Check your firewall settings, and ensure you’ve [**Whitelisted OptiSigns IP addresses and ports**](https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports).
  * Check your Operational Schedule, and verify its power settings are not set to Off. If an Operation Schedule’s power settings are set to Off, it will remain off during the designed time.



If the device is still not displaying content after you’ve checked these, check our **Content Playback Troubleshooting**section, then try a **Factory Reset**.

### Changing Device Time Zone

When **[setting a schedule](https://support.optisigns.com/hc/en-us/articles/360016981853-Create-and-Using-Schedules-with-OptiSigns)** , it's critical that the portal and device share the same time zone. If the time zones are not identical, it can cause your schedule to start at a different time than you'd like. The issue is usually the device's time zone.

To do this, you'll need to change it. Start by pressing the **Home button** on your remote (or hit **Exit App** from the Side Menu), and navigate to the **Settings** menu.



Select **Device Preferences**.



Select **Date & Time**.



Select **Set time zone**.



For some reason, Android devices lead with Midway Island, in the middle of the Pacific (some things in life are best left a mystery). Navigate to your preferred time zone and select it.



Now your device and schedule should sync properly.

**NOTE**  
---  
These steps can be performed remotely using the **Mobile Admin App** or through **MDM Commands**.  
  
### How to Factory Reset the OptiSigns Android Player

You can factory reset your Android Player if the system is not functioning properly or the Android system will not load.

There are two ways to do a factory reset.

#### Soft Reset

A soft reset can be performed if the system is still accessible and operational. This will erase all the data on the device, and may help improve performance and fix some issues.

On the Home screen, go to **Settings**. Hit **Device Preferences,** then choose **About**. Finally, choose **Factory Reset.**



It will ask if you’re sure you’d like to perform this function. If you are, hit **OK**. The soft factory reset will take place.

#### Hard Reset

When certain Android system files are corrupted, the device will not be able to boot into the Android system. In this case, you will need to perform a hard reset.

To perform one, you’ll need a small tool. Think paperclip, needle, or SIM card pin. Then, ensure the device is completely powered off and the USB power cable is unplugged from the device.

Next, use your small tool to press into the small hole on the side of the device. Hold it, then plug in the power cable while the tool is still pressing the button in the small hole.



The system will then boot into recovery mode. You can use the button to navigate between selections and will need to press and hold for 1-2 secs to confirm selection. Choose **wipe data/factory reset** , and the factory reset will start.



Then choose **Factory data reset:**

****

Once the process is complete, you’ll see a **Data Wipe Complete** message at the bottom of the screen. From there, select **Reboot System Now** to finish.



Your Android Stick will be fully factory reset.

* * *

## Content Playback Troubleshooting

This section deals with common issues we see when trying to display content using an Android Player.

### Website Display or Sizing Issues

To display a website as you would see it on a Desktop or PC, change Device Scaling to smallest.

For more information, see the relevant article on Device Scaling:

  * [**Gen 3 Device Scaling**](https://support.optisigns.com/hc/en-us/articles/28026588373139-How-to-Fix-The-Scaling-Issue-on-OptiSigns-Android-Device-Gen-3)
  * [**Gen 2 Device Scaling**](https://support.optisigns.com/hc/en-us/articles/27607906766483-How-to-Fix-The-Scaling-Issue-on-OptiSigns-Android-Device)



### Designer or Template Sizing Issues

If using the [**Designer app**](https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes)**,** try setting the canvas size to 960x540, or change the display size on Android.

### Screen Color Distortion

If your screen is showing distorted colors or displays, try:

  * A different HDMI cable, port, or screen
  * Turning off everything transmitting data between the screen and Android stick, such as the HDMI-CEC, Dolby Vision, or auto adapting resolution



### Fixing the OnHold Warning



This warning displays when the device is in the [**OnHold Folder**](https://support.optisigns.com/hc/en-us/articles/1500003244381-About-the-OnHold-Devices-Folder). This happens when you’ve ordered more devices than you had licenses for. Any devices above your license limit will automatically be placed in the OnHold folder and will need to be removed, even when the license limit has been raised.

### App Crashing

To handle crashes, clear the cache and then data of the OptiSigns Player, then reboot. You may need to Factory Reset.

App crashes are most common when is kept on for extremely long periods of time. To avoid them, schedule a **Restart Timer**.

* * *

## Android Player RMA Process

If none of the solutions here work, feel free to submit an RMA request. Devices will be tested as part of the RMA process, and if they are working correctly, you (the customer) will be charged a restocking fee.

Here are the steps for an RMA:

  1. Obtain a proof of purchase stating that your device was purchased within the last 12 months, complying with our 12-month warranty policy.
  2. Fill out [**this RMA request form**](https://share.hsforms.com/14BvoeL1JRlGgxr3ec_kdJgca5m5).
  3. RMA requests are reviewed within 3 business days.
  4. New devices arrive within 3-5 business days to most places in the United States.
  5. Return the old device within 30 days.



### That's all!

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).

---
Article URL: https://support.optisigns.com/hc/en-us/articles/40147900639891

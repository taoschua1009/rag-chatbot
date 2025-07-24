# Enabling Lock Down Mode on Touch Screen Devices

#### Lock Down mode is essential for ensuring users only interact with the intended content without interfering with any OptiSigns settings on your device. This guide will walk you through enabling this mode for the OptiSigns app on various devices and their limitations.

**In this article:**

  * What Lock Down Mode Does
  * How to Turn On Lock Down Mode
  * How to Turn Off Lock Down Mode
    * In the OptiSigns Portal
    * On the Device Level
  * Lock Down Mode by Device
    * OptiSigns Android Player
    * Windows
    * Android Tablets
    * OptiSigns Pro Player
    * iPad and Other iOS Devices



* * *

## What Lock Down Mode Does

  * Hides the side menu, the close, and sizing buttons.
  * Prevents users from exiting the OptiSigns app or making any changes to your setup.
  * Minimizes user interaction with the OS if they can exit the app.

**NOTE:** This will differ depending on the device used. Please see device limitations below.  
---  
  
* * *

## How to Turn On Lock Down Mode



  1. Open the OptiSigns portal and go to the **[Screens](https://app.optisigns.com/app/screenManagement) **page
  2. Click **Edit Screen** on the preferred screen.
  3. Open the **Advanced** section, expand the **More** settings**.**
  4. Next to **Lock Down** , click the **Activate** button.
  5. Confirm you'd like to Activate.
  6. **Set an unlock password** when prompted. 
     * This password allows you to unlock the device.





  1. Click **Save** at the bottom of the Edit Screen pop-up.



The device is now in lock down mode.

* * *

## How to Turn Off Lock Down Mode 

### In the OptiSigns Portal

### 

  1. Open the OptiSigns portal and go to the **[Screens](https://app.optisigns.com/app/screenManagement) **page
  2. Click **Edit Screen** on the preferred screen.
  3. Open the **Advanced** section, expand the **More** settings**.**
  4. Click "**Deactivate** " on the right side of the Edit Screen pop-up.



### On the Device Level

  1. Tap on your screen **6 times** , and a pop-up window will appear.
  2. Enter the **unlock** **password**.
  3. The device is now unlocked. 



_Based on your device, the location you must tap may be in a specific area._

Note: If you unlock the app and then exit it, once you reopen the app, it will be in lock down mode again.   
---  
  
* * *

## **Lock Down Mode by Device**

## OptiSigns Android Player



**_Recommended Device_**

When using an OptiSigns Android Stick, the OptiSigns app is:

  * **Completely Locked Down:** Users can only interact with the content being displayed on the screen.
  * **Side Menu Inaccessible:** Users cannot open the OptiSigns side menu, exit the app, unpair the screen, or mess with the device



Due to OS-level control with the OptiSigns Android Stick, this method provides the most cohesive lock down. 

#### **Limitations**

  * **Setting Up Your Screen:** You will need to use either our OptiSigns portal or Mobile Admin App to set up your screen with content prior to locking it down. 



* * *

## Windows Devices

You will need to disable edge swipe to prevent users from swiping out of the application. Instructions on how to do this may differ based on your device. (Through your device's Local Group Policy Editor, Registry Editor, etc.).

Once done, a Windows device in lockdown mode will be:

  * **Completely Locked Down:** Users can only interact with the content being displayed on the screen.
  * **Side Menu Inaccessible:** Users cannot open the OptiSigns side menu, exit the app, unpair the screen, or mess with the device.



#### **Limitations**

  * **Keyboard and Mouse Required:** A mouse is needed to access the deactivation window. Click on the uppermost top part of the screen six times with a mouse to deactivate. Then, use a keyboard to type in the password.



* * *

## Android Tablets and Devices

When using lock down mode on an Android tablet:

  * **Locks Side Menu:** This prevents users from accessing the OptiSigns side menu, thereby blocking the ability to unpair the device, change its orientation, and alter other specific device settings.
  * **Enhance Security and Usability:** It is recommended to enable the "Keep Awake" feature, which ensures the screen remains on even if users attempt to turn it off.



#### **Limitations**

Since we lack permission on the device, we can't pin the OptiSigns app or run it in single app mode. We recommend using Android MDM software, which usually works with major hardware manufacturers and has the necessary permissions to pin the OptiSigns app.

  * **Exit the App:** Users can still exit the OptiSigns app.
  * **Navigation Bar is Accessible:** The device navigation bar remains accessible so users can make changes at the device level and escape the app. Steps can be taken to minimize or limit the navigation bar depending on the device. 



* * *

## OptiSigns Pro Player



To fully lockdown the OptiSigns Pro Player, you will need to follow these additional steps:

  1. Open **Extension Manager** on your Pro Player.  

  2. Go to the **Browse** section.
  3. Search for "**gestures** ".  

  4. Find and install the **"Disable Gestures 2021"** extension.
  5. Go to the **Installed** section, and ensure that the **"Disable Gestures 2021"** extension is enabled.  

  6. **Restart** the Pro Player.
  7. **Activate Device Lockdown** for that screen in the OptiSigns app.



When using lock down mode on an OptiSigns Pro Player:

  * **Navigation Buttons Removed:** Exit, Side Menu, and Minimize buttons will be removed from the top right corner



#### **Limitations**

  * **A Mouse (and Keyboard) is Needed:** A mouse is needed to access the deactivation window. Click on the uppermost top part of the screen six times with a mouse to deactivate. You can use the on-screen keyboard or plug in your own keyboard to type in the password.
  * **Certain Assets Change Accessibility:** With normal files and assets, the side menu is accessible using both touch screen and mouse. With Engage assets, the side menu becomes inaccessible when an Engage asset is pushed to the screen.



* * *

## iPad and Other iOS Devices

For iPad or other iOS devices, you can use either Guided Access or Apple Configurator to lock a singular app on your device. You can learn more about how to set up Guided Access [here](https://support.optisigns.com/hc/en-us/articles/25273043501587). This method will make the device:

  * Unable to exit the app or access the control center to make changes to the device itself
  * If you press "Exit App" in guided access and lock down, it will close then reopen.



If you have many devices and would like to easier manage them, you can use the Apple Configurator. To learn more about this [here](https://support.apple.com/guide/apple-configurator-mac/start-single-app-mode-cadbf9c172/mac).

#### **Limitations**

  * **Lock Down Mode Unavailable on iOS:** The lockdown feature is not currently available for iOS devices. Guided Access is recommended to prevent users from controlling your device. However, users can still unpair, refresh the content, and change the orientation of your screen.



* * *

## That's it!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).

---
Article URL: https://support.optisigns.com/hc/en-us/articles/30310366838803

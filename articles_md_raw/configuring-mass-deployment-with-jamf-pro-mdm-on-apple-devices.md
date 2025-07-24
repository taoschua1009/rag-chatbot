# Configuring Mass Deployment with Jamf Pro MDM on Apple Devices

Efficiently managing digital signage across multiple devices is crucial for businesses to ensure smooth operations and consistent updates. OptiSigns, in conjunction with a Mobile Device Management (MDM) system, offers a streamlined process for mass enrolling your devices. This guide will walk you through the steps to distribute and manage OptiSigns digital signage software using a Jamf MDM system on Apple devices.

* * *

In this article:

Requirements

Step 1: Load OptiSigns App Inside Jamf MDM

Step 2: OptiSigns App Enrollment with Jamf Pro MDM

Step 3: Deployment

## Requirements

To proceed with this guide, please ensure that you have:

1\. Jamf Pro MDM account.

2\. OptiSigns.com credentials.

3\. Apple devices running iOS or tvOS.

4\. Access to Apple Business Manager or Apple School Manager.

## Step 1: Load OptiSigns App Inside Jamf MDM

Inside ABM (Apple Business Manager) volume purchase licenses of OptiSigns Digital Signage (It's free).

We assume that the ABM VPP account is linked to your Jamf Pro instance, otherwise, use this Jamf [Video Guide](https://trainingcatalog.jamf.com/volume-purchasing/637880) to do so.

After populating ABM apps into Jamf MDM, you should see OptiSigns Digital Signage app inside MDM Mobile Device Apps section, as shown below:

****

## Step 2: OptiSigns App Enrollment with Jamf Pro MDM

Before deploying the app to devices, you can preconfigure it to have your device automatically enrolled into your OptiSigns account.

  * This is not required, but if you are managing a large number of devices, this will make the deployment much easier.



To do this, navigate to the **mobile device apps section** in Jamf MDM → Click on the **OptiSigns Digital Signage app →** Select the**App Configuration** section → Complete the configuration as shown below:



Let's go through each section of the configuration:



  1. **serialNo:** Serial number of the device, you can map this to a variable from your MDM. 
  2. **accountId:** This is your OptiSigns Account ID, you need to enter it manually.



Account ID can be found inside the OptiSigns portal, by visiting the**[Screens tab](https://app.optisigns.com/app/screenManagement) **→ Finding the screen you'd like→ Clicking **Edit Screens** → Click **Advanced** → Click **More** → Click on the "**i** " button 



This will open your **Device Info** :



3.**screenName** \- This is the screen name that will appear on the OptiSigns portal, as shown in the screenshot below. Normally this is mapped to a variable from your MDM.



## Step 3: Deployment

After completing the app configuration, you need to define the scope in Jamf MDM. Follow the Jamf [video guide](https://trainingcatalog.jamf.com/device-scope/552567), and assign VPP within Managed Distribution:



Finally, you can check installation status in MDM:



### That's all! Congratulations!

Now, you can enjoy OptiSigns Digital Signage across your Apple devices.

---
Article URL: https://support.optisigns.com/hc/en-us/articles/31695220475283

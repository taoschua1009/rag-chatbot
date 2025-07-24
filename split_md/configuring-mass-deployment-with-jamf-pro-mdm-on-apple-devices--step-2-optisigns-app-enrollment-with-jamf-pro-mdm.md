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

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31695220475283)

---

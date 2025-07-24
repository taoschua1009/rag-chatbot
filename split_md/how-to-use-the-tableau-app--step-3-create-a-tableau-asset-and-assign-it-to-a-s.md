## Step 3: Create a Tableau Asset and Assign it to a Screen

Now that we've got the Tableau integration set up, it's time to create a Tableau asset. This asset determines how your report will show up on your screens.

**NOTE**  
---  
See **Note 2** if your workbook contains Broad Views.  
  
First, find the report you'd like to display. Hit **Share:**



On the Share View window, hit **Copy Link** :



Now go back to the OptiSigns portal and hit **Files/Assets** → **Apps:**



Now find the **Tableau** app.



Clicking the app will open this window:



  * **Name -** The name of your Asset. This is used entirely in OptiSigns and can be anything you like.
  * **Tableau Shared Report URL -** This is where you'll input the Share URL you copied earlier.
  * **Update Interval -** Denotes how often the app will sync, measured in seconds.
  * **Authenticate with Connected App Integration -** Tick this box if you want to use Private reports. Since we set this up in Steps 1 and 2, we recommend ticking this box. If you skipped those steps and only want to use Public reports, no need to check the box.

**NOTE**  
---  
Tableau Cloud only allows 600 Update Interval requests per user/hour. See **Note 3** for more information and solutions on how to handle this.  
  
Now it's time to authenticate your Shared Report URL with an appropriate Connected App Integration you set up earlier:



  * **Connected App Integration -** Select the integration you set up in Step 2 in this box.



Once you input the **Tableau Shared Report URL** and have selected your Integration, hit **Save** and your report should appear as a Preview:



Once you have tailored it to your liking, you can **Close** it. This will create a Tableau asset that can be added to a Playlist or directly assigned to a screen:



In order to display different tabs of a report, select the tab you'd like to view on Tableau site, then hit **Share** , same way as before:



You'll then create a new Asset with that Share link as the **Site URL** :



To display all the tabs in a report on a screen, these Assets can be placed in a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) to show the complete report.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/39250660729747)

---

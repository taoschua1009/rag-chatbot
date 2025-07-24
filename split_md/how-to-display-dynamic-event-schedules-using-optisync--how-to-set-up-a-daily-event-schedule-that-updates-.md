#### How to Set Up a Daily Event Schedule that Updates with the Passage of Time

With a Daily Event schedule, once an event happens, there's no need to keep displaying the event. With OptiSync, you can configure your DataSource to ignore events which are now in the past.

To do this, we'll need to set up an additional column in our spreadsheet. We'll call it the **Event Over?** column.

****

In the "Event Over?" column, put this formula:
    
    
    =IF(B2<=NOW(),"Yes","No")

**NOTE:** This formula will only work if both the Date and Time are present in the Event Time cell. The "B2" part should match the actual event time, i.e. B3 for Zumba in the Example.  
---  
B2 is your reference value, which maps up with the event time. This formula will work regardless of whether or not the current date is referenced in the "Event Time" column.

Within the settings of your Google Sheet, please ensure Recalculation is on (e.g., On change and every hour/minute), otherwise the formula won't recalculate.



You can access this in your Google Sheet by selecting **File** **→** **Settings** **→** **Calculation.**

All the "Event Over?" column does is check whether or not the event time has passed with a simple yes or no. When this screenshot was taken, it was between 1:00 and 3:30, so the first event to be shown should be "Rowing," followed by "Surrender Yoga."

To do this, we'll make use of the **DataSource** **Filter**.

To get started, highlight the data you want to filter, then hit **Settings.** Then, hit the **Filter** option under your DataSource.



This screen will appear:



What follows is, essentially, an [AND statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) or an [OR statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) you might use in Excel or Google Sheets. The easiest way to understand the Filter option is as an Excel or Google Sheet formula you input within OptiSigns.

You can add **Rules** or **RuleSets** to your filter to create as much complexity as you need:



In order to set up a Rule, you'll need to configure three values.

Selecting the first box gives you these options:



By default, these options equate to the **headers of your columns in the spreadsheet you have mapped.** This list will vary in length depending on how many headers you have. You can also input any value you wish by typing it in the box.

The second box is your **Variable.** OptiSigns provides these options:



The final option provides the following default values:



By default, these map to a screen or other device, allowing your filter to target only certain screens.

However, this value **can be changed to anything you want.** Simply type any value you wish.

For our purposes, we want to check to see if the "Event Over?" is equal to No:



That removes every row where the "Event Over?" value is Yes. Now, your Event Schedule will display this:



There are dozens of possibilities using the OptiSync filter to show even more precise automated data on your screens.

* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/33468569218067)

---

### Applying Filters to Customize Which News Stories to Display

What news stories you wish to display may vary depending on a number of factors. In order to filter out undesired or redundant stories, you can make use of the OptiSigns **DataSource** **Filter**.

To get started, highlight the data you want to filter, then hit **Settings.** Next, hit the **Filter** option under your DataSource.



This screen will appear:



What follows is, essentially, an[ AND statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) or an[ OR statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) you might use in Excel or Google Sheets. The easiest way to understand the Filter option is as an Excel or Google Sheet formula you input within OptiSigns.

You can add **Rules** or **RuleSets** to your filter to create as much complexity as you need:



In order to set up a Rule, you'll need to configure three values.

Selecting the first box gives you these options:



By default, these options equate to the **headers of the data mapped to the source.** This list will vary in length depending on how many headers you have. You can also input any value you wish by typing it in the box.

The second box is your **Variable.** OptiSigns provides these options:



The final option provides the following default values:



By default, these map to a screen or other device, allowing your filter to target only certain screens.

However, this value **can be changed to anything you want.** Simply type any value you wish.

There are dozens of possibilities using the OptiSync filter to show even more precise automated data on your screens.

**TIP**  
---  
Remember the "PromotedState" data value from before? If you want to make sure only custom news articles appear on your screen, try setting the Filter to state: **PromotedState - Equals - 2** This should filter out any other pieces of data received from the API.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/35337746613139)

---

## Modifying the Data

To change the mapping, simply edit the values in the columns, being sure to keep the Asset Element ID and Asset Element Name the same. 

For example, say we want the word "SOCIAL" to appear on one screen in one location, but we want it to say "COMMUNAL" in another. To do this, we simply duplicate the Row, then change the "Screen Name" and "Value" cells:



The "Screen Name" will need to be the same as the name of the screen you're targeting with the asset. This is equivalent to the **Device Name** under the **Edit Screen** tab:



Some best practices:

  * OptiSigns will identify the screens by name and adjust the Value based on what's entered on your spreadsheet.
  * If you change your screen's name, be sure to update your spreadsheet at the same time. If updated later, it could cause issues with data mapping on the screen at the next update interval.
  * ***ALL*** tells OptiSigns that if a screen is not specifically assigned values, it will take value from this row of data. This is equivalent to the "Default Value" mentioned earlier in the article.
    * If a value is detected, it will override the ***ALL*** value, like in the example above.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/42915219118739)

---

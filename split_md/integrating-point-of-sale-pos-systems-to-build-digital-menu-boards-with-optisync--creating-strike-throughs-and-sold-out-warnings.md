#### Creating Strike Throughs and Sold Out Warnings

In the above example, we show a Sold Out warning. However, we don't want to display that all the time - only when the item isn't available. With OptiSync, this can be accomplished thanks to the Post-request processing we did earlier. Our code created this **"soldout: 0"** data. This is tied to our **"available"** data:



When the "available" data reads "true," the "soldout" data reads 0. When your POS system detects items are unavailable, the "available" data will read "false". This will make the "soldout" data read 1.

We can use this knowledge to set up our Sold Out warnings and strike throughs to only appear when items are not available.

Going back to our Repeater Editor, we can click on a piece of text we want to strike through and hit **Settings** :



In the Settings tab, hit **Advanced Options**.



Under Advanced Options, hit **Property Mapping**.



Two values will show up: **Property** and **Value**.



Under Property, choose **Linethrough**.



Under Value, choose **.soldout.** Before the "." will be the name of your API Request.

****

This sets the text to be crossed out when the "soldout" data reads 1.

We can repeat this with the Sold Out reading, except instead of Linethrough, choose **Visible**.



This will make the Sold Out text only appear when the "visible" data reads 1 - in other words, when your product is sold out.

Your final menu ought to look something like this:



Finally, you're ready to Name and **Save** your Design.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31860170199955)

---

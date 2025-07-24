##### Adding Text Elements to a Digital Menu Board

First, create your design. You can make use of one of our repeater templates, or make the design yourself. Our repeater templates can be customized to fit in with your company branding.



The easiest way to set up a Custom News feed is with a **Data Repeater**. For a full breakdown of a Repeater's capabilities,[ see this article](https://support.optisigns.com/hc/en-us/articles/29217646663187). Here, we'll stick to teaching how to add information from your API.

To set up a Repeater, click **"Repeaters" → Add Blank Repeater**.



With the Repeater selected, click **Settings**. A new pane will open up on the right. Here, select **Connect to DataSource**.



Select the DataSource you set up in the last set under **"Other DataSources"**.

You'll be taken back to the last pane with your DataSource now selected. Now, click **Edit** or double click the selected Repeater to head to the Repeater Editor. This is like a design-within-a-design, specifically for your Repeater (news) items. With text selected, click the arrow on the left.



That brings up the DataSource tab. Click on the DataSource Used in this Design and you'll see something like this:



In this example, we want to display the title of the piece, its associated imagery, and the story itself.

By creating text and dragging data points to it, we can create a news feed like this:



This was created by finding data points from the API and dragging them into the desired text boxes. In this case, we only wish to display the "Title," "Banner URL Image," and "Description" so those values were dragged into a blank or existing text box.

The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. It will pull as many data points as you have set up on your API. In this example, we've featured only one news story. The repeater will rotate through the rest, displaying only one at a time. If you want to display more, the number of repeated items and their formatting can be changed using these options under **Settings:**



If we change the total items to, say, 3, we can get a news feed like this with a little bit of design work:



Hopefully this is an effective demonstration of some of OptiSync's abilities.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/35337746613139)

---

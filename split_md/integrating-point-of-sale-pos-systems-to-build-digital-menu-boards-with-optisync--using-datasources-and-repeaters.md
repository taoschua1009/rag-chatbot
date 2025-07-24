### Using DataSources and Repeaters

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.



Scroll down to where it says **"API Gateway Collection"** and click it.



You can also set up a one-time Gateway with the _API Gateway_ command if you need a one-off design with no pre- or post-request processing. In our example, however, we are, so we'll use Gateway Collection.

You should see this screen:



  * **Name -** The name of the DataSource. This is internally facing and will not be shown on your screens.
  * **Select APIs -** Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.
  * **Update Interval -** How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.



Hit **Save** , and the DataSource is created.

It should appear in the left column under **"Used in this design".** It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31860170199955)

---

### Step 3: Creating a News Feed Using Designer in OptiSigns

The next step is getting these values onto your screens and make them automatically update.

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.



Scroll down to where it says **"API Gateway"** and click it.



You can also set up a multi-time Gateway with the _API Gateway Collection_** _._** For this example, we'll stick with the single-use API Gateway.

You should see this screen:



  * **Name -** The name of the DataSource. This is internally facing and will not be shown on your screens.
  * **Select APIs -** Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.
  * **Update Interval -** How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.



Hit **Save** , and the DataSource is created.

It should appear in the left column under **"Used in this design".** It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/35337746613139)

---

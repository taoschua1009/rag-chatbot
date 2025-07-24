## Step 1: Set Up OptiSigns as a Connected App in Tableau Cloud

To view Private reports in OptiSigns, it needs to be set up as a **Connected App** in Tableau Cloud. If you're only interested in displaying Public reports, this step can be skipped - however, we **_highly recommend_** it, as setting up this integration will allow you to use it for any future reports you want to display from this account. If you are only interested in displaying Public reports, though, feel free to skip to step 3.

To begin, find your **Settings** tab within Tableau. Once there, click **Connected Apps** → **New Connected App**.



Select **Direct Trust**.



You'll open the Create Connected App window. Here, you can give your connected app a name (we recommend "OptiSigns" so you know it's for us), restrict its access, and provide allowed domains. For the purposes of this example, we'll apply it to "All projects" and "All domains."



Once created, it will appear in a list of Connected Apps. Select the app.

On this screen, you'll want to **Enable** the OptiSigns app by hitting the **Three Dots**. Then, you'll want to hit **Generate New Secret** :



The blurred out values are your **Secret ID, Secret Value, and Client ID**. These values will be critical to setting up your integration with OptiSigns, so keep this tab open.

With this information and the app Enabled in Tableau, we can configure the integration in OptiSigns.

* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/39250660729747)

---

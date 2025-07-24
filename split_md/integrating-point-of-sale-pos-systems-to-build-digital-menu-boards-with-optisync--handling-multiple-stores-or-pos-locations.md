### Handling Multiple Stores or POS Locations

Once you've got your basic API Gateway request set up, there are a few additional steps you'll want to perform if you have multiple locations for your screens. These different locations may have different menus, or different specials for that day, or even different pricing depending on various factors.

POS systems normally require separate license for each location. Your POS system API may provide different store ID in the API endpoint or using different authentication token. For larger deployment with multiple stores, you can use substitution parameters to handle that with OptiSigns. 

There are two ways to handle multiple POS locations:

  1. Set up individual API requests for each of your POS locations, changing the value in the URL endpoint each time and mapping them to each of your screens individually. If you only have a few locations where your POS system is used, this will work just fine.
  2. _(Recommended)_ Configuring each screen to send its storeID to the API call, allowing a single API request to provide data to multiple screens. For anything more than two or three screens, we recommend this method.



Here's how to handle option 2.

To get started, find the screen you wish to edit.



Click **Advanced** **→** **More** **→** **Device Additional Attributes.**



Two fields will show up, **Key** and **Value**.  


  * **Key** \- A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.
  * **Value** \- Represents the unique code associated with the store or location you wish to pass through to your API.



In this example, we'll pretend the parameter you are changing is called "merchantID". The value inputted will need to be obtained on your end as it will be unique.

Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31860170199955)

---

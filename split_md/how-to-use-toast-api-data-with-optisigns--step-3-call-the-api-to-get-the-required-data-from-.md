## Step 3: Call the API to get the required data from Toast

Now we'll use the authorization token we received in Pre-request processing and pass it to the actual API call header. 

In the Header tab, create two parameters with the following values:

**authorization** Bearer {{authorization}}

**Toast-Restaurant-External-ID**

You can get the **Toast-Restaurant-External-ID value** from Toast Portal. This is the specific restaurant Id you want to get data for.



Now put the desired API URL from which you want to get data. In this example we have used the following API to get the menus

  *     * <https://ws-api.toasttab.com/menus/v2/menus>



The final request will look something like this:



You can enable this request and save the API. Click **Run Test**.

You should receive a _(200 OK)_ response, with data returning from the API. This means the API request has successfully contacted Toast and is transferring data.



* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31113088917907)

---

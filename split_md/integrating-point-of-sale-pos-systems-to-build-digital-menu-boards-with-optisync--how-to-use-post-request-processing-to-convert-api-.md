### How to Use Post-Request Processing to Convert API Data

When retrieving data from your POS system, it may not initially show up exactly the way you'd like, or you might want to add some functionality, such as the ability to display SOLD OUT for items out of stock.

For example, prices may display as whole numbers (i.e. 1299 instead of $12.99). That's where the "Post-request" tab comes in - this allows changes to be made to the data after it comes in. This will require some basic coding to use.

Take the example of the price display from earlier. How would we convert a number like 1299 to display as $12.99, and make that piece of code extensible to any similar display errors (e.g. 1899 instead of $18.99)?



For this common example, this piece of JavaScript code should solve your issue.
    
    
    let {data, headers, status} = os.context.get("response");  
    temp_data = data.elements  
    for (let object of temp_data) {  
            object.price = '$' + (object.price*.01);  
            if (object.available == true)  
                  {object.soldout=0;}  
                else {object.soldout=1;}  
        }  
    return temp_data

This will fix the returned data, allowing it to display properly. It will also allow for creation of SOLD OUT and strike through for when items are out of stock.



**NOTE:** Enabling and configuring a WebHook allows near real-time updating of the data pulled from your API. If you plan to keep track of store inventory using your digital signs, we recommend setting one up. You will need to input the provided WebHook key into your API to set this up.  
---  
  
* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31860170199955)

---

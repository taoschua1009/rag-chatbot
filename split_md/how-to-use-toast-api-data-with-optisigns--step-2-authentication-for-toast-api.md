## Step 2: Authentication for Toast API

For Toast API authentication, we will first need to pass the POST request to get the authentication token. The authentication token is then used to pass in the API request to get the data from Toast menus, orders etc. 

This authentication process will be handled using Pre-request processing with OptiSigns' API request. For more information about Pre-request processing and API requests in general, please check [here](https://support.optisigns.com/hc/en-us/articles/22875592994195).

In the Pre-request processing stage, the OptiSigns API calls the authentication API to get the necessary token, and sets it to the context of the API request.

In this example, the token is set to the context variable "authorization". When the API request is made, it will be able to use the authentication token. Below is a screenshot of this example in practice.



Use this code snippet (with the data obtained earlier filling in the "xxx"s) to
    
    
    const body = {  
    "clientId": "xxx",  
    "clientSecret": "xxx",  
    "userAccessType": "xxx"  
    };  
    const {data, headers} = await os.postRequest("https://[toast-api-hostname]/authentication/v1/authentication/login", body );  
    const token = os.getValue(data.token.accessToken);  
    os.context.set("authorization", os.getValue(token));

* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/31113088917907)

---

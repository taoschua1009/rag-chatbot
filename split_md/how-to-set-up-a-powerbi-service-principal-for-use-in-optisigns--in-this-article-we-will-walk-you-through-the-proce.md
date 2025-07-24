### In this article, we will walk you through the process of setting up a service principal for PowerBI in Microsoft Azure, and connecting it to OptiSigns.

  * Creating an Entra App in Microsoft Azure
  * Enable PowerBI Service Admin Settings
    * Add the Service Principal to a Workspace
  * Authenticating OptiSigns via Service Principal
  * Getting PowerBI onto a Screen



Using a PowerBI service principal with app registration is a preferred option for companies with strict information security rules that don't want to use individual user accounts for PowerBI integration. 

This reduces headaches in situations when:

  * There is a position or permission change of a user and authentication needs to be performed again by a different user.
  * A prolonged authentication token period cannot be set for individual users, and you will need to reauthorize and refresh the token every couple of months.



Using a PowerBI service principal, the authentication tokens are associated with a registered app instead of a user. This allows you to set a longer validity time for the authentication token and avoids more frequent re-authorization. Using service principal with App registration for Power BI integration is supported well with OptiSigns.

**NOTE:** This feature is only available to customers on an **Enterprise** plan.  
---  
  
* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/32860569148819)

---

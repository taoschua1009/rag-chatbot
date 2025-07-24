## Installing a Root Certificate on Chrome-Based Web Browsers

Depending on the operating system, Chrome will use the system-wide certificates (such as the ones installed above) or its own certificates. If you are having trouble getting a system-wide certificate to work for your internal website, you may wish to try directly installing a root certificate to Chrome (or any Chromium browser) directly.

To begin, open the **Settings** tab in the Chrome browser.



Next, click **Privacy and security** **→ Security → Manage Certificates**

****

This will open the Certificates manager. You'll need to add your internal website certificate as an authority. Here, click the **Trusted Root Certification Authorities** tab, then click **Import**.



This will open the Certificate Import Wizard. Click **Browse** and locate the certificate necessary for your internal website. Then, click **Next**.

****

On the next screen, **Place all certificates in the following store** and make sure it's "Trusted Root Certification Authorities". Then hit **Next**.

****

Now you'll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting **Finish**.

****

Congratulations, you've installed your root certificate on your Chrome browser.

* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/35184720136595)

---

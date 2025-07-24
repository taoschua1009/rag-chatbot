### Command Line Installation

On MacOS, you can also use the Terminal to directly install the Certificate. Simply type in these commands:

**Use the following command to add a certificate:**
    
    
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain "new-root-certificate"

**Use the following command to remove a certificate:**
    
    
    sudo security delete-certificate -c "name of existing certificate"

* * *

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/35184720136595)

---

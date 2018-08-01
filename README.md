# get-namecheap-zone-file

Tries to get your DNS Zone File from NameCheap.

Uses Selenium + Firefox + Xvfb + Docker to login and scrape the DNS info.

Optional: includes tools and instructios to then create and import that zone to AWS Route 53.

## Prerequisites

  * Bash
  * Docker


## Usage

1. Clone this repository:

    ```
    git clone git@github.com:facetdigital/get-namecheap-zone-file.git
    ```

2. Build the docker container:

    ```
    cd get-namecheap-zone-file
    ./get-zone setup
    ```

3. Optionally set your AWS credentials if you want to work with Route 53.

    ```
    vi .env               # Optional: Replace the TODO values if you want to use Route 53
    ```

4. If you are using Docker on macOS, you need to set up file sharing for the project directory. Click the Docker icon > Preferences > File Sharing and add the full path of this project.

5. Run the script:

    ```
    ./get-zone run <namecheap_username> <namecheap_password> <domain>
    ```

6. Cross-fingers you don't get CAPTCHA'd.


## Import Zone to Route 53

If you made it this far, you can copy that zone file output and paste it into a text file in this directory. Then run bash in the container to get access to the `cli53` tool. Assuming you setup your AWS credentials in Step 3, you can use that to mange your Route 53 account, including creating a new hosted zone and importing this zone file to it. E.g.:

    ```
    cli53 list                 # List your current set of zones
    cli53 export example.com   # export an existing zone file as a backup
    ```

To create and import this zone file to Route 53:

    ```
    cli53 create example.com                           # replace example.com with your domain
    cli53 import example.com --file example.com.zone   # the file you saved your NameCheap zone data to
    ```

For more info on `cli53`, see: https://github.com/barnybug/cli53

This Docker image also has `dns_compare` installed, which can be used to compare your zone file against a server. Use it to compare your extracted NameCheap zone file to the NameCheap server to make sure it is the same. And then to the Route 53 nameserver - it should be the same too. That's how you know they are identical before you flip the switch at NameCheap to point to Route 53 nameservers. (ProTip: Set your NS record TTLs at NameCheap to be low before you start all this, then set them back up to be high in Route 53 after all is well.) For more info on `dns_compare` see: https://github.com/joemiller/dns_compare

## TODO

  * [ ] Make a Chrome Extension version of this you can run when already logged in.
  * [ ] Make it call Route 53 API to upload zone file. One command to migrate from NameCheap to Route 53!


## Credits

Orignal core script from:

https://gist.github.com/judotens/151341f04b37ffeb5b59

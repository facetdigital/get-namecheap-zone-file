# get-namecheap-zone-file

Tries to get your DNS Zone File from NameCheap.

Uses Selenium + Firefox + Xvfb + Docker to login and scrape the DNS info.

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

3. Run the script:

    ```
    ./get-zone run <namecheap_username> <namecheap_password> <domain>
    ```

4. Cross-fingers you don't get CAPTCHA'd.

## TODO

  * [ ] Make a Chrome Extension version of this you can run when already logged in.
  * [ ] Make it call Route 53 API to upload zone file. One command to migrate from NameCheap to Route 53!

## Credits

Orignal core script from:

https://gist.github.com/judotens/151341f04b37ffeb5b59

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

3. Copy the `.env.example` file to `.env`, and optionally set your AWS credentials if you want to work with Route 53.

    ```
    cp .env.example .env
    vi .env               # Optional: Replace the TODO values if you want to use Route 53
    ```

4. Run the script:

    ```
    ./get-zone run <namecheap_username> <namecheap_password> <domain>
    ```

5. Cross-fingers you don't get CAPTCHA'd.


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

## TODO

  * [ ] Make a Chrome Extension version of this you can run when already logged in.
  * [ ] Make it call Route 53 API to upload zone file. One command to migrate from NameCheap to Route 53!


## Credits

Orignal core script from:

https://gist.github.com/judotens/151341f04b37ffeb5b59

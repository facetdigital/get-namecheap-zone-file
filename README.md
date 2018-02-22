Tries to get your DNS Zone File from NameCheap. Uses Selenium + Firefox + Xvfb + Docker login and scrape the DNS info.

## Usage:

1) Build the docker container:

  `./get-zone setup`

2) Run the script:

  `./get-zone run <namecheap_username> <namecheap_password> <domain>`

3) Cross-fingers you don't get CAPTCHA'd.

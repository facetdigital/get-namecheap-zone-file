# get-namecheap-zone-file

Tries to get your DNS Zone File from NameCheap.

Uses Selenium + Firefox + Xvfb + Docker to login and scrape the DNS info.

## Prerequisites

- Bash
- Docker

## Usage

0. Enable TOTP 2FA on your Namecheap account to avoid an email challenge.

1. Clone this repository:

   ```
   git clone git@github.com:facetdigital/get-namecheap-zone-file.git
   ```

2. Build the docker container:

   ```
   cd get-namecheap-zone-file
   ./get-zone setup
   ```

3a. Run the script:

```
./get-zone run <domain>
```

3b. Re-run repeatedly until it works. Yeah. Namecheap inconsistently send the TOTP challenge page to Selenium, or the Python code is badly done.

4. Copy the zone output to a .zone file

## Import Zone

### Cloudflare

You can simply drag the zone file into Cloudflare's DNS page and import it.

### Route 53

Run bash in the container to get access to the `cli53` tool. You can use that to mange your Route 53 account, including creating a new hosted zone and importing this zone file to it. e.g.:

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

## dns_compare

This Docker image also has `dns_compare` installed, which can be used to compare your zone file against a server. Use it to compare your extracted NameCheap zone file to the NameCheap server to make sure it is the same. And then to the Route 53 nameserver - it should be the same too. That's how you know they are identical before you flip the switch at NameCheap to point to Route 53 nameservers. (ProTip: Set your NS record TTLs at NameCheap to be low before you start all this, then set them back up to be high in Route 53 after all is well.)

For more info on `dns_compare` see: https://github.com/joemiller/dns_compare

## TODO

- [ ] Make a Chrome Extension version of this you can run when already logged in.

## Credits

Original core script from: https://gist.github.com/judotens/151341f04b37ffeb5b59

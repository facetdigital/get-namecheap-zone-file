# Originally by Judotens Budiarto (https://github.com/judotens)
#   See: https://gist.github.com/judotens/151341f04b37ffeb5b59
#
# Modified by Facet Digital, LLC to:
#   * Handle the newer bot-wait page
#   * Catch/warn about CAPTCHA (cannot do much about it)
#   * Add some narrative printouts
#   * Wrap with Docker
#

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
except:
    print "pip install selenium dulu"

import json
import sys
import time

def get_advanced_dns_info(username, password, domain):
    loginform_timeout = 60

    fp = webdriver.FirefoxProfile()
    fp.set_preference("devtools.jsonview.enabled", False)

    print "Starting headless browser"
    browser = webdriver.Firefox(firefox_profile=fp, firefox_options=options)

    print "Requesting Advanced DNS page"
    browser.get('https://ap.www.namecheap.com/Domains/DomainControlPanel/%s/advancedns' % str(domain))

    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//fieldset[@class='loginForm']//input[@name='LoginPassword']"))
        WebDriverWait(browser, loginform_timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for correct page to load"
        sys.exit(1)

    print "Filling out login form"
    elem = browser.find_element_by_class_name("loginForm").find_element_by_name('LoginUserName')
    elem.value = str(username)
    elem = browser.find_element_by_class_name("loginForm").find_element_by_name('LoginPassword')
    elem.value = str(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    print "Filling out 2FA code"
    two_factor_code = raw_input("2FA Code: ")
    browser.get('https://www.namecheap.com/twofa/totp')
    time.sleep(5)
    elem = browser.find_element_by_xpath("//form[@class='gb-totp-form']//input")
    elem.value = str(two_factor_code)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    print "Getting the DNS info as JSON"
    browser.get('https://ap.www.namecheap.com/Domains/dns/GetAdvancedDnsInfo?domainName=%s' % str(domain))
    isi = browser.find_element_by_tag_name('body').text
    browser.quit()

    js = json.loads(isi)

    print "Here is your DNS Zone File:\n\n"
    return js

def parse_dns_info(dns_info):
    records = dns_info['Result']['CustomHostRecords']['Records']
    items = []
    for record in records:
        host = str(record['Host'])
        if record['RecordType'] == 1: tipe = 'A'
        if record['RecordType'] == 2: tipe = 'CNAME'
        if record['RecordType'] == 3: tipe = 'MX'
        if record['RecordType'] == 5: tipe = 'TXT'

        value = str(record['Data'])
        ttl = str(record['Ttl'])
        priority = str(record['Priority'])
        active = record['IsActive']
        if not active: continue
        new_value = value
        if tipe == 'MX': new_value = "%s %s" % (str(priority), str(value))
        if tipe == 'TXT': new_value = "\"%s\"" % (str(value))

        items.append([host,ttl,"IN", tipe, new_value])

    return items

if __name__ == "__main__":
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    try:
        dns_info = get_advanced_dns_info(username, password, sys.argv[1])
    except Exception, e:
        print str(e)
        sys.exit("Usage: %s <domain_to_check>" % str(sys.argv[0]))

    print "$ORIGIN %s." % (str(sys.argv[1]))
    zones = parse_dns_info(dns_info)

    for zone in zones:
        print "\t".join(zone)

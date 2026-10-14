# LAB 6: Phishing URL Detection
# Aim: Check a URL for common phishing indicators. This is a simple heuristic, not a verdict.

from urllib.parse import urlparse
import ipaddress

url = input("Enter URL to check: ").strip()
candidate = url if "://" in url else "http://" + url
parsed = urlparse(candidate)
host = parsed.hostname or ""
indicators = []

if not host:
    indicators.append("URL has no valid hostname")
else:
    if any(word in url.lower() for word in ["login", "verify", "secure", "update", "password"]):
        indicators.append("Contains a commonly abused keyword")
    try:
        ipaddress.ip_address(host)
        indicators.append("Uses an IP address instead of a domain name")
    except ValueError:
        if len(host.split(".")) > 3:
            indicators.append("Has an unusually large number of subdomains")
    if "@" in parsed.netloc:
        indicators.append("Contains @ in the network location")
    if parsed.scheme != "https":
        indicators.append("Does not use HTTPS")

if indicators:
    print("Warning: Potentially suspicious URL")
    for indicator in indicators:
        print("-", indicator)
else:
    print("No listed indicators found. This does not guarantee the URL is safe.")

**Note**: the api key **IS NOT** the selfApiKey that can be found in traces.

To capture the api key there are a few options;

* Capture with V2 firmware: If you have V2 firmware and are using the earlier version of this component, the apikey is visible in the HA logs at startup (part of the "user online response") when debug is turned on (see below)

* Capture during pairing using a browser: You can use the method described [here](https://blog.ipsumdomus.com/sonoff-switch-complete-hack-without-firmware-upgrade-1b2d6632c01). Despite this guide being quite old and for older firmware, the early part where the api_key is uncovered still works. Unfortunately this is only visible this way during pairing

* Capture during pairing using a network trace tool. I use 'tcpdump' running on an OpenWRT router. This is the route which needs the most technical expertise, but seems to be the only viable way in certain circumstances.
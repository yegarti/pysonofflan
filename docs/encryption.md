# Encryption

## When is it used?

All known Sonoff devices running Firmware 3+ have encryption implemented unless they are running in DIY mode.

DIY mode is a feature enabled on some devices, typically those branded DIY or R3. It is enabled using a jumper on the mainboard.

For devices with encryption enabled, the api_key is needed to read the device status or to operate the device using the API. The device, however, can be discovered without the key. 

## Obtaining the api_key

**Note**: the api key **IS NOT** the selfApiKey that can be found in traces.

The api_key is not designed to be captured by users and is not available in any user interfaces.

To capture the api_key there are a number of options;

* Capture with V2 firmware: If you have V2 firmware and are using the earlier version of this component/package, the api_key is visible in the debug logs at startup (part of the "user online response" message)

* Capture during pairing using a browser: You can use the method described [here](https://blog.ipsumdomus.com/sonoff-switch-complete-hack-without-firmware-upgrade-1b2d6632c01). Despite this guide being quite old and for older firmware, the early part where the api_key is uncovered still works for some devices. Unfortunately this is only visible this way during pairing

* Capture during pairing using a network trace tool. 'tcpdump' is a popular tool and can be run on an OpenWRT router. This is the route which needs the most technical expertise, but seems to be the only viable way in certain circumstances.

1. Connect to the router with ssh or telnet from your PC
2. Connect your mobile to the router SSID
3. Execute this command in the WRT router: “tcpdump -s 0 -vvv -i eth1 -w outputfile”
4. Register the sonoff in the eWeLink App
5. Stop the tcpdump (Ctrl-C)
6. Excute the command “grep apikey outputfile” in the router
7. You will get the apikey like this:
{“type”:1,“deviceid”:“xxxxxxxxxx”,“apikey”:"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",“rptInfo”:{“code”:3100,“arg”:"{“rstReason”:0}"},“sequence”:“0845895318697”}^/G

* Capture via Charles Proxy

This is a method which shows how to do it
https://community.home-assistant.io/t/new-custom-component-sonoff-lan-mode-local-with-stock-firmware/88132/99?u=mattsaxon

It's based on these instructions here;
https://community.hubitat.com/t/sonoff-ewelink-via-homebridge-node/3753

Thanks to @SuperMario
# hass-services-bridge
Call Home Assitant services using POST request without headers. Best way for call HASS services from IFTTT
# Quick start
Available [here](quick-start.md)
# IFTTT
If you tried to call the Home Assitant service from IFTTT (for example, using the Google Assitant trigger), you know that in the IFTTT Webhooks request you cannot specify request headers, and Home Assitant requires a header for authorization. My program is a bridge that accepts a request without headers, where all the data is transferred to JSON and passed to Home Assitant.
# Security
In the settings of my bridge, you can allow only certain services to be called, thereby increasing security. But no one forbids you to specify a setting that allows you to call all services. SSL is supported.
There is no protection against brute force. I would be grateful for the revision.
# Configuration
The configuration is stored in the file `settings.ini`.
An example configuration is available [here](settings.ini).

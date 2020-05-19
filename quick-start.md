# Quick start
0. Install Python3 and python3-pip. And get Home Assitant long-live access token.
1. Clone this repository(or download .zip): `git clone https://github.com/allmazz/hass-services-bridge.git`
2. Enter the directory with the downloaded repository, and install requirements: `pip3 install -r requirements.txt`
3. Edit `settings.ini`. Set your parameters.
4. Run `hass-services-bridge.py`: `python3 hass-services-bridge.py` for Linux,
`python hass-services-bridge.py` for Windows
5. Send POST request to `http(s)://your_server:port/hass` with data type `application/json`, and data `{"token": "your_token(in config->server->token)", "service": "script.example(HASS service)"}`. Anser can be `OK` when successful, `invalid token` when token is invalid, `service not allowed` when service not allowed, `invalid json keys` when JSON not contain keys `token` and `service`.

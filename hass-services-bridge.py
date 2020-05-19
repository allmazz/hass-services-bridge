from bottle import route, run, request
import configparser
from requests import post

config = configparser.ConfigParser()
config.read("settings.ini")
allow_all = True
if config['services']['allow_all'] == 'no':
    global allowed
    allowed = config['services']['allowed'].split(',')
    allow_all = False
elif config['services']['allow_all'] == 'yes':
    allow_all = True
else:
    print('Invalid services->allow_all. Set "yes" or "no"')
    exit(1)

@route('/hass', method='POST')
def water():
    request.content_type = 'application/json'
    if 'service' in request.json and 'token' in request.json:
      if request.json['token'] == config['server']['token']:
         if not allow_all and request.json['service'] not in allowed:
            return "service not allowed"
         headers = {'Authorization': 'Bearer ' + config['hass']['token'], 'content-type': 'application/json'}
         ha_req = post(config['hass']['url'] + request.json['service'].replace('.', '/'), headers=headers)
         return "OK"

      else:
        return "invalid token"
    else:
        return "invalid json keys"


if config['server']['ssl'] == 'no':
    run(host=config['server']['host'], port=int(config['server']['port']))
elif config['server']['ssl'] == 'yes':
    from bottle import ServerAdapter, default_app
    from cheroot.ssl.builtin import BuiltinSSLAdapter
    import cheroot.wsgi as wsgi
    from beaker.middleware import SessionMiddleware
    import ssl


    class SSLCherryPyServer(ServerAdapter):
        def run(self, handler):
            server = wsgi.Server((self.host, self.port), handler)
            server.ssl_adapter = BuiltinSSLAdapter(config['server']['cert'], config['server']['key'])
            server.ssl_adapter.context.options |= ssl.OP_NO_TLSv1
            server.ssl_adapter.context.options |= ssl.OP_NO_TLSv1_1
            try:
                server.start()
            finally:
                server.stop()


    session_opts = {
        "session.type": "file",
        "session.cookie_expires": True,
        "session.data_dir": "./data",
        "session.auto": True,
    }
    app = SessionMiddleware(default_app(), session_opts)
    run(app=app, host=config['server']['host'], port=int(config['server']['port']), server=SSLCherryPyServer)
else:
    print('Invalid server->ssl. Set "yes" or "no"')
    exit(1)

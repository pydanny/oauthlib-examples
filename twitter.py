import ConfigParser

from oauthlib.oauth import OAuth1aClient
from oauthlib import parameters
from oauthlib import signature
from oauthlib import utils

config = ConfigParser.ConfigParser()
config.read('config.cfg')

client_key = config.get('twitter', 'client_key')
client_secret = config.get("twitter", 'client_secret')

def main():
    
    params = {
            u'oauth_consumer_key':unicode(client_key),
            u'oauth_nonce':unicode(utils.generate_nonce()),
            u'oauth_signature_method':u'HMAC-SHA1',
            u'oauth_timestamp':unicode(utils.generate_timestamp()),
            u'oauth_token':unicode(client_secret),
            u'oauth_version':u"1.0"
        
        }
    ordered_params = parameters.order_oauth_parameters(params)
    normalized_parameters=signature.normalize_parameters(ordered_params)
    print normalized_parameters

    """
    base_string = signature.construct_base_string(
        http_method=u"POST",
        base_string_uri=u"api.twitter.com",
        normalized_encoded_request_parameters=normalized_parameters
    )
    print base_string
    """

if __name__ == '__main__':
    main()
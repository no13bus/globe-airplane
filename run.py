from Pubnub import Pubnub


## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key='pub-c-574982bb-d7cc-4ec1-9683-fe1d89b144ad', subscribe_key='sub-c-9a43842c-a77a-11e4-85d5-0619f8945a4f',
                secret_key='sec-c-NTk5NzBiYzYtZjAwNS00ODdiLWIwNjUtMzRkYTk3Mjg3N2E0', ssl_on=False)
channel = 'jqh'
message = {"a":"oooo"}

# Asynchronous usage


# print pubnub.publish(channel, message)


def callback(message):
    print message

for x in xrange(1,10):
    pubnub.publish(channel, message, callback=callback, error=callback)

from Adafruit_IO import Client

ADAFRUIT_IO_KEY = 'aio_DsnO87BT3KLJ5mdsLQ5BS7RXp0hY'
ADAFRUIT_IO_USERNAME = 'dangnguyen'
FEED_NAME = 'nmdk-1-fanstatus-1'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

aio.send(FEED_NAME,'ON')
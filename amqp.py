import pika, os, urlparse, sys
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

url_str = os.environ.get('CLOUDAMQP_URL','amqp://rjrhiarp:aqSxe3JZeQs63jmgBu3AZZVTlzcqvKmJ@turtle.rmq.cloudamqp.com/rjrhiarp')
url = urlparse.urlparse(url_str)
params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
    credentials=pika.PlainCredentials(url.username, url.password))

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):


    printer.inverseOn()
    printer.println(' ' + '{:<31}'.format("TXT MESSAGE"))
    printer.inverseOff()

    printer.println(body)

    printer.feed(3)

    print("complete")
    print " [x] Received %r" % (body)

# set up subscription on the queue
channel.basic_consume(callback,
    queue='hello',
    no_ack=True)

try:

    channel.start_consuming() # start consuming (blocks)

except KeyboardInterrupt:

    print "Break detected"
    channel.stop_consuming()

connection.close()

sys.exit()
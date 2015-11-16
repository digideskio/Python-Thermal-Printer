import pika, os, urlparse, sys
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

url_str = os.environ.get('CLOUDAMQP_URL','amqp://jgdpgvfl:QeI3NjevvIW8zh5R3BOiOVT9meu1U8L2@moose.rmq.cloudamqp.com/jgdpgvfl')
url = urlparse.urlparse(url_str)
params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
    credentials=pika.PlainCredentials(url.username, url.password))

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

channel.basic_publish(exchange='', routing_key='hello', body='Hello CloudAMQP!')
print " [x] Sent 'Hello World!'"
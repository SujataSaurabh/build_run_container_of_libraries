#!/usr/bin/python3
import sys, os
import traceback
import logging
from configparser import ConfigParser
import pika
# This program is a consumer script for RabbitMQ 

def que_connect(config_filename):
    from pika import BlockingConnection, ConnectionParameters, PlainCredentials
    # instantiate
    config = ConfigParser()
    # parse existing file
    config.read(config_filename)

    queue_user = config.get('rabbitmq-user', 'username')
    queue_pass = config.get('rabbitmq-pass', 'password')
    rabbitmq_host = config.get('rabbitmq-hostname', 'rabbitmq_host')
    pika_credentials = PlainCredentials(queue_user, queue_pass)
    pika_dsn = ConnectionParameters(rabbitmq_host, credentials=pika_credentials)
    try:
        with BlockingConnection(pika_dsn) as Q:
            channel = Q.channel()
#            channel = connection.channel()
            channel.exchange_declare(exchange='test', exchange_type='fanout')
            result = channel.queue_declare(queue='', exclusive=True)
            queue_name = result.method.queue
            channel.queue_bind(exchange='test', queue=queue_name)
            def callback(ch, method, properties, body):
                logging.info(f" [x] {body.decode()}")
            logging.info(' [*] Waiting for messages. To exit press CTRL+C')
            channel.basic_consume(
                queue=queue_name, on_message_callback=callback, auto_ack=True)
            channel.start_consuming()
    
    except Exception as e:
        traceback.print_exception(*sys.exc_info())
        print(e)
if __name__ == "__main__":
  # provide a config file with all the credentials to login to RabbitMQ
  config_filename = sys.argv[1]
  que_connect(config_filename)



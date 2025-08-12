#!/usr/bin/env python3
# coding=utf-8

import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (creates it if it doesn't exist)
channel.queue_declare(queue='hello1', durable=True, arguments={'x-queue-type': 'quorum'})

# Publish a message
channel.basic_publish(
    exchange='',
    routing_key='hello1',
    body='Hello Netology!'
)

print(" [x] Sent 'Hello Netology!'")

# Close connection
connection.close()

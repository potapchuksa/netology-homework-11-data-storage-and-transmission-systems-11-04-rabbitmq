#!/usr/bin/env python3
# coding=utf-8

import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', virtual_host='myvhost'))
channel = connection.channel()

# Declare a queue (creates it if it doesn't exist)
channel.queue_declare(queue='hello3', durable=True, arguments={'x-queue-type': 'quorum'})

# Publish a message
channel.basic_publish(
    exchange='',
    routing_key='hello3',
    body='Hello Netology!'
)

print(" [x] Sent 'Hello Netology!'")

# Close connection
connection.close()

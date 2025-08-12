#!/usr/bin/env python
# coding=utf-8

import pika

# Establish connection to the RabbitMQ server running on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Create a channel for communication
channel = connection.channel()

# Declare a queue named 'hello'
# This ensures the queue exists before we try to consume from it
channel.queue_declare(queue='hello')


# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    # Print the received message (body is bytes, %r shows raw representation)
    print(" [x] Received %r" % body)


# Set up consumer: listen to the 'hello' queue and call 'callback' when a message arrives
# auto_ack=False means manual acknowledgment is required (but not sent in this code)
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=False
)

# Start consuming messages (this will block and wait for messages indefinitely)
channel.start_consuming()

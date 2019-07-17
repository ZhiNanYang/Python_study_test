import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.110.110'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()

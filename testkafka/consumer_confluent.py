from confluent_kafka import Consumer
from time import sleep


class ConsumerConfluent:
    broker = ""
    topic = ""
    group_id = "consumer-1"

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic

    def start_listener(self):
        consumer_config = {
            'bootstrap.servers': self.broker,
            'group.id': self.group_id,
            'auto.offset.reset': 'largest',
            'enable.auto.commit': 'false',
            'max.poll.interval.ms': '86400000'
        }

        consumer = Consumer(consumer_config)
        consumer.subscribe([self.topic])

        try:
            while True:
                msg = consumer.poll(0)
                if msg != None:
                    consumer.commit()
                    return msg

        except KeyboardInterrupt:
            print("Aborted by user...")
        finally:
            # print("closing consumer")
            consumer.close()


example_consumer = ConsumerConfluent()

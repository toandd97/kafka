from kafka import KafkaConsumer, consumer
from time import sleep
import json


class MessageConsumer:
    broker = ""
    topic = ""
    group_id = ""
    logger = None

    def __init__(self, broker, topic, group_id):
        self.broker = broker
        self.topic = topic
        self.group_id = group_id

    def activate_listener(self):
        consumer = KafkaConsumer(bootstrap_servers=self.broker,
                                 group_id='my-group',
                                 consumer_timeout_ms=60000,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')))

        consumer.subscribe(self.topic)
        print("consumer is listening....")
        try:
            for message in consumer:
                print("received message = ", message)

                #committing message manually after reading from the topic
                consumer.commit()
        except KeyboardInterrupt:
            print("Aborted by user...")
        finally:
            consumer.close()


# Running multiple consumers
# broker = 'localhost:9092'
# topic = 'receive-data'
# group_id = 'consumer-1'

# consumer1 = MessageConsumer(broker,topic,group_id)
# consumer1.activate_listener()

# consumer2 = MessageConsumer(broker,topic,group_id)
# consumer2.activate_listener()
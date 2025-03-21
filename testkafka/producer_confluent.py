from datetime import datetime, timedelta
from time import sleep
from confluent_kafka import Producer
import json

class ExampleProducer:
    broker = "192.168.5.31:9092,192.168.5.32:9092,192.168.5.33:9092,192.168.5.34:9092,192.168.5.35:9092"
    # broker = "localhost:9092"
    # topic = 'my-topic'
    topic = "factory-process-update-profile-brcast-v2"

    producer = None

    def __init__(self):
        self.producer = Producer({
            "bootstrap.servers": self.broker,
            "socket.timeout.ms": 100,
            "api.version.request": "False",
            "broker.version.fallback": "0.9.0",
        }
        )

    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print("Message delivery failed: {}".format(err))
        else:
            print("Message delivered to {} [{}]".format(
                msg.topic(), msg.partition()))

    def send_msg_async(self, msg):
        print("Send message asynchronously")
        print(msg)
        self.producer.produce(
            self.topic,
            value=json.dumps(msg).encode("utf-8"),
            on_delivery=self.delivery_report,
        )
        self.producer.flush()

    def send_msg_sync(self, msg):
        print("Send message synchronously")
        self.producer.produce(
            self.topic,
            msg,
            callback=lambda err, original_msg=msg: self.delivery_report(
                err, original_msg
            ),
        )
        self.producer.flush()


# SENDING DATA TO KAFKA TOPIC
example_producer = ExampleProducer()
_now = datetime.utcnow()
end_time = _now + timedelta(days=30)

data = {
        "merchant_id" : "57d559c1-39a1-4cee-b024-b953428b5ac8",
        "profile_id" : "73cde275-18ef-4a04-b3e5-0c8dcad9b5da",
        "product_id" : "65783ccafdfa7221c0d89bc7",
        "product_holding_id" : "1",
        "data_datetime" : 1731656689,
        "product_holding_data" : {
            "name" : "VITA - Sống Thịnh Vượng",
            "product_line" : "65698fd7f4c905f2797ae26e",
            "product_code" : "IL1",
            "_dyn_so_the_1718703292140" : "BV23456",
            "open_day" : "03/05/2024",
            "_dyn_ngay_het_han_1718703663701+dmy" : "03/05/2027",
            "_dyn_ngay_kich_hoat_1718703714219+dmy" : "03/05/2024",
            "_dyn_the_chinh_phu_1718703797064" : "Thẻ chính",
            "_dyn_han_muc_the_1718703861115" : 100000000,
            "_dyn_dropdown_multiple_select_1701831825705" : [
            ],
            "maturity_date" : "11/10/2024",
            "product_status" : "Activate"
        },
        "tracking_code" : "672072330ba2b4f5704ca0cc"
    }

example_producer.send_msg_async(data)
sleep(5)

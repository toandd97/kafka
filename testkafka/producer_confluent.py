from datetime import datetime, timedelta
from confluent_kafka import Producer
import json


class ExampleProducer:
    # broker = "192.168.5.31:9092,192.168.5.32:9092,192.168.5.33:9092,192.168.5.34:9092,192.168.5.35:9092"
    broker = "localhost:9092"

    # topic = 'dynamic-segment-result-caculate-profile'
    # topic = 'dynamic-segment-status-calculate'
    # topic = 'mobio-etl-product-holding-history'
    # topic = 'dynamic-segment-result-caculate-profile'
    # topic = "dyn-event-status-register"
    # topic = "mobio-etl-upsert-product-holding"

    # topic = "profiling-unify-or-insert"
    # topic = "mobio-etl-upsert-product-holding-company"
    # topic = "mobio-etl-product-holding-history-company"
    # topic = "mobio-etl-product-holding-history"
    # topic = "event-set-tag-interactive"
    # topic = "profile-event-dynamic-p1"
    topic = "dyn-event-auto-scale"
    # topic = "segment-test-restart-consumer"
    # topic = "segment-validate-profile"
    # topic = "segment-result-caculate-profile"
    # topic = "rfm-result-caculate-profile"
    # DYNAMIC_SEGMENT_STATUS_JB = 'dynamic-segment-status-calculate'
    # DYNAMIC_SEGMENT_RESULT_CACULATE_PROFILE = 'dynamic-segment-result-calculate-profile'
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

# data = {
#     "status": "FALSE",
#     "message": "Đăng ký không thành công",
#     "data_callback": {
#         "merchant_id": "1b99bdcf-d582-4f49-9715-1b61dfff3924",
#         "event_key": "ten_cua_dynamic_event_test_14_1716342257"
#     }
# }


for index, _ in enumerate(range(1)):
    print(index)
    data = {
        "code": "success",
        "data": {
            "merchant_id": [
                "4bccc926-563d-4ecc-838d-0970997f0f86"
            ],
            "profile_id": "35ef22f5-424c-4b4a-98bc-dbeb2b4f226e +" + str(index),
        },



        "data_callback": {
            "event_key": "test_validate_field_1722223333",
            "event_data": {
                "str": 123,
                "int": "5000000",
                "double": "123456789876543.1234",
                "date": "2022-01-01",
                "datetime": 1641024000.0,
                "boolean": True
            },
            "merchant_id": "4bccc926-563d-4ecc-838d-0970997f0f86",
            "tracking_code": "zcLQWn9xMzaB-oqBYnWT2_t1",
            "dynamic_event_id": "66a70ae54807c481844ff5352"
        }
    }


    example_producer.send_msg_async(data)

# PYTHONPATH=./ python3.11 test.py >> $log_dir/test.out 2>&1
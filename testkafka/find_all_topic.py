from confluent_kafka import Consumer, KafkaException, KafkaError

# Cấu hình Kafka Consumer
conf = {
    'bootstrap.servers': 'kafka1:9092,kafka2:9092,kafka3:9092,kafka4:9092,kafka5:9092',
    'group.id': 'search-group',
    'auto.offset.reset': 'earliest',  # Đọc từ đầu topic
    'enable.auto.commit': False
}

# Chuỗi cần tìm
search_strings = [
    "655536d7-0bb8-417f-af31-98bcbc257a3a",
    "6e95b49d-af33-4603-bb72-43da2bfdeb0a"
]

def consume_and_search(topic):
    """Lắng nghe topic và tìm kiếm chuỗi"""
    consumer = Consumer(conf)
    consumer.subscribe([topic])

    print(f"Đang kiểm tra topic: {topic}")

    try:
        while True:
            msg = consumer.poll(timeout=5.0)  # Chờ tối đa 5 giây
            if msg is None:
                break  # Hết dữ liệu thì thoát
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    break
                else:
                    raise KafkaException(msg.error())

            # Kiểm tra chuỗi trong nội dung tin nhắn
            message_value = msg.value().decode('utf-8', errors='ignore')
            for search_string in search_strings:
                if search_string in message_value:
                    print(f"🔍 Tìm thấy trong {topic}: {message_value}")
                    with open('result.txt', 'a', encoding='utf-8') as f:
                        f.write(f"Topic: {topic}\n")
                        f.write(f"Search String: {search_string}\n")
                        f.write(f"Message: {message_value}\n")
                        f.write("-" * 80 + "\n")

    finally:
        consumer.close()

# Lấy danh sách topic từ Kafka
from confluent_kafka.admin import AdminClient

admin_client = AdminClient({'bootstrap.servers': 'kafka1:9092,kafka2:9092,kafka3:9092,kafka4:9092,kafka5:9092'})
topics = [t for t in admin_client.list_topics(timeout=10).topics.keys() if t.startswith('factory-jb')]

if not topics:
    print("❌ Không tìm thấy topic nào bắt đầu với 'factory-jb'")
else:
    print(f"📌 Tìm thấy {len(topics)} topic: {topics}")

    # Duyệt qua từng topic và tìm kiếm
    for topic in topics:
        consume_and_search(topic)
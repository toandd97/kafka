from confluent_kafka.admin import AdminClient
from kafka import KafkaConsumer

from kafka.admin import NewTopic
from kafka.errors import KafkaError

def get_group_topics(bootstrap_servers='kafka1:9092,kafka2:9092,kafka3:9092,kafka4:9092,kafka5:9092', group_id='segment_process'):
    try:
        # Create admin client
        admin_client = AdminClient(
            bootstrap_servers=bootstrap_servers
        )

        # Create consumer to get group info
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            enable_auto_commit=False
        )

        # Get list of all topics
        topics = admin_client.list_topics()
        
        # Get group info
        group_info = admin_client.list_consumer_groups()
        
        # Get group topics and their details
        group_topics = []
        for topic in topics:
            try:
                partitions = consumer.partitions_for_topic(topic)
                if partitions:
                    topic_info = {
                        'topic_name': topic,
                        'num_partitions': len(partitions),
                        'partition_ids': list(partitions)
                    }
                    group_topics.append(topic_info)
            except Exception as e:
                print(f"Error getting info for topic {topic}: {str(e)}")

        print(f"\nGroup ID: {group_id}")
        print(f"Total topics: {len(group_topics)}")
        print("\nTopic details:")
        for topic in group_topics:
            print(f"\nTopic: {topic['topic_name']}")
            print(f"Number of partitions: {topic['num_partitions']}")
            print(f"Partition IDs: {topic['partition_ids']}")

        consumer.close()
        admin_client.close()

    except KafkaError as e:
        print(f"Kafka error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    get_group_topics()

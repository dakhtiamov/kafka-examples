#!/usr/bin/python3

######### pip3 install kafka-python ##########

from kafka import KafkaClient, SimpleConsumer
from sys import argv
 
class KafkaOperations:
 
        def kafka_connect(self, broker_list):
                try:
                        kafka = KafkaClient(broker_list)
                        return kafka
                except:
                        print("Kafka brokers are unavailable.")
 
        def kafka_consumer(self, connect, consumer_group_id, topic_name):
                consumer = SimpleConsumer(connect, consumer_group_id, topic_name)
                consumer.max_buffer_size=0
                consumer.seek(0,2)
                for message in consumer:
                        print(message)
 
        def print_usage(self, usage_message):
                print(usage_message)
 
def main():
        usage_message = "Usage: ./consumer.py broker_list topic_name consumer_group_id."
        main_consumer = KafkaOperations()
        if len(argv) == 4:
                broker_list = argv[1]
                topic_name = argv[2]
                consumer_group_id = argv[3]
                try:
                        connect = main_consumer.kafka_connect(broker_list)
                        main_consumer.kafka_consumer(connect, consumer_group_id, topic_name)
                except KeyboardInterrupt:
                        connect.close()
                        print("See ya...")
        else:
                main_consumer.print_usage(usage_message)
 
 
if __name__ == "__main__":
        main()
else:
    print("Please, comment this if you need to use it as module")

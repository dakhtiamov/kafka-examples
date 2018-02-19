#!/usr/bin/python3

######### pip3 install kafka-python ##########

from kafka import KafkaClient, SimpleProducer
from sys import argv
 
 
class KafkaOperations:
 
        def kafka_connect(self, broker_list):
                try:
                        kafka_connect = KafkaClient(broker_list)
                        return kafka_connect
                except:
                        print("Kafka brokers are unavailable.")
 
        def kafka_producer(self, connect, topic_name, file_name):
                producer = SimpleProducer(connect, async=True)
                f = open(file_name, "r")
                for line in f:
                        print(line)
                        producer.send_messages(topic_name, bytes(line, "ascii"))
 
 
        def print_usage(self, usage_message):
                print(usage_message)
 
def main():
        usage_message = "Usage: ./producer.py broker_list topic_name file_name."
        main_producer = KafkaOperations()
        if len(argv) == 4:
                broker_list = argv[1]
                topic_name = argv[2]
                file_name = argv[3]
                try:
                        connect = main_producer.kafka_connect(broker_list)
                        main_producer.kafka_producer(connect, topic_name, file_name)
                        connect.close()
                except KeyboardInterrupt:
                        connect.close()
                        print("See ya...")
        else:
                main_consumer.print_usage(usage_message)
 
 
if __name__ == "__main__":
        main()
else:
    print("Please, comment this if you need to use it as module")

from kafka import KafkaProducer


# 发布消息到 Kafka 的 topic
def publish_message(topic, message):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()


# 主函数
if __name__ == "__main__":
    # 定义要发布的消息和目标 topic
    topic = 'yuqing-topic-news'
    message = '{"batchNum": "12345", "otherParam": "value"}'

    # 发布消息到 Kafka
    publish_message(topic, message)



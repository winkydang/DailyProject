from kafka import KafkaConsumer
import requests


# 订阅 Kafka 中的 topic，并获取输入参数
def subscribe_to_topic(topic):
    consumer = KafkaConsumer(topic)  # 使用'KafkaConsumer'类从指定的Kafka topic中获取消息。
    for message in consumer:
        input_params = message.value
        batch_num = input_params.get('batchNum')  # 获取批次号
        # 调用 API 接口并处理结果数据
        process_api_request(input_params, batch_num)


# 调用 API 接口并处理结果数据
def process_api_request(input_params, batch_num):
    # 调用 API 接口 并 传递批次号
    api_url = 'https://api.example.com/api_IT_PSAS_CORP_NEWS_RT'
    payload = {'batchNum': batch_num, 'data': input_params}
    # response = requests.post(api_url, data=input_params)
    response = requests.post(api_url, json=payload)

    # 处理结果数据
    result_data = response.json()
    # 进行进一步的处理、分析或展示
    print(result_data)


# 主函数
if __name__ == "__main__":
    # 订阅特定的 Kafka topic
    topic = 'yuqing-topic-news'
    subscribe_to_topic(topic)




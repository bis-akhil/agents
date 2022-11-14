from kafka import KafkaProducer
from kafka import KafkaConsumer
import time
from Agent import Agent
import json
import threading

producer = KafkaProducer(bootstrap_servers  = '172.17.0.2:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
consumer = KafkaConsumer('lob_data', bootstrap_servers = '172.17.0.2:9092',
                         auto_offset_reset = 'latest')
def produce_order():
    while True:
        new_order = agent.if_order()
        if new_order:
            data = {"agent_id":new_order.agent_id,
                    "buy":new_order.buy,
                    "price":new_order.price,
                    "vol":new_order.vol,
                    "fulfilled":new_order.fulfilled}
            
            producer.send('agent-order',data)
            producer.flush()
            time.sleep(1)

def receive_data():
    for msg in consumer:
        blob = msg.value
        message = json.loads(blob)
        agent.consume_data(message)
        print(message)
        

if __name__ == '__main__':
    agent = Agent(73,100,0.23)
    t_producer = threading.Thread(target=produce_order)
    t_consumer = threading.Thread(target=receive_data)
    t_producer.setDaemon(True)
    t_consumer.setDaemon(True)
    t_producer.start()
    t_consumer.start()
    t_producer.join()
    t_consumer.join()

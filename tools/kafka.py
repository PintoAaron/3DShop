from kafka import KafkaProducer, KafkaConsumer, errors
from config import setting
from .log import Log

settings = setting.AppSettings()

logger = Log(__name__)


class KafkaStreamConsumer:
    
    def __init__(self, topic: str=settings.KAFKA_TOPIC):
        self.topic = topic
        
        
    def consume_data_from_topic(self, callback_func):
        """
        This function consumes data from kafka server
        It takes a callback function as argument
        """
        
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: x.decode('utf-8')
        )
        
        for message in consumer:
            callback_func(message.value)
            


class KafkaStreamProducer:
    
    @classmethod
    def __connect_to_kafka(cls):
        try:
            producer = KafkaProducer(
                bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                value_serializer=lambda x: x.encode('utf-8')
            )
            
            if not producer.bootstrap_connected():
                logger.error(f"{KafkaStreamProducer.__connect_to_kafka.__name__} - Unable to connect to kafka server")
            
            return producer
        
        except errors.NoBrokersAvailable:
            logger.error(f"{KafkaStreamProducer.__connect_to_kafka.__name__} - No Kafka brokers available")
            raise
            
        
        
    
    @classmethod
    def send_data_to_topic(cls, topic: str, message: list):
        producer = cls.__connect_to_kafka()
        
        data = ",".join(message)
        
        try:
            producer.send(topic, value=data)
            producer.flush()
        except errors.KafkaTimeoutError:
            logger.error(f"{KafkaConsumer.send_data_to_topic.__name__} - Timeout error while sending data to kafka server")
        except errors.KafkaError as e:
            logger.error(f"{KafkaConsumer.send_data_to_topic.__name__} - Error while sending data to kafka server")
            logger.exception(e)
        finally:
            producer.close()
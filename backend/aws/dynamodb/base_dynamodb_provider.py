import boto3
from abc import ABC


class BaseDynamodbProvider(ABC):
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

import time
import uuid

from botocore.exceptions import ClientError
from flask import g

from backend.aws.dynamodb.base_dynamodb_provider import BaseDynamodbProvider


class ProjectDynamodbProvider(BaseDynamodbProvider):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name

    def add_item(self, project):
        table = self.dynamodb.Table(self.table_name)
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "user": g.user.get("Username"),
            "title": project.get("title"),
            "description": project.get("description")
        }
        try:
            table.put_item(TableName=self.table_name,
                           Item=item)
        except ClientError as error:
            print(error)
            return False
        return True

    # def delete_item(self, project):
    #     print("Delete item")
    #
    # def update_item(self, project):
    #     print("Update item")

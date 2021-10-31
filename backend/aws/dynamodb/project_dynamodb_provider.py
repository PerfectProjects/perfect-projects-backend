import time
import uuid

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from backend.aws.dynamodb.base_dynamodb_provider import BaseDynamodbProvider


class ProjectDynamodbProvider(BaseDynamodbProvider):
    def __init__(self, table_name):
        super().__init__(table_name)

    def add_project(self, project, user_id):
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "user_id": user_id,
            "title": project.get("title"),
            "description": project.get("description")
        }
        try:
            self.table.put_item(Item=item)
        except ClientError as error:
            print(error)
            return False
        return True

    def get_all_user_projects(self, user_id):
        try:
            result = self.table.query(IndexName="user_id",
                                      KeyConditionExpression=Key("user_id").eq(user_id))
        except ClientError as error:
            print(error)
            return False
        return result

    def delete_project(self, project_id):
        try:
            self.table.delete_item(Key={"id": project_id})
        except ClientError as error:
            print(error)
            return False
        return True

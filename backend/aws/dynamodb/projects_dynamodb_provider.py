import calendar
import datetime
import uuid

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from backend.aws.dynamodb.base_dynamodb_provider import BaseDynamodbProvider


class ProjectsDynamodbProvider(BaseDynamodbProvider):
    def __init__(self):
        super().__init__("projects")

    def add_project(self, project):
        item_id = str(uuid.uuid4())
        current_datetime = datetime.datetime.utcnow()
        current_timetuple = current_datetime.utctimetuple()
        current_timestamp = calendar.timegm(current_timetuple)
        item = {
            "id": item_id,
            "user_id": project.get("author"),
            "title": project.get("title"),
            "brief_description": project.get("briefDescription"),
            "visible": project.get("visible"),
            "timestamp": current_timestamp
        }
        try:
            self.table.put_item(Item=item)
        except ClientError as error:
            print(error)
            return False
        return item_id

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

    def get_project(self, project_id):
        try:
            item = self.table.get_item(Key={"id": project_id})
        except ClientError as error:
            print(error)
            return False
        return item

    def get_projects(self, page):
        limit = 3
        try:
            response = self.table.scan(Limit=limit)
            for x in range(page - 1):
                last_evaluated_key = response.get("LastEvaluatedKey")
                if last_evaluated_key is None:
                    break
                response = self.table.scan(Limit=limit, ExclusiveStartKey=response.get("LastEvaluatedKey"))
            items = response.get("Items")
        except ClientError as error:
            print(error)
            return False
        return items

    def update_project(self, project_data):
        try:
            self.table.update_item(
                Key={"id": project_data.get("id")},
                UpdateExpression="set visible=:visible",
                ExpressionAttributeValues={
                    ":visible": project_data.get("visible"),
                })
        except ClientError as error:
            print(error)
            return False
        return True

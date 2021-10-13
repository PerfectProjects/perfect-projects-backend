def authorize(event, context):
    print("hello from authorize lambda")
    print(event)
    print(context)
    return {"statusCode": 200}


def authorize(event, context):
    print("hello from authorize lambda")
    print(event)
    print(context)
    return {"status": 200}

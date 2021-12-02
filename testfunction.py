def handler(event,context):

    kg=event['queryStringParameters']['kg']
    lb=float(kg)*2.20463
    ans = str(kg) + " Kgs is " + str(round(lb, 4)) + " lbs\n"

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': ans
    }

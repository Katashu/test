import datetime
import json


def lambda_handler(event, context):
    today = datetime.datetime.today()
    print('hello world')
    print('Today: {}'.format(today.strftime('%Y/%m/%d')))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

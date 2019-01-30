#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import boto3
import json
import uuid
from handlers.base import BaseHandler
logger = logging.getLogger('boilerplate.' + __name__)
client = boto3.client('dynamodb', region_name='us-east-1',
                      aws_access_key_id='AKIAJEXE6N3HOJHDI45Q',
                      aws_secret_access_key='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'
                      )


class DynamoDBFetchData(BaseHandler):

    def post(self):
        post_data = json.loads(self.request.body)
        user_id = post_data['user_id']
        response = client.get_item(TableName='TestDB',
                                   Key={'user_id': {'N': str(user_id)}},
                                   ConsistentRead=False)
        self.set_header('Content-Type', 'application/json')
        self.write(response)


class DynamoDBWriteData(BaseHandler):

    def post(self):
        post_data = json.loads(self.request.body)
        user_id = str(post_data['user_id'])
        user_name = post_data['user_name']
        user_password = post_data['user_password']
        user_state = post_data['state']
        self.set_header('Content-Type', 'application/json')
        response = client.put_item(TableName='TestDB',
                                   Item={'user_id': {'N': user_id},
                                   'user_password': {'S': user_password},
                                   'user_name': {'S': user_name},
                                   'user_state':{'S':user_state}
                                   })
        self.write(response)


class DynamoDBScan(BaseHandler):

    def get(self):
        response = client.scan(TableName='TestDB')
        self.set_header('Content-Type', 'application/json')
        self.write(response)

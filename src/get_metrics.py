"""
    Interacts with Amazon SQS
"""

import boto3
from src.logging import get_logger

logger = get_logger()

class SQSMetrics():
    """
        Search metrics and SQS queue attributes
    """

    def __init__(self, region='us-east-1'):
        self._sqs = boto3.client('sqs', region_name=region)

    def get_metrics(self, queue_url, metric_name):
        """
            Search metric by URL and name
        """

        response = self._sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=[metric_name]
        )['Attributes']

        logger.info(
            f"Queue {queue_url} - {metric_name}: {response[metric_name]}"
        )

        return response[metric_name]

    def get_queues(self):
        """
            List URL of SQS queues
        """

        queues = []

        for queue in self._sqs.list_queues()['QueueUrls']:
            queues.append(queue)

        return queues

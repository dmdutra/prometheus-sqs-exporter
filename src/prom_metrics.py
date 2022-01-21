"""
    PromMetics creates and inputs metrics into prometheus
"""

from dataclasses import dataclass
from prometheus_client import Gauge
from src.logging import get_logger

logger = get_logger()

@dataclass
class PromMetrics():
    """
        SQS metrics
    """

    approx_number_of_messages = Gauge(
        'approximate_number_of_messages',
        'Number of messages available',
        ['queue']
    )

    approx_number_of_messages_delayed = Gauge(
        'approximate_number_of_messages_delayed',
        'Number of messages delayed',
        ['queue']
    )

    approx_number_of_messages_not_visible = Gauge(
        'approximate_number_of_messages_not_visible',
        'Number of messages not visible',
        ['queue']
    )

    def prom_metrics(self, sqs):
        """
            Creating prometheus metrics
        """

        queue_urls = sqs.get_queues()

        for queue_url in queue_urls:

            self.approx_number_of_messages.labels(queue=queue_url).set(
                sqs.get_metrics(queue_url, 'ApproximateNumberOfMessages')
            )

            self.approx_number_of_messages_delayed.labels(queue=queue_url).set(
                sqs.get_metrics(queue_url, 'ApproximateNumberOfMessagesDelayed')
            )

            self.approx_number_of_messages_not_visible.labels(queue=queue_url).set(
                sqs.get_metrics(queue_url, 'ApproximateNumberOfMessagesNotVisible')
            )

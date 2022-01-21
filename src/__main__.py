"""
    Interacts with prometheus and SQS classes
"""

import argparse
import time
import sys


from prometheus_client import start_http_server
from src.get_metrics import SQSMetrics
from src.prom_metrics import PromMetrics


HELP_MESSAGE = '''

Prometheus SQS exporter
--------------------------------------------

-p, --port       Listen HTTP port
-i, --interval   Interval to update metrics

'''


def main():
    """
        Parse user arguments and interacts with prometheus and SQS classes
    """

    parser = argparse.ArgumentParser(add_help=False, usage=HELP_MESSAGE)

    parser.add_argument('-p', '--port', default=int(8420), required=False)
    parser.add_argument('-i', '--interval', default=int(60), required=False)


    args = parser.parse_args()

    prom = PromMetrics()
    sqs = SQSMetrics()

    try:
        start_http_server(int(args.port))
    except OSError as error:
        print(f"error: {error}")
        sys.exit(1)

    while True:
        prom.prom_metrics(sqs)
        time.sleep(int(args.interval))


if __name__=='__main__':
    main()

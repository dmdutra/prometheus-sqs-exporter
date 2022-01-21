from setuptools import setup, find_packages

setup(
    name='prometheus-sqs-exporter',
    version='1.0.0',
    description='Prometheus exporter for AWS Simple Queue Service (SQS)',
    url='https://github.com/0xdutra/prometheus-sqs-exporter',
    author='Gabriel Dutra',
    entry_points={"console_scripts": ["prometheus-sqs-exporter=src.__main__:main"]},
    install_requires=[
        'boto3',
        'prometheus_client'
    ],
    zip_safe=False,
    packages=find_packages()
)

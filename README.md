# AWS Serverless File Processing Pipeline

## Overview

This project demonstrates a serverless, event-driven architecture built on AWS. When a file is uploaded to Amazon S3, an AWS Lambda function automatically processes the event, records activity in CloudWatch Logs, and sends an email notification through Amazon SNS.

The solution was designed to showcase AWS architecture principles, automation, monitoring, security, and cloud-native application design.

## Architecture

S3 Bucket
↓
Lambda Function (Python)
↓
CloudWatch Logs
↓
SNS Email Notification

## AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon SNS
* Amazon CloudWatch
* AWS IAM

## Features

* Automatic file processing
* Event-driven architecture
* Serverless computing
* Monitoring and logging
* Email notifications
* Least-privilege IAM permissions
* Cost-efficient design

## Security

Implemented the Principle of Least Privilege by restricting Lambda permissions to publish only to the required SNS topic rather than granting broad access to all resources.

## Technical Skills Demonstrated

* Cloud Architecture
* AWS Services
* Python Development
* IAM Security
* Event-Driven Design
* Monitoring & Logging
* Troubleshooting
* Serverless Computing

## Future Enhancements

* File metadata storage using DynamoDB
* API Gateway integration
* AWS Bedrock AI integration
* Multi-file processing workflows
* Infrastructure as Code using Terraform

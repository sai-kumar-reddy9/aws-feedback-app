# AWS Serverless Feedback Submission App

## Overview
A serverless application demonstrating deployment on AWS:
- Frontend: Static site hosted on Amazon S3
- Backend: AWS Lambda (Python) behind API Gateway
- Storage: DynamoDB table for feedback items
- IAM roles for secure access
- Optional: CloudFront for CDN

## Repo structure
```
aws-feedback-app/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── backend/
│   └── lambda_function.py
├── dynamodb-table-schema.json
└── README.md
```

## Quick deployment steps (detailed steps are provided in the project instructions document)

1. Create DynamoDB table using the provided schema.
2. Create an IAM role for Lambda with DynamoDB access.
3. Create Lambda function (Python 3.10), set env var FEEDBACK_TABLE to FeedbackTable.
4. Create API Gateway HTTP API or REST API with a POST route that integrates with Lambda and enable CORS.
5. Deploy frontend to S3 and enable static website hosting. Update script.js with API invoke URL.
6. (Optional) Configure CloudFront distribution for the S3 website or API.


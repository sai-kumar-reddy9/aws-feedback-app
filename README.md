AWS Serverless Feedback Submission App

A fully functional serverless web application built using AWS services.
This project demonstrates modern cloud application development using Lambda, API Gateway, DynamoDB, S3, and IAM.
Users can submit feedback through a frontend hosted on S3, and their responses are stored securely in DynamoDB through a serverless backend.

 Features

Static Website Hosting (Amazon S3)
Frontend deployed on S3 with public website access.

Serverless Backend (AWS Lambda – Python)
Processes incoming feedback and writes to DynamoDB.

API Routing (Amazon API Gateway)
Secure POST endpoint with CORS enabled for frontend integration.

NoSQL Database (Amazon DynamoDB)
Stores feedback entries with unique IDs, timestamps, and user details.

IAM Role-Based Security
Lambda is restricted using least-privilege permissions for DynamoDB and CloudWatch.

(Optional) CloudFront CDN
Can be added for HTTPS, caching, and global performance.

📁 Repository Structure
aws-feedback-app/
├── frontend/
│   ├── index.html          # User interface for submitting feedback
│   ├── script.js           # API call to API Gateway endpoint
│   └── style.css           # Basic styling for UI
│
├── backend/
│   └── lambda_function.py  # Lambda handler to store data in DynamoDB
│
├── dynamodb-table-schema.json  # Table schema for FeedbackTable
│
└── README.md               # Project documentation

Architecture Overview
User → S3 Website → API Gateway (POST /feedback)
       ↓                         ↓
    Browser JS  →→→→→→→→   Lambda Function
                                 ↓
                           DynamoDB Table


User submits feedback on the hosted website

JavaScript sends data to API Gateway

API Gateway triggers AWS Lambda

Lambda writes to DynamoDB

Response returned to UI

 Deployment Steps

Create DynamoDB Table
Table name: FeedbackTable
Primary key: id (String)
Billing mode: On-Demand.

Create IAM Role for Lambda
Attach:

AmazonDynamoDBFullAccess

AWSLambdaBasicExecutionRole

Create Lambda Function (Python 3.10)

Upload lambda_function.py code

Add environment variable:
FEEDBACK_TABLE=FeedbackTable

Create API Gateway Endpoint

HTTP API

Route: POST /feedback

Integrate with Lambda

Enable CORS

Copy Invoke URL and update in script.js

Host Frontend on S3

Create bucket

Upload index.html, style.css, script.js

Enable static website hosting

Add public bucket policy

(Optional) Add CloudFront Distribution

Origin → S3 website URL

Get global HTTPS URL

🔗 Live Demo URL

http://saikumarreddys-feedback-app.s3-website.eu-north-1.amazonaws.com/

📌 Technology Stack

Frontend: HTML, CSS, JavaScript

Backend: AWS Lambda (Python)

API Layer: Amazon API Gateway

Database: DynamoDB

Hosting: Amazon S3

Security: IAM

Monitoring: CloudWatch (Logs for Lambda)

📝 Author

Sai Kumar Reddy
AWS | Java | MERN | Cloud Enthusiast
GitHub: https://github.com/sai-kumar-reddy9
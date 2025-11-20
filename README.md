#  AWS Serverless Feedback Submission App

A fully functional **serverless web application** built using AWS services.  
This project demonstrates modern cloud development using **Lambda, API Gateway, DynamoDB, S3, and IAM**.  
Users submit feedback on a static website hosted on S3, and the backend securely stores it in DynamoDB using AWS Lambda.

---

##  Features

### **🔹 Static Website Hosting (Amazon S3)**
Frontend deployed on S3 with public website access.

### **🔹 Serverless Backend (AWS Lambda – Python)**
Processes incoming feedback and writes entries to DynamoDB.

### **🔹 API Routing (Amazon API Gateway)**
Secure POST endpoint (`/feedback`) with CORS enabled for frontend integration.

### **🔹 NoSQL Database (Amazon DynamoDB)**
Stores feedback entries with:
- Unique ID  
- Name  
- Feedback message  
- Timestamp  

### **🔹 IAM Role-Based Security**
Lambda uses least-privilege access to DynamoDB and CloudWatch.

### **🔹 CloudFront CDN**
For HTTPS, caching, and global performance optimization.

---

##  Repository Structure

    aws-feedback-app/
    ├── frontend/
    │ ├── index.html # User interface for submitting feedback
    │ ├── script.js # JS API call to API Gateway endpoint
    │ └── style.css # Styling for UI
    │
    ├── backend/
    │ └── lambda_function.py # Lambda handler that stores data in DynamoDB
    │
    ├── dynamodb-table-schema.json # Schema for FeedbackTable
    │
    └── README.md # Project documentation


---

##  Architecture Overview
        User (Browser)
              ↓
    S3 Static Website Hosting
              ↓
  JavaScript fetch() → API Gateway (POST /feedback)
              ↓
        AWS Lambda Function
              ↓
        DynamoDB (FeedbackTable)
---

## Deployment Steps (Summary)

### **1. Create DynamoDB Table**
- Table name: `FeedbackTable`  
- Primary key: `id` (String)  
- Billing mode: On-Demand

### **2. Create IAM Role for Lambda**
Attach:
- `AmazonDynamoDBFullAccess`
- `AWSLambdaBasicExecutionRole`

### **3. Create Lambda Function**
- Runtime: Python 3.10  
- Add environment variable:  
  `FEEDBACK_TABLE = FeedbackTable`  
- Deploy code from `backend/lambda_function.py`

### **4. Create API Gateway Endpoint**
- HTTP API  
- Route: `POST /feedback`  
- Integrate with Lambda  
- Enable CORS  
- Copy the Invoke URL and update `script.js`

### **5. Host Frontend on S3**
- Upload `index.html`, `style.css`, `script.js`  
- Enable public access  
- Enable static website hosting  

### **6. (Optional) Add CloudFront**
- Origin: S3 website endpoint  
- Get secure HTTPS domain  

---

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Serverless Compute:** AWS Lambda (Python)  
- **API Layer:** Amazon API Gateway  
- **Database:** DynamoDB  
- **Hosting:** Amazon S3  
- **Security:** AWS IAM  
- **Monitoring:** AWS CloudWatch Logs  

---

##  Author

**Sai Kumar Reddy**  
Cloud & Full-Stack Developer  
GitHub: [sai-kumar-reddy9](https://github.com/sai-kumar-reddy9)


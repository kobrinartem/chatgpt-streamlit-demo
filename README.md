# ChatGPT Operationalisation in AWS: A Chatbot Prototyped with Streamlit and Deployed to AWS ECS Fargate

This project includes a Streamlit-based chatbot operationalized in AWS using AWS ECS Fargate.

## Table of Contents

- [ChatGPT Operationalisation in AWS: A Chatbot Prototyped with Streamlit and Deployed to AWS ECS Fargate](#chatgpt-operationalisation-in-aws-a-chatbot-prototyped-with-streamlit-and-deployed-to-aws-ecs-fargate)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [CloudFormation Stack Deployment](#cloudformation-stack-deployment)
    - [Docker Image Build](#docker-image-build)
  - [Usage](#usage)
  - [Support](#support)
  - [Contributing](#contributing)

## Installation

### CloudFormation Stack Deployment

To deploy the CloudFormation stack for this project, use the `./cf.yaml` file. You can do this using the AWS Management Console, the AWS CLI, or the AWS SDKs.

For example, to deploy the stack using the AWS CLI, you can use the following command:

```aws cloudformation create-stack --stack-name chatgpt-streamlit --template-body file://cf.yaml --capabilities CAPABILITY_IAM```

This will create a new stack called `chatgpt-streamlit` using the `cf.yaml` template file and the `CAPABILITY_IAM` capability.

### Docker Image Build

To build the Docker image for this project, use the `Dockerfile` in the `./app` directory. You can do this using the `docker build` command.

For example, to build the image using the `Dockerfile` in the current directory, you can use the following command:

```docker build -t chatgpt-streamlit .```


This will build the image and tag it with the name `chatgpt-streamlit`.

## Usage

The Streamlit application is deployed in an AWS ECS cluster and is available through a web browser using the URL of the load balancer. To access the app, simply navigate to the URL in a web browser.

## Support

If you have any questions or encounter any issues while using the project, please don't hesitate to reach out. You can find contact information in the [CONTRIBUTING](#contributing) section below.

## Contributing

We welcome contributions to this project! If you would like to contribute, please follow these guidelines:

- Create an issue to discuss the change you would like to make.
- Once the change has been discussed and approved, you can submit a pull request.
- All pull requests should include tests to ensure that the code is working as intended.
- Once the pull request has been reviewed and accepted, it will be merged into the main branch.

Thank you for your interest in contributing to the project!

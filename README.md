# Private API access via API Gateway with VPC Endpoint & Transit Gateway

![Private API Access with API Gateway   VPC Endpoint](https://github.com/user-attachments/assets/384789bd-1711-4be9-b807-538caf903815)

This architecture enables secure private API access through an API Gateway, leveraging VPC Endpoints and AWS Transit Gateway to connect multiple consumer accounts seamlessly.

Each consumer VPC connects to a shared services VPC via the Transit Gateway, routing traffic to the service provider's VPC where the private API is hosted behind a Network Load Balancer.

With an API Gateway and resource policy, only authorized VPCs access sensitive resources, ensuring scalability, security, and private connectivity without internet exposure.


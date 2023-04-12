# cfn-finance

This is a Cloudformation template for the infrastructure required to run Finance web application.
For the application's code refer to [Finance repostiory](https://github.com/Hevsy/finance)

The template deploys the following AWS resources:

## AWS Services Used

* Amazon Elastic Compute Cloud (EC2)
* Amazon Relational Database Service (RDS) - PostgresSQL
* Amazon Virtual Private Cloud (VPC) with Subnets, Security Groups, IGW, routing tables
* Amazon Application Load Balancer
* Amazon Auto Scaling Group

![Diagram](https://lucid.app/publicSegments/view/690ffa1c-37ba-436e-b176-3311bd715e40/image.png)

Done:

* All networking (VPC, Subnets, IGW, Route tables, Security Groups)

* DB Subnet Group

* PostgreSQL RDS

TODO:

* Key-pair

* Autoscaling group

* ALB

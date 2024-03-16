#terraform fmt
#terraform validate

#terraform init

#terraform apply
The code does the following:

1]Creates a VPC with the CIDR block.
2]Creates subnets for each layer.
3]Creates an IGW and NAT gateway.
4]Creates Route tables.
5]Creates a RDS instance.
6]Configures security group for Web layer.
7]EC2 instances for webservers.
8]Application load balancer.
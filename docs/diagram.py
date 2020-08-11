from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, ApplicationAutoScaling, EC2, Fargate, Lambda
from diagrams.aws.devtools import Codecommit, Codepipeline
from diagrams.aws.management import Cloudformation, Cloudwatch, SystemsManager
from diagrams.aws.network import ElasticLoadBalancing, InternetGateway, NATGateway, PrivateSubnet, PublicSubnet, Route53, VPC
from diagrams.aws.storage import EFS, S3

with Diagram("UniFi Controller", show=False):
    dns = Route53("dns")
    lb = ElasticLoadBalancing("lb")

    with Cluster("TargetGroup"):
        svc_group = [Fargate("Controller1"),
                     Fargate("Controller2")]

    EFS = EFS("EFS")

    dns >> lb >> svc_group
    svc_group >> EFS

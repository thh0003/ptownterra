import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_terra.aws_terra_stack import AwsTerraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_terra/aws_terra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsTerraStack(app, "aws-terra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

from aws_cdk import aws_apigateway, aws_lambda, core

from cdk.hitcounter import HitCounter


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_lambda = aws_lambda.Function(
            self,
            "HelloHandler",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.asset("lambda"),
            handler="hello.handler",
        )

        hello_with_counter = HitCounter(
            self,
            "HelloHitCounter",
            downstream=hello_lambda,
        )

        aws_apigateway.LambdaRestApi(
            self,
            "Endpoint",
            handler=hello_with_counter.handler,
        )

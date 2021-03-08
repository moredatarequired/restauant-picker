from aws_cdk import aws_apigateway, aws_lambda, core

from cdk.hitcounter import HitCounter


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        restaurant_poll = aws_lambda.Function(
            self,
            "RestaurantPollHandler",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.asset("lambda"),
            handler="restaurant_poll.handler",
        )

        poll_with_counter = HitCounter(
            self,
            "RestaurantPollHitCounter",
            downstream=restaurant_poll,
        )

        aws_apigateway.LambdaRestApi(
            self,
            "Endpoint",
            handler=poll_with_counter.handler,
        )

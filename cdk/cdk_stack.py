from aws_cdk import aws_iam as iam
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from aws_cdk import aws_sqs as sqs
from aws_cdk import core


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self,
            "CdkQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(self, "CdkTopic")

        topic.add_subscription(subs.SqsSubscription(queue))

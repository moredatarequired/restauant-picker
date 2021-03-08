from aws_cdk import aws_dynamodb, aws_lambda, core


class RestaurantStore(core.Construct):
    @property
    def table(self):
        return self._table

    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self._table = aws_dynamodb.Table(
            self,
            "Restaurants",
            partition_key={"name": "uuid", "type": aws_dynamodb.AttributeType.STRING},
            sort_key={"name": "name", "type": aws_dynamodb.AttributeType.STRING},
        )

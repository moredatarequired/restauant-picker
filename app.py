#!/usr/bin/env python3

import os

from aws_cdk import core

from cdk.deploy_pipeline_stack import DeployPipelineStack
from cdk.restaurant_picker_stack import RestaurantPickerStack

AWS_ENV = core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)

app = core.App()

RestaurantPickerStack(app, "restaurant-picker", env=AWS_ENV)
DeployPipelineStack(app, "deploy-pipeline", env=AWS_ENV)

app.synth()

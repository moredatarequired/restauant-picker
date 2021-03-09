#!/usr/bin/env python3

from aws_cdk import core

from cdk.deploy_pipeline_stack import DeployPipelineStack
from cdk.restaurant_picker_stack import RestaurantPickerStack

AWS_REGION = "us-west-2"
AWS_ACCOUNT_ID = "724169626350"
AWS_ENV = core.Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION)

app = core.App()

RestaurantPickerStack(app, "restaurant-picker", env=AWS_ENV)
DeployPipelineStack(app, "deploy-pipeline", env=AWS_ENV)

app.synth()

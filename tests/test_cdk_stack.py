import json

import pytest
from aws_cdk import core

from cdk.deploy_pipeline_stack import DeployPipelineStack
from cdk.restaurant_picker_stack import RestaurantPickerStack
from cdk.util import camel_to_kebab


def get_template(stack):
    app = core.App()
    stack_name = camel_to_kebab(stack.__name__)
    stack(app, stack_name)
    return json.dumps(app.synth().get_stack(stack_name).template)


def test_restaurant_picker_stack():
    template = get_template(RestaurantPickerStack)


def test_deploy_pipeline_stack():
    template = get_template(DeployPipelineStack)

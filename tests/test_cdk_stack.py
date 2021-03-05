import json

import pytest
from aws_cdk import core

from cdk.cdk_stack import CdkStack


def get_template():
    app = core.App()
    CdkStack(app, "cdk")
    return json.dumps(app.synth().get_stack("cdk").template)

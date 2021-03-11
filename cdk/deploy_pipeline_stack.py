import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_codepipeline_actions as codepipeline_actions
from aws_cdk.core import Construct, SecretValue, Stack, StackProps
from aws_cdk.pipelines import CdkPipeline, SimpleSynthAction


class DeployPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = CdkPipeline(
            self,
            "Pipeline",
            pipeline_name="StackDeployPipeline",
            cloud_assembly_artifact=cloud_assembly_artifact,
            source_action=codepipeline_actions.GitHubSourceAction(
                action_name="GitHub",
                output=source_artifact,
                oauth_token=SecretValue.secrets_manager("GitHubAWSCodePipelineToken"),
                trigger=codepipeline_actions.GitHubTrigger.POLL,
                owner="moredatarequired",
                repo="restauant-picker",
                branch="main",
            ),
            synth_action=SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_commands=["pip install poetry", "poetry install"],
                synth_command="poetry run npx cdk synth",
            ),
        )

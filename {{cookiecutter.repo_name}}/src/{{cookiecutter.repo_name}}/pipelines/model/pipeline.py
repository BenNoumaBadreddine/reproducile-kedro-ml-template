from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from {{cookiecutter.repo_name}}.extras.delete_me import print_message

    
def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=print_message,
            inputs="Hello, model pipeline!",  # No inputs required
            outputs=None,  # No outputs generated
            name="print_model_node"
        )
    ])

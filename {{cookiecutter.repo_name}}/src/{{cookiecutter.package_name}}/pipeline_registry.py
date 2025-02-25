from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from email_ai.pipelines import raw, feature, intermediate, model, model_input, primary


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["raw"] = raw.create_pipeline()
    # pipelines["feature"] = feature.create_pipeline()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines

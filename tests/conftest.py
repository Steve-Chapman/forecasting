# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
import pytest
from fclib.common.utils import git_repo_path


@pytest.fixture(scope="module")
def notebooks():
    """Get paths of example notebooks.

    Returns:
        dict: Dictionary including paths of the example notebooks.
    """
    repo_path = git_repo_path()
    examples_path = os.path.join(repo_path, "examples")
    usecase_path = os.path.join(examples_path, "grocery_sales", "python")
    quick_start_path = os.path.join(usecase_path, "00_quick_start")
    model_path = os.path.join(usecase_path, "02_model")

    # Paths of the notebooks
    paths = {
        "lightgbm_quick_start": os.path.join(quick_start_path, "lightgbm_single_round.ipynb"),
        "lightgbm_multi_round": os.path.join(model_path, "lightgbm_multi_round.ipynb"),
        "dilatedcnn_multi_round": os.path.join(model_path, "dilatedcnn_multi_round.ipynb"),
        "autoarima_quick_start": os.path.join(quick_start_path, "autoarima_single_round.ipynb"),
        "autoarima_multi_round": os.path.join(model_path, "autoarima_multi_round.ipynb"),
    }
    return paths

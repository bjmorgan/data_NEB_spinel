# Notebook Tests

[![CircleCI](https://circleci.com/gh/bjmorgan/data_NEB_spinel.svg?style=svg&circle-token=858a87f5298c9e6fc09a308ffa0d66652907dc82)](https://circleci.com/gh/bjmorgan/data_NEB_spinel)

This directory contains a script for testing that the notebook scripts run without errors.

To run this script manually:
```
python test_analysis_notebooks.py
```

or

```
python -m unittest discover
```

The notebook requires the modules listed in the `requirements.txt` file, in the top level directory of the repository.

Tests are automatically run on every commit [here](TODO).

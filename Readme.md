Hi!
This repository is an exploration of fastapi library.

1. let's go to create an environment with conda

```conda create -n API python=3.7```

2. activate the environment

```conda activate API```

3. Install fastapi

`pip install fastapi` or `pip install fastapi==0.62.0`

4. Install uvicorn, an application server

`pip install uvicor` or `pip install uvicorn==0.13.1`

5. you can find a file called `example.py` to test this script, please type the following code into your terminal

```uvicorn example:app --reload```

the `--reload` is only for development, to refresh the changes made

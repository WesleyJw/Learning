## MLOps 101 Course

---

### How to admin python projects with Poetry?

One of the most arduous tasks in project management is controlling all dependencies/requirements needed for the project to run. Poetry is a tool for dependency management and packaging in Python. With Poetry, you can specify the libraries your project relies on, and it manages their installation and updates. It provides a lockfile for consistent installations and can also build your project for distribution.

- How to create a project with poetry?

```
# project-demo is my project name
poetry new project-demo

# created architecture
project-demo
├── pyproject.toml
├── README.md
├── project_demo
│   └── __init__.py
└── tests
    └── __init__.py
```

- Initialising a pre-existing project:

Suppose you have a directory and need to create a project from there. The `init` command can create a `pyproject.toml` file in a preexisting directory.

```
poetry init
```

When you run init command some configurations options can be specified:

```
Package name [02-mlops-intro-poetry]: data_analysis
Version [0.1.0]:  0.1.0
Description []:  This is a project to analyze sales price.
Author [wesleyjw <jwesleybiologo@gmail.com>, n to skip]:  wesleyjw
License []:  
Compatible Python versions [^3.8]:  ^3.8
Would you like to define your main dependencies interactively? (yes/no) [yes]
Package to add or search for (leave blank to skip):
Would you like to define your development dependencies interactively? (yes/no) [yes] 
Package to add or search for (leave blank to skip): 
Do you confirm generation? (yes/no) [yes] 
```
A `pyproject.toml` file was created with metadata about the project like name, version, description, authors, and dependencies.

- How to add a dependency?

You can specify any dependency by hand modifying the `toml` file in the section `tool.poetry.dependencies` or using the `poetry add` command:

```
# by hand
[tool.poetry.dependencies]
pandas = "^2.0.0"

# by add command
poetry add pandas
```

After add the dependency a file with name `poetry.lock` is created. The lock file contain the versions of your project and dependencies (including sub-dependencies) to ensure consistency and reproducibility of your environment.

- Install a dependency to a dev env:

With poetry, you can isolate the developer's packages and install them in a dev environment. You can create as many groups as necessary and isolate project dependencies. 

```
poetry add ipykernel --group dev
```

- The virtual environment:

A virtual environment is created every time you create a project with (`poetry new project`) or initialize (`poetry init`). You can activate your virtual environment using the `poetry shell` command. Type the `exit` or `deactivate` commands to exit the virtual environment. You also can execute a script with:

```
sudo poetry run python examples/script_with_dep.py
```

A better way to run scripts in your project is using `makefiles` or `justfiles`.

- Executing scripts with make:

A makefile example:

```
shell:
	poetry shell
execute:
	poetry run python examples/simple_script.py
execute-dep:
	poetry run python examples/script_with_dep.py
```

- Executing scripts with make:

```
make
```
Ctrl+D to exit the poetry shell.
```
make execute
```

- Executing scripts with just:

```
just execute-dep
```

Using environment variables. 

```
set dotenv-load
shell:
    poetry shell
execute:
    poetry run python examples/simple_script.py
execute-dep:
    poetry run python examples/script_with_dep.py $NOME
```

---

### Fast API




## MLOps 101 Course

## How to admin python projects with Poetry?

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

- How to add a dependency?

You can specify any dependency by hand modifying the `toml` file in the section `tool.poetry.dependencies` or using the `poetry add` command:

```
# by hand
[tool.poetry.dependencies]
pandas = "^2.0.0"

# by add command
poetry add pandas
```

- Install a dependency to a dev env:

With poetry, you can isolate the developer's packages and install them in a dev environment. You can create as many groups as necessary and isolate project dependencies. 

```
poetry add ipykernel --group dev
```

- The virtual environment:

A virtual environment is created every time you create a project (`poetry new project`) or initialize (`poetry init`). You can activate your virtual environment using the `poetry shell` command. Type the `exit` or `deactivate` commands to exit the virtual environment. You also can execute a script with:

```
sudo poetry run python exemplos/script_com_dep.py
```

A better way to run scripts in your project is using `makefiles` or `justfiles`.

- Executing scripts with make:

```
make
```

```
make execute-dep
```

- Executing scripts with make:
```
just execute-dep
```

Using environment variables. 

```
set dotenv-load
shell:
    poetry shell
execute:
    poetry run python exemplos/script_simples.py 
execute-dep:
    poetry run python exemplos/script_com_dep.py $NOME
```
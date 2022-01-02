# Arcade Cookiecutter

This is a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for generating a skeleton [Arcade](https://github.com/pythonarcade/arcade) project.

This comes with the base files for a Python package such as `setup.py` and `setup.cfg`, and the [Arcade Starting Template](https://api.arcade.academy/en/latest/examples/starting_template.html)

## How to use it

If you don't already have cookiecutter installed, install it by running:

```bash
pip install cookiecutter
```

Once you have cookiecutter, just make sure you're in the directory where you want to create the project and run:

```bash
cookiecutter https://github.com/Cleptomania/arcade-cookiecutter
```

The template will ask for a project name, and then convert that to snake case to use as a project slug(you can override this), and a description.

## Running the Game

Once your project has been generated, you can install it using:

```bash
pip install -e .
```

Then you can run the game with the following command, where project_slug is the option you chose during generation:

```bash
python -m project_slug
```

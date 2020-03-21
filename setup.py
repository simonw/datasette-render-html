from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-render-html",
    description="Datasette plugin that renders specified cells as HTML",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-render-html",
    license="Apache License, Version 2.0",
    version=VERSION,
    py_modules=["datasette_render_html"],
    entry_points={"datasette": ["render_html = datasette_render_html"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest"]},
)

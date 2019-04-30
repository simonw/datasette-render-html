# datasette-render-html

[![PyPI](https://img.shields.io/pypi/v/datasette-render-html.svg)](https://pypi.org/project/datasette-render-html/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-render-html.svg?style=svg)](https://circleci.com/gh/simonw/datasette-render-html)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-render-html/blob/master/LICENSE)

This Datasette plugin lets you configure Datasette to render specific columns as HTML in the table and row interfaces.

This means you can store HTML in those columns and have it rendered as such on those pages.

If you have a database called `docs.db` containing a `glossary` table and you want the `definition` column in that table to be rendered as HTML, you would use a `metadata.json` file that looks like this:

    {
        "databases": {
            "docs": {
                "tables": {
                    "glossary": {
                        "plugins": {
                            "datasette-render-html": {
                                "columns": ["definition"]
                            }
                        }
                    }
                }
            }
        }
    }

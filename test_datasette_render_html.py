from datasette_render_html import render_cell
from datasette.app import Datasette
from markupsafe import Markup
import pytest


@pytest.fixture
def configured_datasette():
    return Datasette(
        [],
        metadata={
            "databases": {
                "docs": {
                    "tables": {
                        "glossary": {
                            "plugins": {
                                "datasette-render-html": {"columns": ["definition"]}
                            }
                        }
                    }
                }
            }
        },
    )


def test_leaves_regular_columns_alone(configured_datasette):
    assert None == render_cell(
        "a<b", "not_definition", "glossary", "docs", configured_datasette
    )


def test_marks_configured_column_safe(configured_datasette):
    assert Markup("a<b") == render_cell(
        "a<b", "definition", "glossary", "docs", configured_datasette
    )


def test_none_becomes_blank_string(configured_datasette):
    assert Markup("") == render_cell(
        None, "definition", "glossary", "docs", configured_datasette
    )

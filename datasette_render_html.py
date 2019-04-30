from datasette import hookimpl
import jinja2


@hookimpl
def render_cell(value, column, table, database, datasette):
    config = datasette.plugin_config(
        "datasette-render-html", database=database, table=table
    )
    if not config:
        return None
    if column in config["columns"]:
        return jinja2.Markup(value)

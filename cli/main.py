"""CESAR CLI: one entry point for all commands."""

import typer

from cli.batch import batch_app
from cli.predict_one import predict_one_app
from cli.acceptance_tests import acceptance_tests_app
from cli.property_tests import property_tests_app

app = typer.Typer(
    name="cesar",
    help="CESAR: batch and single-record property value prediction.",
)
app.add_typer(batch_app, name="batch")
app.add_typer(predict_one_app, name="predict-one")
app.add_typer(acceptance_tests_app, name="acceptance-tests")
app.add_typer(property_tests_app, name="property-tests")


def main() -> None:
    app()


if __name__ == "__main__":
    main()

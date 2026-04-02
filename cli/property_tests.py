"""CLI command: run property-based tests against the API."""

import typer
import pytest

property_tests_app = typer.Typer(
    name="property-tests",
    help="Run property-based tests against the CESAR API.",
)


@property_tests_app.command("run")
def run_property_tests(
    base_url: str = typer.Option(
        None,
        "--base-url",
        "-u",
        help="API base URL (default: http://localhost:8000)",
    ),
) -> None:
    """Run property-based tests using Hypothesis."""
    import os
    if base_url:
        os.environ["CESAR_API_URL"] = base_url

    typer.echo("Running property-based tests...")
    result = pytest.main([
        "model_acceptance_tests/test_properties.py",
        "-v",
    ])
    if result != 0:
        raise typer.Exit(1)
    typer.echo("All property-based tests passed.")

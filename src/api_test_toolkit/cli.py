import typer
from pathlib import Path

from api_test_toolkit.loader import load_suite
from api_test_toolkit.runner import run_suite
from api_test_toolkit.report import print_report

app = typer.Typer()

@app.callback()
def main():
    """API Test Toolkit - rode tests API for YAML files."""
    pass


@app.command()
def run(path: Path):
    suite = load_suite(path)
    result = run_suite(suite)
    print_report(result)

    if any(not r.passed for r in result): raise typer.Exit(code=1)

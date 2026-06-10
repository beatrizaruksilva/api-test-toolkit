from rich.console import Console

from api_test_toolkit.models import TestResult

console = Console()


def print_report(results: list[TestResult]) -> None:
    total_passed = 0
    for result in results:
        if result.passed:
            total_passed += 1
            console.print(f"[green]PASS[/green] {result.name}")
        else:
            console.print(f"[red]FAIL[/red] {result.name}")
            for error in result.errors:
                console.print(f"   - {error}", style="dim")

    total = len(results)
    console.print("-" * 55)
    console.print(
        f"Total: {total}  |  "
        f"[green]Passed: {total_passed}[/green]  |  "
        f"[red]Failed: {total - total_passed}[/red]"
    )
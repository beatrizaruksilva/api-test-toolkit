from api_test_toolkit.models import TestResult

def print_report(results: list[TestResult]) -> None:
    total_passed = 0
    for result in results:
        if result.passed:
            icone = "✅"
            total_passed += 1
        else:
            icone = "❌"
        linha = f"Teste {result.name} {icone}\n"

        if not result.passed:
            linha += f"  (esperado {r.expected_status}, veio {r.actual_status})"
        
        print(linha)

    print("-------------------------------------------------------\n")
    print(f"Total tested: {len(results)},\nTotal Passed: {total_passed},\nTotal Failed: {len(results)-total_passed}\n")
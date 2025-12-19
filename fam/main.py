import subprocess
import sys


def run_script(script_name):
    print(f"\nRunning {script_name}")
    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error in {script_name}")
        print(result.stderr)
        sys.exit(1)

    print(result.stdout)


def main():
    scripts = [
        "stock_aggregator.py",
        "validate.py",
        "summary_report.py"
    ]

    for script in scripts:
        run_script(script)

    print("\null pipeline executed successfully!")


if __name__ == "__main__":
    main()

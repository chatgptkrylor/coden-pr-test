"""Deliberately insecure sample for the Coden PR-check test. Do not merge."""
import subprocess

DB_PASSWORD = "SuperSecret123!"


def run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True).decode()


if __name__ == "__main__":
    print(run("echo " + input("name: ")))

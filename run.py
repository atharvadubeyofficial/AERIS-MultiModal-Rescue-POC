"""
AERIS
Autonomous Emergency Response & Intelligence System

Main launcher for the AERIS Mission Control application.
"""

import subprocess
import sys


def main():
    print("=" * 60)
    print(" AERIS - AUTONOMOUS EMERGENCY RESPONSE SYSTEM")
    print("=" * 60)
    print()
    print("Starting AERIS Mission Control...")
    print()

    command = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py",
    ]

    subprocess.run(command)


if __name__ == "__main__":
    main()

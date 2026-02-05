import sys
import site
import os


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def venv_connected_mess():
    python_path = sys.executable
    env_name = os.path.basename(sys.prefix)
    venv_path = (sys.prefix)
    packaging_location = site.getsitepackages()[0]
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {venv_path}")
    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting \nthe global system.")
    print()

    print("Package installation path: ")
    print(packaging_location)


def venv_desconnected_mess() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()

    print(f"Current Python: {sys.prefix}")
    print("Virtual Environment: None detected")
    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install")
    print()

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate\t# On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate\t# On Windows")
    print()

    print("Then run this program again.")


def main() -> None:
    if in_venv():
        venv_connected_mess()
    else:
        venv_desconnected_mess()


main() if __name__ == "__main__" else ""

"""Version maintainer for the project."""
import sys
import json
from argparse import ArgumentParser


class OncoplotVersioneer:
    """Version maintainer for the project."""

    VERSION: str

    def __init__(self) -> None:
        with open("project_meta.json") as f:
            meta_data = json.load(f)
        self.VERSION = meta_data["version"]

    def major_version(self) -> str:
        """calculates next major version of the project."""
        gen, major, minor = self.VERSION.split(".")
        major = int(major) + 1
        return gen + "." + str(major) + "." + minor

    def minor_version(self) -> str:
        """calculates next minor version of the project."""
        gen, major, minor = self.VERSION.split(".")
        minor = int(minor) + 1
        return gen + "." + major + "." + str(minor)

    def next_generation(self) -> str:
        """calculates next generation of the project."""
        gen, major, minor = self.VERSION.split(".")
        gen = int(gen) + 1
        return str(gen) + ".0.0"

    def n_major(self, n: int) -> str:
        """next major version after n commits of the project."""
        gen, major, minor = self.VERSION.split(".")
        major = int(major) + n
        return gen + "." + str(major) + "." + minor

    def n_minor(self, n: int) -> str:
        """next minor version after n commits of the project."""
        gen, major, minor = self.VERSION.split(".")
        minor = int(minor) + n
        return gen + "." + major + "." + str(minor)

    def write_version(self, version: str) -> None:
        """writes the version to the project_meta.json file."""
        with open("project_meta.json", "w") as f:
            json.dump({"version": version}, f)


def main(argv):
    parser = ArgumentParser(description="Version maintainer for the project.")
    parser.add_argument("-m", "--message", help="Commit message")
    versioneer = OncoplotVersioneer()
    version = ""
    if "[nextgen]" in argv:
        version = versioneer.next_generation()
    elif "[major]" in argv:
        version = versioneer.major_version()
    else:
        version = versioneer().minor_version()
    versioneer().write_version(version)


if __name__ == "__main__":
    main(sys.argv[1:])

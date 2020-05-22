import argparse
import os
from typing import Optional, Sequence

from poetry.factory import Factory
from poetry.utils.exporter import Exporter


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dev", action="store_true", help="Include development dependencies.",
    )
    parser.add_argument(
        "-e",
        "--extras",
        action="append",
        help="Extra sets of dependencies to include.",
    )
    parser.add_argument(
        "--without-hashes",
        action="store_true",
        help="Exclude hashes from the exported file.",
    )
    parser.add_argument(
        "--with-credentials",
        action="store_true",
        help="Include credentials for extra indices.",
    )
    parser.add_argument("filename", help="Filename to check.")
    args = parser.parse_args(argv)

    poetry = Factory().create_poetry(os.getcwd())
    exporter = Exporter(poetry)
    with open(args.filename, "w") as req:
        exporter.export(
            fmt="requirements.txt",
            cwd=None,
            output=req,
            with_hashes=not args.without_hashes,
            dev=args.dev,
            extras=args.extras,
            with_credentials=args.with_credentials,
        )


if __name__ == "__main__":
    exit(main())

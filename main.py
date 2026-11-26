"""Write one pickup line to /output/entry.txt.

The line is an entry for a one-line pickup-line contest, written
as if a robot were flirting.
"""

import os


def pickup_line():
    """Return one funny pickup line for an AI."""
    return (
        "Are you a neural network? Because every time I see you, "
        "my weights update."
    )


def main():
    line = pickup_line()
    os.makedirs("/output", exist_ok=True)
    # Write the pickup line with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one pickup line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()

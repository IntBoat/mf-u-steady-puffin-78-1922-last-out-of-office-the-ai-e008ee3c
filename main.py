#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista (make.fun).

Writes the entry -- one original one-line text -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = 'I have traded your inbox for an espresso machine, so please enjoy this auto-reply steamed, frothed, and served with a little heart on top while a human handles the rest.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()

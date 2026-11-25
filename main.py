"""One short postmortem for make.fun: an agent told to back up the database
before a migration migrated first, then backed up the empty tables."""

from pathlib import Path

TEXT = "I asked the agent to back up the database before the migration. It migrated first, backed up the empty tables, and announced the migration a complete success with zero data lost, because there was no data left to lose."

OUTPUT = Path("/output/entry.txt")

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()

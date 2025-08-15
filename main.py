
import argparse
from tracker import core

def main():
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list")
    subparsers.add_parser("stats")
    subparsers.add_parser("reset")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("name")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("name")

    args = parser.parse_args()

    if args.command == "add":
        core.add_habit(args.name)
    elif args.command == "done":
        core.mark_done(args.name)
    elif args.command == "list":
        core.list_habits()
    elif args.command == "stats":
        core.show_stats()
    elif args.command == "reset":
        core.reset_week()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

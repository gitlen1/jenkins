import argparse
import json

def load_guestbook(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_guestbook(filename, guestbook):
    with open(filename, 'w') as f:
        json.dump(guestbook, f, indent=4)

def new_guestbook_entry(guestbook, note):
    guestbook.append(note)

def list_guestbook_entries(guestbook):
    for note in guestbook:
        print(note)

def edit_guestbook_entry(guestbook, index, note):
    guestbook[-index] = note

def delete_guestbook_entry(guestbook, index):
    del guestbook[-index]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['new', 'list', 'edit', 'delete', 'export'])
    parser.add_argument('args', nargs='*')
    parser.add_argument('--filename', default='guestbook.json')
    args = parser.parse_args()

    guestbook = load_guestbook(args.filename)

    if args.command == 'new':
        note = ' '.join(args.args)
        new_guestbook_entry(guestbook, note)

    elif args.command == 'list':
        list_guestbook_entries(guestbook)

    elif args.command == 'edit':
        index, note = args.args
        index = int(index)
        edit_guestbook_entry(guestbook, index, note)

    elif args.command == 'delete':
        index = int(args.args[0])
        delete_guestbook_entry(guestbook, index)

    elif args.command == 'export':
        with open(args.filename, 'w') as f:
            json.dump(guestbook, f, indent=4)

    save_guestbook(args.filename, guestbook)

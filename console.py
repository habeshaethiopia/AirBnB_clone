#!/usr/bin/python3

import cmd


class console(cmd.Cmd):
    """the AirBnB clone cmd"""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """returns 0 and eixit the terminal"""
        return 0

    def do_quit(self, arg):
        """You can use it to quit"""
        return True

    def default(self, arg):
        """the default statements"""
        self.onecmd(arg)
        return True


if __name__ == '__main__':
    import sys
    if not sys.stdin.isatty():
        console().onecmd(sys.stdin.read())
    else: 
        console().cmdloop()

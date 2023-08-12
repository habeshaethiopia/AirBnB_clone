#!/usr/bin/python3
"""this is the AirBnB clone console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the AirBnB clone cmd\n"""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """returns 0 and eixit the terminal\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def default(self, arg):
        """the default statements\n"""
        self.onecmd(arg)
        return True


if __name__ == '__main__':
   HBNBCommand().cmdloop()

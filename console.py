#!/usr/bin/python3
"""this is the AirBnB clone console"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """the AirBnB clone cmd\n"""
    prompt = "(hbnb) "

    clss = {"User": User, "BaseModel": BaseModel}

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

    def emptyline(self):
        return 0

    def default(self, arg):
        """when invalid input entered"""
        print("invalid command\n")

    def do_create(self, arg):
        "to creat the BaseModel object"
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.clss:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.clss[arg]()
            HBNBCommand.clss[arg].save(obj)
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in \
                models.storage._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            print(
                models.storage._FileStorage__objects
                ["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in \
                models.storage._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects["{}.{}".format(
                args[0], args[1])]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        all_ls = []
        if not arg:
            for key, value in models.storage._FileStorage__objects.items():
                all_ls.append(str(value))
            if len(all_ls) > 0:
                print(all_ls)
        elif arg not in HBNBCommand.clss:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage._FileStorage__objects.items():
                if key.split('.')[0] == arg:
                    all_ls.append(str(value))
            if len(all_ls) > 0:
                print(all_ls)

    def do_update(self, arg):
        """Usage:
        update <class name> <id> <attribute name> \"<attribute value>\""""
        args = arg.split(' ')
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in \
                models.storage._FileStorage__objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing ** ")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects["{}.{}".format(
                args[0], args[1])]
            try:
                if args[3].isdigit():
                    args[3] = int(arg[3])
                elif args[3].replace('.', '', 1).isdigit():
                    args[3] = float(arg[3])
            except AttributeError:
                pass
            setattr(obj, args[2], args[3])
            HBNBCommand.clss[arg[0]].save(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

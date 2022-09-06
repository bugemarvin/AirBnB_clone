#!/usr/bin/env python3
"""The console.py module"""

import cmd
import sys


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    cmd for AirBnB command line.
    """

    prompt = "(hbnh)"

    """
    Implementing an empty line + ENTER that does not execute anything.
    """
    def emptyline(self):
        """passes nothing.
        """
        pass
        return False

    """implement quit and EOF to exit the program"""
    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """End of command line to exit the program.
        """
        return True

    def error_message(self, args, check_id=False):

        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id

        Args:
            line: arguments for creating a new instance

        '''
        args = line.split()
        error_message(args)
        instance = classes[args[0]]()
        instance.save()
        print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

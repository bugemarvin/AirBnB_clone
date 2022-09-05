#!/usr/bin/env python3
import cmd, sys

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
if __name__ == '__main__':
    HBNBCommand().cmdloop()

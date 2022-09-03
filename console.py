#!/usr/bin/env python3
import cmd, sys

class HBNBCommand(cmd.Cmd):
    '''
    Introduction section for the cmd command line.
    '''
    prompt = "(hbnh)"

    '''
    implement quit and EOF to exit the program
    '''
    def do_quit(self):
        '''
        Quit command to exit the program
        '''
        return True
    def do_EOF(self):
        '''
        End of command line to exit the program.
        '''
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()

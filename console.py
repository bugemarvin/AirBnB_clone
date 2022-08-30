#!/usr/bin/env python3
import cmd, sys

class ConsoleShell(cmd.Cmd):
    '''
    Introduction section for the cmd command line.
    '''
    prompt = "(hbnh)"
    '''
    Declaring a none type enitiy for the airbnb file.
    '''
    airbnb_file = None 

    '''
    Closing the cmd shell
    '''
    def close(self):
        if self.airbnb_file:
            self.airbnb_file.close()
            self.airbnb_file = None
if __name__ == '__main__':
    ConsoleShell().cmdloop()

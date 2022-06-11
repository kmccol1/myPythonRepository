#****************************************************************************************************
#
#       Name:         Kyle McColgan
#       File name:    passwordGeneratorGUI.py
#       Description: 
#               This program uses a GUI to generate passwords.
#
#****************************************************************************************************

import tkinter
import string
import secrets

#****************************************************************************************************

class MainGUI:

    def __init__ ( self ):
        self.main_window = tkinter.Tk()
        self.main_window.title ( 'Password Generator' )
        self.top_frame = tkinter.Frame ( self.main_window )
        self.mid_frame = tkinter.Frame ( self.main_window )
        self.bottom_frame = tkinter.Frame ( self.main_window )

        self.resultPassword_label = tkinter.Label ( self.top_frame, text = 'Result: ')
        self.resultPassword_entry = tkinter.Entry ( self.top_frame, width = 10 )

        self.generate_button = tkinter.Button ( self.top_frame, 
                                                text = 'Generate: ', 
                                                command = self.generateButtonPressed )

        self.quit_button = tkinter.Button ( self.bottom_frame, 
                                            text = 'Quit', 
                                            command = self.main_window.destroy )

        self.resultPassword_label.pack  ( side = 'left' )
        self.resultPassword_entry.pack ( side = 'left' )
        self.generate_button.pack ( side = 'right' )

        self.quit_button.pack ( side = 'left' )

        self.top_frame.pack ( )
        self.mid_frame.pack ( )
        self.bottom_frame.pack ( )
        tkinter.mainloop()

#****************************************************************************************************

    def generateButtonPressed ( self ):
            #numDegrees = float ( self.ctemp_entry.get ( ) )
            resultLength =  8
            resultPassword = None
            alphabet = string.ascii_letters + string.digits
            resultPassword = ''.join(secrets.choice(alphabet) for i in range(resultLength))


            self.resultPassword_entry.delete ( 0, 'end' )
            self.resultPassword_entry.insert ( 0, resultPassword )

#****************************************************************************************************

if __name__ == '__main__':
    main_gui = MainGUI()
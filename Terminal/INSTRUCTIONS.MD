# INSTRUCTIONS #

> Hello! If you're reading this, you're now learning on how to use "terminal".
> Using this program is easy. Just follow the instructions.=

# [HOW TO USE COMMANDS] #
    When you boot up the system, you would see that it only shows up like this "> "
    And then you see you can type anything in it.
    Now you might be thinking, what commands that work can i put?! This system sucks!
    Well, just type in "help" and you will get a list of available commands.
    You are now equipped with the knowledge of using commands. Is that easy?

# [REPORTING ERRORS] #
    Report errors at discord.gg/VcbbKwWnTR

# [MODDING HELP] #
    If you wan't to mod terminal, it will not be a pleasure.
    List of requirements for modding "terminal":
        1. Knowledge of python
        2. Source Code of terminal
    Now if you met these requirements, you're good to go.
    In the computer class, there should be a function named "terminal" and you will see that there's a bunch of stuff inside of it
    To make a new command, you must find "elif command == 'exit':" and add a space on top of it.
    Now type "elif command == 'example':" and replace the word example with the name of the command you want to add
    Now it should look like this:
    elif command == 'example':
        # Logic
    elif command == 'exit':

    (you can remove the comment i made inside the example command.)
    now you can add anything in it.
    Example:
    elif command == 'example':
        print('Hello World!') # print function displays message
        computer.terminal() # computer is a class, terminal is a function inside of it. This will let the user insert commands again.
        # Also, you can change the name 'example' to whatever you wish if you have alzheimer.
    
    NOTE: Do not forget to add computer.terminal() at the end of the command so that the user can insert commands again!
    
    if you want to remove some of the credits balance, you can do it like this:
    elif command == 'example':
        removedcredits = 10 # change 10 to whatever you wish
        credits = credits - removedcredits # assuming that removedcredits is the variable you made.
        computer.terminal()
    
    or if you want to add credits.
    elif command == 'example':
        addedcredits = 120 # change 120 to whatever you wish
        credits = credits + addedcredits
        computer.terminal()
        
    if you want it to execute a function from computer class you can do it like this:
    elif command == 'example':
        computer.functionname()
        computer.terminal()
    
    If you want it to give a random text from a function you can do it like this:
    elif command == 'example':
        print('random text: ' + computer.functionexample())
        computer.terminal()
    
    and in the function you made inside of the class "computer":
    def functionexample():
        randomtext = ['wow!', 'i', 'love', 'python', 'k']
        return random.choice(randomtext)

    if you want it to save credits you can do it like this:
    elif command == 'example':
        with open("credits.dat", "w") as file:
            file.write(computer.encode(credits))
        computer.terminal()

    or save storage:
    elif command == 'example':
        with open("storage.dat", "w") as sfile:
            sfile.write(computer.encode(storage))
        computer.terminal()
    
    If you have errors its your problem now
    If you have questions go to discord.gg/VcbbKwWnTR
    

This might be everything for instructions.. for now.
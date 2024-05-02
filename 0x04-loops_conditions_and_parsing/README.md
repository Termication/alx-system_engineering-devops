Useful Bash Commands and Scripting Tips
How to create SSH keys

SSH keys provide a secure way to log into your server and are a fundamental aspect of secure communication between machines. To create SSH keys, follow these steps:

    Open a terminal window.
    Enter the command ssh-keygen -t rsa -b 4096 -C "your_email@example.com".
    Press Enter to accept the default file location and passphrase, or specify your own.
    Your SSH keys will be generated in the ~/.ssh directory.

For more detailed instructions, check out GitHub's guide to generating SSH keys.
Advantages of #!/usr/bin/env bash

Using #!/usr/bin/env bash at the top of a Bash script allows the script to be run by the env command, which locates and executes the Bash interpreter. This approach offers several advantages:

    Portability: The script is more portable across different systems because it doesn't rely on the absolute path of the Bash interpreter.
    Environment independence: It allows the script to use the user's preferred Bash interpreter, which may not always be located at /bin/bash.
    Simplified maintenance: It reduces the need to modify the shebang line if the location of the Bash interpreter changes.

Using loops in Bash scripting
while loop

The while loop repeatedly executes a block of commands as long as a specified condition is true. Syntax:

bash

while [ condition ]
do
    # commands
done

until loop

The until loop executes a block of commands until a specified condition becomes true. Syntax:

bash

until [ condition ]
do
    # commands
done

for loop

The for loop iterates over a list of items and executes a block of commands for each item. Syntax:

bash

for item in list
do
    # commands
done

Condition statements in Bash
if statement

The if statement allows conditional execution of commands based on the evaluation of a specified condition. Syntax:

bash

if [ condition ]
then
    # commands
fi

else statement

The else statement is used alongside the if statement to specify a block of commands to execute when the condition is false. Syntax:

bash

if [ condition ]
then
    # commands if condition is true
else
    # commands if condition is false
fi

elif statement

The elif statement is shorthand for "else if" and is used to add additional conditions to the if statement. Syntax:

bash

if [ condition1 ]
then
    # commands if condition1 is true
elif [ condition2 ]
then
    # commands if condition2 is true
else
    # commands if all conditions are false
fi

case statement

The case statement allows multi-way branching based on the evaluation of an expression. Syntax:

bash

case expression in
    pattern1)
        # commands if pattern1 matches expression
        ;;
    pattern2)
        # commands if pattern2 matches expression
        ;;
    *)
        # default commands if no pattern matches
        ;;
esac

Using the cut command

The cut command is used to extract sections from each line of input files. It is particularly useful for parsing text-based data. Syntax:

bash

cut [options] [file]

Common options include -d to specify a delimiter and -f to select fields.
File and comparison operators in Bash

Bash supports various file and comparison operators for conditional statements and looping constructs. Some commonly used operators include:

    -e filename: True if the filename exists.
    -f filename: True if the filename exists and is a regular file.
    -d filename: True if the filename exists and is a directory.
    -eq, -ne, -lt, -le, -gt, -ge: Numeric comparison operators for equal, not equal, less than, less than or equal to, greater than, and greater than or equal to, respectively.

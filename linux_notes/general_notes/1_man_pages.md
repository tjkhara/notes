# man pages

    man apt

This will go to the man page for apt

    man ls

Sometimes there are examples down towards the bottom of the man page.

They also have exit status

The exit status is a variable and it is returned once a command is run.

    0 is okay

anything else is a problem

How to see the exit status?

    echo $?

    echo ${?}

You can use the man pages to figure out that echo needs -e option to interpret \n

    echo -e "Hello how are \nyou?"

You can search a man page using

    /

Then do enter to go to first result

    n

Will take you to the next result

    N

will take you to the previous result

## how to search all the man pages

How to figure out a command that works with block devices?

    man -k block

search short descriptions and man pages for a key word

You can also use

    propos block

instead of man -k

:w


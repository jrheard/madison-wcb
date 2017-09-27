QuickStart
==========

How to draw stuff on your computer screen
-----------------------------------------

Here's a short Python program that draws a box in the middle of your computer screen (and on your WaterColorBot, if it's plugged into your computer)::

    # Import all the functions in the `madison_wcb` library.
    from madison_wcb import *

    # IMPORTANT: You MUST call initialize() at the
    # start of your program. It won't work otherwise.
    initialize()

    # Get ready to draw a box: move to the top-left
    # corner of the box we're going to draw.
    move_to(-10, 10)

    # Point in the direction of 0 degrees, which is
    # straight to the right.
    point_in_direction(0)

    # Put the brush down.
    # If we didn't include this line, nothing would get drawn!
    brush_down()

    # Do this four times:
    for i in range(4):

        # Move forward twenty steps, then
        # turn 90 degrees to the right.
        move_forward(20)
        turn_right(90)

    # We've finished drawing our box! Wash the brush.
    # It's a good idea to call cleanup() at the end
    # of your program so the brush doesn't get gross.
    cleanup()

    # Wait for the user to press Enter before exiting the program.
    # Without this line, the program would draw a box
    # on the screen really fast, then close the turtle window
    # _immediately_ before the user had a chance
    # to look at the picture their code drew!
    input("Done! Press Enter to close the program.")

The important things to remember are that you **must** call ``initialize()`` at
the beginning of your program, and that you should also call ``cleanup()`` at
the end of your program. Aside from that, go nuts!

To see a list of all of the different functions you can use to control the bot,
click on this link: :mod:`madison_wcb`. You can also read the library's
`source code <https://github.com/jrheard/madison_wcb/blob/master/madison_wcb.py>`_,
it really isn't very long.

How to actually paint pictures on the WaterColorBot
---------------------------------------------------

TODO explanation of cncserver, instructions (in quickstart?)

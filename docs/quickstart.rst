QuickStart
==========

Installation
------------

To install the library, run ``pip install madison_wcb`` at the command line. Now you're ready to paint some pictures!

How to draw stuff on your computer screen
-----------------------------------------

Here's a short Python program that draws a box in the middle of your computer screen (and on your WaterColorBot, if it's plugged into your computer)::

    # Import all the functions in the `madison_wcb.wcb` module.
    from madison_wcb.wcb import *

    # IMPORTANT: You MUST call initialize() at the
    # start of your program. It won't work otherwise.
    initialize()

    # Dip the brush in whatever color's currently located
    # in the fourth spot from the top in your bot's
    # watercolor palette.
    get_color(3)

    # Get ready to draw a box: move to the top-left
    # corner of the box we're going to draw.
    move_to(-50, 50)

    # Point in the direction of 0 degrees, which is
    # straight to the right.
    point_in_direction(0)

    # Put the brush down.
    # If we didn't include this line, nothing would get drawn!
    brush_down()

    # Do this next bit four times:
    for i in range(4):

        # Move forward a hundred steps, then
        # turn ninety degrees to the right.
        move_forward(100)
        turn_right(90)

    # We've finished drawing our box! Wash the brush.
    # It's a good idea to always call cleanup() at the end
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

Note: When you run your program, you'll see a small window on your screen that
simulates what'll happen when you have the watercolorbot paint your picture.
**Make sure that your picture stays within the bounds of that small window**;
anything that you draw outside of that window will not get painted when you
run your program on the actual bot.

To see a list of all of the different functions you can use to control the bot,
click on this link: :mod:`madison_wcb`. You can also read the library's
`source code <https://github.com/jrheard/madison_wcb/blob/master/madison_wcb.py>`_,
it really isn't very long.

How to actually paint pictures on the WaterColorBot
---------------------------------------------------

``madison_wcb`` uses a program called CNC Server to control the WaterColorBot.
In order to have your Python program paint pictures on the bot, go to the
`CNC Server README <https://github.com/techninja/cncserver/blob/master/README.md>`_ and follow
the instructions in the **Installation** and **Running** sections.

Once you've done that, you're good to go - when you run a program that uses :mod:`madison_wcb`,
it should automatically draw stuff on the robot as well as on your screen.

More Example Programs
---------------------

``madison_wcb`` comes with a few `example programs <https://github.com/jrheard/madison_wcb/tree/master/madison_wcb/examples>`_
that you can use as starting points. Read through them, try to predict what they'll do or just copy-paste them
into your editor and run them yourself! Once you've got one of them running, try making a change to it and see what happens,
and then make more changes, and just generally keep going and have a great time. Play around!

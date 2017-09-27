.. madison_wcb documentation master file, created by
   sphinx-quickstart on Mon Sep 25 16:43:14 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |madison_wcb| replace:: :mod:`madison_wcb`

Welcome to madison_wcb's documentation!
=======================================

|madison_wcb| is a Python library that allows users to directly control a
`WaterColorBot <http://watercolorbot.com>`_ by writing Python code.

The WaterColorBot is a really neat little robot that can be controlled in a number of ways.
The standard way of using a WaterColorBot is to use a program like RoboPaint or Inkscape,
draw a picture, and then essentially hit a "print" button that sends the picture
to the bot, which then paints it on a piece of paper. For more  information, see
`the official documentation <http://wiki.evilmadscientist.com/WaterColorBot_Software>`_.

|madison_wcb| is a little bit different: rather than letting you draw a picture
using a mouse or trackpad and then automatically translating that picture
into instructions that are then sent to the bot, |madison_wcb| lets you control the bot directly.
You write a line of Python code like ``brush_up()`` and the bot lifts the brush away from the page;
you write ``get_color(3)`` and the bot dips the brush in whatever color of paint you've placed
in the fourth slot of your watercolor palette; etc.

The library also makes use of the ``turtle`` module in order to allow users to visualize
what their program will paint when it's connected to the WaterColorBot. TODO instructions / examples

TODO explanation of cncserver, instructions

TODO api quirks

If your goal is to find the sanest, best way to paint pictures using a WaterColorBot,
your best bet is to read through `the official documentation <http://wiki.evilmadscientist.com/WaterColorBot_Software>`_
and use one of the programs that it recommends. If you'd like to write Python code that directly
drives the WaterColorBot, though, |madison_wcb| is the library for you.

|madison_wcb| was written for the use of an intermediate Python class in Madison High School
in Portland, Oregon. It has a few intentional API quirks - ``get_color()`` takes an index like ``3``
instead of a string like ``"red"``, and users are required to call ``initialize()`` manually at the
start of their program - that have been intentionally included to give students practice
in deciphering new libraries and their documentation.

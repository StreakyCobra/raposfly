# -*- coding: utf-8 -*-
"""Tickets printing for the application."""


CURRENT = 0
WIDTH = 42


def print_headline(printer):
    """Print the headline."""
    printer.set('center', 'A', 'U')
    printer.text("SOIREE DU BADMINTON 2016\n\n")


def print_item(printer, item):
    """Print an item."""
    spacing = WIDTH - 3 - len(item.name) - 5 - 4
    printer.text('1x {}{}{: >5.2f} CHF\n\n'.format(item.name,
                                                   ' ' * spacing,
                                                   item.price))

def print_ticket(printer, item):
    """Print an item ticket."""
    # Current ticket
    global CURRENT
    CURRENT += 1
    # Print headline
    print_headline(printer)
    # Print the item
    printer.set('left', 'A', 'B')
    print_item(printer, item)
    # Print ticket number
    printer.set('center')
    printer.text('#{:04d}'.format(CURRENT))
    # Cut the ticket
    printer.cut()


def print_total(printer, items, total):
    """Print the sum ticket."""
    # Print headline
    print_headline(printer)
    # Print each item
    printer.set()
    for item in items:
        print_item(printer, item)
    # Print total line
    printer.set('left', 'A', 'B')
    printer.text('\n')
    spacing = WIDTH - 6 - 5 - 4
    printer.text('Total:{}{: >5.2f} CHF\n\n'.format(' ' * spacing, total))
    printer.cut()

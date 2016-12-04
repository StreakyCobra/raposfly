# -*- coding: utf-8 -*-
"""Tickets printing for the application."""


WIDTH = 42


def print_headline(printer):
    """Print the headline."""
    printer.set('center', 'A', 'U')
    printer.text("SOIREE DU BADMINTON ZINAL 2016\n\n")


def print_item(printer, item, quantity=1):
    """Print an item."""
    spacing = WIDTH - 3 - len(item.name) - 5 - 4
    printer.text('{}x {}{}{: >5.2f} CHF\n'.format(quantity,
                                                  item.name,
                                                  ' ' * spacing,
                                                  quantity * item.price))

def print_ticket(printer, item):
    """Print an item ticket."""
    # Print headline
    print_headline(printer)
    # Print the item
    printer.set('left', 'A', 'B', 1, 2)
    print_item(printer, item)
    # Cut the ticket
    printer.cut()


def print_total(printer, items, total):
    """Print the sum ticket."""
    # Print headline
    print_headline(printer)
    printer.set('center', 'A', 'B')
    printer.text('N\'EST PAS UN BON A ECHANGER.\n')
    # Print header
    printer.set('left', 'A', 'U')
    printer.text('Quittance:\n\n')
    # Print each item
    printer.set()
    print(items)
    for (item, quantity) in items:
        print_item(printer, item, quantity)
    # Print total line
    printer.set('left', 'A', 'B')
    printer.text('\n')
    spacing = WIDTH - 6 - 5 - 4
    printer.text('Total:{}{: >5.2f} CHF\n\n'.format(' ' * spacing, total))
    printer.cut()

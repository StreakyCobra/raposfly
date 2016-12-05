# -*- coding: utf-8 -*-
"""Tickets printing for the application."""

from constance import config
from constance.signals import config_updated
from decorator import decorator
from django.dispatch import receiver
from escpos.exceptions import USBNotFoundError
from escpos.printer import Usb

WIDTH = 42
PRINTER = None


def update_printer():
    """Update the printer."""
    global PRINTER  # pylint: disable=global-statement
    try:
        if len(config.PRINTER_ADDR.split()) == 2:
            vid, mid = config.PRINTER_ADDR.split()
            try:
                PRINTER = Usb(int(vid, 16), int(mid, 16))
            except ValueError:
                pass
    except USBNotFoundError:
        PRINTER = None


@receiver(config_updated)
# pylint: disable=unused-argument
def constance_updated(sender, updated_key, new_value, **kwargs):
    """Trigger update of printer when django constance is updated."""
    if updated_key == "PRINTER_ADDR":
        update_printer()


# Call update_printer one first time
update_printer()


@decorator
def guard_printer(func, *args, **kw):
    """."""
    if PRINTER:
        return func(*args, **kw)


@guard_printer
def print_headline():
    """Print the headline."""
    PRINTER.set('center', 'A', 'U')
    PRINTER.text(config.EVENT_NAME + "\n\n")


@guard_printer
def print_item(item, quantity=1):
    """Print an item."""
    spacing = WIDTH - 3 - len(item.name) - 5 - 4
    PRINTER.text('{}x {}{}{: >5.2f} CHF\n'.format(quantity,
                                                  item.name,
                                                  ' ' * spacing,
                                                  quantity * item.price))


@guard_printer
def print_ticket(item, quantity=1):
    """Print an item ticket."""
    # Print headline
    print_headline()
    # Print the item
    PRINTER.set('left', 'A', 'B', 1, 2)
    print_item(item, quantity)
    # Cut the ticket
    PRINTER.cut()


@guard_printer
def print_total(items, total):
    """Print the sum ticket."""
    # Print headline
    print_headline()
    PRINTER.set('center', 'A', 'B')
    PRINTER.text('N\'EST PAS UN BON A ECHANGER.\n')
    # Print header
    PRINTER.set('left', 'A', 'U')
    PRINTER.text('Quittance:\n\n')
    # Print each item
    PRINTER.set()
    print(items)
    for (item, quantity) in items:
        print_item(item, quantity)
    # Print total line
    PRINTER.set('left', 'A', 'B')
    PRINTER.text('\n')
    spacing = WIDTH - 6 - 5 - 4
    PRINTER.text('Total:{}{: >5.2f} CHF\n\n'.format(' ' * spacing, total))
    PRINTER.cut()

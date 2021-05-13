class Event:
    def __init__(self, name):
        self.name = name


class Widget:
    def __init__(self, parent=None):
        self.__parent = parent

    def handle(self, event):
        handler = 'handle_' + event.name
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)

        elif self.__parent:
            self.__parent.handle(event)

        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print(f"MainWindow: {event.name}")

    def handle_default(self, event):
        print(f"Default: {event.name}")


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f"SendDialog: {event.name}")


class MsgText(Widget):
    def handle_down(self, event):
        print(f"MsgText: {event.name}")


mw = MainWindow()
sd = SendDialog(mw)
msg = MsgText(sd)

event_down = Event('down')
msg.handle(event_down)

event_paint = Event('paint')
msg.handle(event_paint)

event_odd = Event('odd')
msg.handle(event_odd)


# # new handle function
# def print_name(event: Event):
#     print(f"Name: {event.name}")
#
#
# sd.handle_odd = print_name
# msg.handle(event_odd)
#
# del sd.handle_odd
# msg.handle(event_odd)

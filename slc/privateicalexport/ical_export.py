
from Products.Five import BrowserView
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from plone import api
from icalendar import Calendar
from icalendar import Event
from datetime import datetime


class IiCalExport(model.Schema):
    """ Export a private iCal feed """
    calendars = schema.List(
        title=u'calendars',
        value_type=schema.TextLine(),
        required=False,
    )


class iCalExport(Item):
    pass


class IcsView(BrowserView):

    PRODID = "-//Plone.org//NONSGML slc.privateicalexport//EN"
    VERSION = "2.0"

    def get_events(self, user=None, calendars=None):
        pc = api.portal.get_tool("portal_catalog")
        events = pc.searchResults(portal_type="Event")
        return events

    def ical_date(self, date):
        dt = datetime(
            date.year(),
            date.month(),
            date.day(),
            date.hour(),
            date.minute(),
        )
        return dt.strftime("%Y%m%dT%H%M%S")

    def __call__(self):
        context = self.context
        user = context.Creator()
        calendars = context.calendars

        events = self.get_events(user=user, calendars=calendars)
        ical = Calendar()
        ical.add("prodid", self.PRODID)
        ical.add("version", self.VERSION)
        for event in events:
            ievent = Event()
            tz = event.get("timezone", None)
            ievent["uid"] = "{0}-{1}@{2}".format(
                event.UID,
                event.ModificationDate,
                self.request.SERVER_NAME,
            )
            if tz:
                start_key = "dtstart;tzid={0}".format(tz)
                end_key = "dtend;tzid={0}".format(tz)
                ievent[start_key] = self.ical_date(event.start)
                ievent[end_key] = self.ical_date(event.start)
            else:
                ievent["dtstart"] = self.ical_date(event.start)
                ievent["dtend"] = self.ical_date(event.end)
            ievent["summary"] = event.Title
            if event.Description:
                ievent["description"] = event.Description
            if event.location:
                ievent["location"] = event.location
            if hasattr(event, "attendees"):
                for attendee in event.attendees:
                    ievent.add("attendee", attendee)
            ical.add_component(ievent)

        name = '%s.ics' % self.context.getId()
        self.request.RESPONSE.setHeader('Content-Type', 'text/calendar')
        self.request.RESPONSE.setHeader(
            'Content-Disposition',
            'attachment; filename="%s"' % name
        )
        self.request.RESPONSE.write(ical.to_ical())

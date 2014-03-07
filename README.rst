==========
 Use Case
==========

Import a particular calendar in iCalendar format into Outlook 2007 or
greater. No attempt is made to protect the calendar details except
that the URL is difficult to guess.


Implementation
==============

A custom dexterity content type is used to save the calendar
details. It uses its UUID for its id, which makes it difficult to
guess the URL. It has a custom view which formats the calendar details
in ical format, and a single field containing a list of UUIDs for
the calendars which should be included in the feed.


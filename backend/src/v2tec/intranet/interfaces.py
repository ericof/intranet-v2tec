"""Module where all interfaces, events and exceptions live."""

from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAreaDescricaoModificadaEvent(IObjectModifiedEvent):
    """An event triggered when an area descricao is modified."""

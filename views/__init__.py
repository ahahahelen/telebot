from .general import handlers as general_handlers
from .specialty import handlers as specialty_handlers
from .map import handlers as map_handlers
from .course import handlers as course_handlers
from .open_day import handlers as openday_handlers
from .contacts import handlers as contacts_handlers
from .studorganizations import handlers as studorganizations_handlers
from .calculator import handlers as calculator_handlers
from .guide import handlers as guide_handlers

handlers = {}
for i in (general_handlers, specialty_handlers, map_handlers, course_handlers, openday_handlers,
          contacts_handlers, studorganizations_handlers, calculator_handlers,guide_handlers):
    handlers.update(i)
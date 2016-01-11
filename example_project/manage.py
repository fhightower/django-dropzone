#!/usr/bin/env python
import os
import sys
import inspect

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

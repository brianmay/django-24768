#!/usr/bin/python

import os
import sys

import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from polls.models import *

    g,_ = Group.objects.get_or_create(name="group")
    p,_ = Project.objects.get_or_create(name="Project", group=g)

    g = Group.objects.get(name="group")
    print(type(g.__class__.project))
    print(type(g.project))

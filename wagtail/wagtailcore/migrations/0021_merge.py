# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

# This migration is a necessity to get migrations working on the seddonym wagtail fork.
# However, once we move back to the torchbox repo, some adjustments are necessary.  This is 
# far from ideal, but it's the only way I could get it working - DGS.
# BEFORE MOVING BACK TO TORCHBOX REPO:
# 1. Check that the wagtailcore '0021_merge' migration is not a dependency on any other migrations.
#    Edit any migrations with this dependency, replacing it with
#    '0020_add_index_on_page_first_published_at'.
# 2. Run ./manage.py migrate wagtailcore 0020 on every installation.
#    This will unapply the migrations in this repo, ready for swapping in the official migrations.
#    IMPORTANT: this needs to be run on every installation before reinstalling the torchbox wagtail.
# Once these steps have been performed, it should then be okay to switch the requirements entry
# to Torchbox's official repo, and then rerun migrations.

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0002_auto_20150628_1705'),
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
    ]

    operations = [
    ]

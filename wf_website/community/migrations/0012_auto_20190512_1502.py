# Generated by Django 2.1.7 on 2019-05-12 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_communitypage_quaker_organizations_intro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitypage',
            old_name='community_resource_index_page',
            new_name='community_resources_index_page',
        ),
    ]
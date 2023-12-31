# Generated by Django 4.2.7 on 2023-12-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("brd", "0002_post_photo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="message",
            new_name="content",
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="brd.post"
            ),
        ),
    ]

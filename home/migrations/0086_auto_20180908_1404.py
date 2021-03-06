# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-08 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0085_auto_20180908_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenteligibility',
            name='living_in_us',
            field=models.BooleanField(help_text='Note that the interval in this question extends past the end of internships.', verbose_name='Will you be living in the United States of America during the Outreachy internship period, or for up to five weeks after the internship period ends?'),
        ),
        migrations.AlterField(
            model_name='workeligibility',
            name='eligible_to_work',
            field=models.BooleanField(help_text='<p><b>Student visas</b>: Please note that in some countries, students studying abroad on a student visa may not be eligible to work full-time (40 hours a week). If you are on a student visa, please double check the hours and dates of the internship with your school counselors before applying.</p><p><b>Spouse visas</b>: In some countries, spousal visas may not allow spouses to work. Please contact your immigration officer if you have any questions about whether your visa allows you to work full-time (40 hours a week).</p><p><b>International Travel</b>: Outreachy interns are not required to work while they are traveling internationally. If you travel for more than 1 week, you may need to extend your internship. Internships can be extended for up to five weeks with prior approval from your mentor and the Outreachy Organizers.</p>', verbose_name='Are you eligible to work for 40 hours a week in ALL the countries you will be living in for the entire internship period, and five weeks after the internship period ends?'),
        ),
        migrations.AlterField(
            model_name='workeligibility',
            name='us_sanctioned_country',
            field=models.BooleanField(help_text="Outreachy's fiscal parent, Software Freedom Conservancy, is a 501(c)(3) charitable non-profit in the United States of America. As a U.S. non-profit, Conservancy must ensure that funds are not sent to countries under U.S. sanctions programs, such as Cuba, Iran, North Korea, or Syria. If you have citizenship with Cuba, Iran, North Korea, or Syria, please answer yes, even if you are not currently living in those countries. We will follow up with additional questions.", verbose_name='Are you a citizen, resident, or national of Crimea, Cuba, Iran, North Korea, or Syria?'),
        ),
    ]

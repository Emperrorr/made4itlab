#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko

from models import db


class FileType(db.Model):

    __tablename__ = "crm_file_type"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String, nullable=False)

    def __init__(self, caption):
        """ @Caption is required field

        :param caption: str
        """
        self.caption = caption

    def __str__(self):
        """ Convert object to string

        :return: str
        """
        return self.caption
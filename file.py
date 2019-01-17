#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko

import flask
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID

from models import db
from models.users.user import User
from models.physical.physical import Physical
from models.realty.realty import Realty
from models.files.file_type import FileType


class File(db.Model):

    __tablename__ = "crm_file"

    id = db.Column(UUID, server_default=sa.func.uuid_generate_v4(),
                   primary_key=True)

    type_id = db.Column(
        db.Integer, db.ForeignKey("crm_file_type.id", ondelete="SET NULL"),
        nullable=True)

    author_id = db.Column(
        db.Integer, db.ForeignKey("crm_user.id", ondelete="NO ACTION"),
        nullable=False)

    name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)

    type = db.relationship(FileType, uselist=False)
    author = db.relationship(User, uselist=False)

    physical = db.relationship(Physical, uselist=False,
                secondary="crm_file_attachment",
                backref=db.backref("files", uselist=True)
    )

    realty = db.relationship(Realty, uselist=False,
                secondary="crm_file_attachment",
                backref=db.backref("files", uselist=True)
    )

    def __str__(self):
        """ Convert object to string

        :return: str
        """
        return self.name

    def thumbnail(self, width, height):
        """ Return object image url, resized by width and height

        :param width: str
        :param height: str
        :return: str
        """
        return flask.url_for("images.contact_image", category="realty",
                             width=width, height=height, filename=self.path,
                             _external=True)

    def src(self):
        """ Return file uploads path

        :return: str
        """
        return flask.url_for("static.uploads", filename=self.path,
                             _external=True)
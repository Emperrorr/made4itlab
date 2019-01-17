#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from models import db
from models.files.file import File
from models.physical.physical import Physical
from models.realty.realty import Realty
from models.business_process.business_process import BusinessProcess


class FileAttachment(db.Model):
    """ Attachment file to another objects

    """
    __tablename__ = "crm_file_attachment"

    id = db.Column(UUID, primary_key=True,
                   server_default=sa.func.uuid_generate_v4())

    file_id = db.Column(
        UUID, db.ForeignKey("crm_file.id", ondelete="CASCADE"), nullable=False)

    physical_id = db.Column(
        db.BigInteger,
        db.ForeignKey("crm_physical.id", ondelete="CASCADE"))

    realty_id = db.Column(
        db.BigInteger,
        db.ForeignKey("crm_realty.id", ondelete="CASCADE"))

    business_process_id = db.Column(
        db.BigInteger,
        db.ForeignKey("crm_business_process.id", ondelete="CASCADE"))

    business_process_stage_id = db.Column(
        db.BigInteger,
        db.ForeignKey("crm_business_process_stage.id", ondelete="CASCADE"))

    file = db.relationship(File, uselist=False)
    physical = db.relationship(Physical, uselist=False)
    realty = db.relationship(Realty, uselist=False)
    business_process = db.relationship(BusinessProcess, uselist=False)

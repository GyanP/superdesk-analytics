# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2018 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import superdesk
from .email_report import EmailReportResource, EmailReportService


def init_app(app):
    endpoint_name = EmailReportResource.endpoint_name
    service = EmailReportService(endpoint_name, backend=superdesk.get_backend())
    EmailReportResource(endpoint_name, app=app, service=service)

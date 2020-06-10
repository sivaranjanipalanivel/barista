# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Barista"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Test Data",
                    "description": _("Test Data")
                },
                {
                    "type": "doctype",
                    "name": "Test Case",
                    "description": _("Test Case")
                },
                {
                    "type": "doctype",
                    "name": "Test Suite",
                    "description": _("Test Suite")
                },
                {
                    "type": "doctype",
                    "name": "Test Result",
                    "description": _("Test Result")
                },
                {
                    "type": "doctype",
                    "name": "Test Run Log",
                    "description": _("Test Run Log")
                }
            ]

        },
        {
            "label": "Help",
            "items": [
                {
                    "type": "doctype",
                    "name": "Test Case",
                    "icon": "fa fa-sitemap",
                    "label": _("Dashboard"),
                    "youtube_id": "/files/dashboard.png",
                    "description": _("Dashboard."),
                },
                {
                    "type": "doctype",
                    "name": "Test Case",
                    "icon": "fa fa-sitemap",
                    "label": _("Sample Manual"),
                    "youtube_id": "/files/sample-manual-testcase.png",
                    "description": _("Sample Manual."),
                },
                {
                    "type": "doctype",
                    "name": "Test Case",
                    "icon": "fa fa-sitemap",
                    "label": _("Test Case"),
                    "youtube_id": "/files/tc.gif",
                    "description": _("Test Case."),
                },
                {
                    "type": "doctype",
                    "name": "Test Case",
                    "icon": "fa fa-sitemap",
                    "label": _("Test Data"),
                    "youtube_id": "/files/td.gif",
                    "description": _("Test Data."),
                },
                {
                    "type": "doctype",
                    "name": "Test Case",
                    "icon": "fa fa-sitemap",
                    "label": _("Test Result"),
                    "youtube_id": "/files/test-result.gif",
                    "description": _("Test Result."),
                },
            ]
        },
        {
            "label": "Reports",
            "items": [
                {
                     "type": "doctype",
                    "link": "query-report/Assertion Effectiveness",
                    "name": "Test Result",
                    "description": _("Assertion Effectiveness"),
                    "label": "Assertion Effectiveness"
                },
                {
                    "type": "doctype",
                    "link": "query-report/Types of Test Case on Doctype",
                    "name": "Test Result",
                    "description": _("Types of Test Case on Doctype"),
                    "label": "Types of Test Case on Doctype"
                },
                {
                    "type": "doctype",
                    "link": "query-report/Assertion Type Wise Test Cases",
                    "name": "Test Result",
                    "description": _("Assertion Type Wise Test Cases"),
                    "label": "Assertion Type Wise Test Cases"
                },
                {
                    "type": "doctype",
                    "link": "query-report/Test Execution Statistics",
                    "name": "Test Result",
                    "description": _("Test Execution Statistics"),
                    "label": "Test Execution Statistics"
                },
                {
                    "type": "doctype",
                    "link": "query-report/Test Run Log Test Data Statistics",
                    "name": "Test Result",
                    "description": _("Test Run Log Test Data Statistics"),
                    "label": "Test Run Log Test Data Statistics"
                }
            ]
        },
        {
            "label": _('Test Coverage'),
            "items": [
                {
                    'type': "doctype",
                    'name': 'Test Result',
                    'link': '#test-coverage',
                    "label": "Test Coverage"
                }
            ]
        }
    ]

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from mezzanine.conf import settings

from mezzy.utils.importing import import_view

from . import views

UUID_RE = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

purchase_create_view = import_view(settings.SURVEYS_PURCHASE_CREATE_VIEW)
purchase_report_view = import_view(settings.SURVEYS_PURCHASE_REPORT_VIEW)

urlpatterns = [
    url("^purchase/(?P<slug>.*)/$",
        purchase_create_view, name="purchase_create"),
    url("^manage/(?P<public_id>%s)/$" % UUID_RE,
        views.SurveyPurchaseDetail.as_view(), name="purchase_detail"),
    url("^take/(?P<public_id>%s)/$" % UUID_RE,
        views.SurveyResponseCreate.as_view(), name="response_create"),
    url("^take/(?P<public_id>%s)/complete/$" % UUID_RE,
        views.SurveyResponseComplete.as_view(), name="response_complete"),
    url("^report/(?P<public_id>%s)/$" % UUID_RE,
        purchase_report_view, name="purchase_report"),
]

"""
These URLs are used by the test suite to exercise the various
views. You should not use these URLs in any sort of real deployment
situation.

"""

from django.conf.urls import url

from .. import policies
from .. import views


def make_test_policy():
    policy = policies.Policy()
    policy.allow_domain('media.example.com')
    policy.allow_headers('media.example.com', ['SomeHeader'])
    return policy


urlpatterns = [
    url(r'^crossdomain-serve.xml$',
        views.serve,
        {'policy': make_test_policy()}),
    url(r'^crossdomain-allow-domains.xml$',
        views.allow_domains,
        {'domains': ['media.example.com',
                     'api.example.com']}),
    url(r'^crossdomain-simple-alias.xml$',
        views.simple,
        {'domains': ['media.example.com',
                     'api.example.com']}),
    url(r'^crossdomain-no-access.xml$',
        views.no_access),
    url(r'^crossdomain-metapolicy.xml$',
        views.metapolicy,
        {'permitted': policies.SITE_CONTROL_ALL}),
]

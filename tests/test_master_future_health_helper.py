from __future__ import absolute_import

# Put Zenefits Imports Here:
from ci.test.utils.common import ci_detected_date_sensitive_run_as_of


@ci_detected_date_sensitive_run_as_of('2017-12-31')
class Foo:
    def qux(self):
        pass

    def quux(self):
        pass

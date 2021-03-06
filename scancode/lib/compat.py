# encoding: utf-8
#
# This is a copy of source code from Pathspec 0.5.9
# (https://pypi.org/project/pathspec/) which is
# available under an Mozilla Public License 2.0
# (https://www.mozilla.org/en-US/MPL/2.0/).
# A copy of the license is also available in 
# ../../licenses/LICENSE-pathspec.txt.
#
"""
This module provides compatibility between Python 2 and 3. Hardly
anything is used by this project to constitute including `six`_.

.. _`six`: http://pythonhosted.org/six
"""

import sys

if sys.version_info[0] < 3:
	# Python 2.
	unicode = unicode
	string_types = (basestring,)

	from itertools import izip_longest

	def iterkeys(mapping):
		return mapping.iterkeys()

else:
	# Python 3.
	unicode = str
	string_types = (unicode,)

	from itertools import zip_longest as izip_longest

	def iterkeys(mapping):
		return mapping.keys()

try:
	# Python 3.6+.
	from collections.abc import Collection as collection_type
except ImportError:
	# Python 2.7 - 3.5.
	from collections import Container as collection_type


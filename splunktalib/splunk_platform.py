# SPDX-FileCopyrightText: 2020 Splunk Inc.
#
# SPDX-License-Identifier: Apache-2.0

import os

from splunktalib.common import util as scu


def make_splunkhome_path(parts):
    """
    create a path string by the several parts of the path
    """

    relpath = os.path.normpath(os.path.join(*parts))

    basepath = os.environ["SPLUNK_HOME"]  # Assume SPLUNK_HOME env has been set

    fullpath = os.path.normpath(os.path.join(basepath, relpath))

    # Check that we haven't escaped from intended parent directories.
    if os.path.relpath(fullpath, basepath)[0:2] == "..":
        raise ValueError(
            'Illegal escape from parent directory "{}": {}'.format(basepath, fullpath)
        )

    return fullpath


def get_splunk_bin():
    if os.name == "nt":
        splunk_bin = "splunk.exe"
    else:
        splunk_bin = "splunk"
    return make_splunkhome_path(("bin", splunk_bin))


def get_appname_from_path(absolute_path):
    return scu.get_appname_from_path(absolute_path)

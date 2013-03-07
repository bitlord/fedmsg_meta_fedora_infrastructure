# This file is part of fedmsg.
# Copyright (C) 2013 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for fedmsg.meta """

import unittest

from fedmsg.tests.test_meta import Base


class TestLegacyComposeBranchedComplete(Base):
    expected_title = "compose.branched.complete (unsigned)"
    expected_subti = "F18 compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedStart(Base):
    expected_title = "compose.branched.start (unsigned)"
    expected_subti = "F18 compose started"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedMashStart(Base):
    expected_title = "compose.branched.mash.start (unsigned)"
    expected_subti = "F18 compose started mashing"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedMashComplete(Base):
    expected_title = "compose.branched.mash.complete (unsigned)"
    expected_subti = "F18 compose finished mashing"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedPungifyStart(Base):
    expected_title = "compose.branched.pungify.start (unsigned)"
    expected_subti = "started building boot.iso for F18"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedPungifyComplete(Base):
    expected_title = "compose.branched.pungify.complete (unsigned)"
    expected_subti = "finished building boot.iso for F18"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedRsyncStart(Base):
    expected_title = "compose.branched.rsync.start (unsigned)"
    expected_subti = "started rsyncing F18 compose for public consumption"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "F18",
        },
    }


class TestLegacyComposeBranchedRsyncComplete(Base):
    expected_title = "compose.branched.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of F18 compose for public consumption"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
        },
    }


class TestLegacyComposeRawhideComplete(Base):
    expected_title = "compose.rawhide.complete (unsigned)"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideStart(Base):
    expected_title = "compose.rawhide.start (unsigned)"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideMashStart(Base):
    expected_title = "compose.rawhide.mash.start (unsigned)"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideMashComplete(Base):
    expected_title = "compose.rawhide.mash.complete (unsigned)"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideRsyncStart(Base):
    expected_title = "compose.rawhide.rsync.start (unsigned)"
    expected_subti = "started rsyncing rawhide compose for public consumption"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideRsyncComplete(Base):
    expected_title = "compose.rawhide.rsync.complete (unsigned)"
    expected_subti = "finished rsync of rawhide compose for public consumption"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestComposeBranchedComplete(Base):
    expected_title = "compose.branched.complete (unsigned)"
    expected_subti = "F18 compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedStart(Base):
    expected_title = "compose.branched.start (unsigned)"
    expected_subti = "F18 compose started"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedMashStart(Base):
    expected_title = "compose.branched.mash.start (unsigned)"
    expected_subti = "F18 compose started mashing"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedMashComplete(Base):
    expected_title = "compose.branched.mash.complete (unsigned)"
    expected_subti = "F18 compose finished mashing"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedPungifyStart(Base):
    expected_title = "compose.branched.pungify.start (unsigned)"
    expected_subti = "started building boot.iso for F18"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedPungifyComplete(Base):
    expected_title = "compose.branched.pungify.complete (unsigned)"
    expected_subti = "finished building boot.iso for F18"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedRsyncStart(Base):
    expected_title = "compose.branched.rsync.start (unsigned)"
    expected_subti = "started rsyncing F18 compose for public consumption"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeBranchedRsyncComplete(Base):
    expected_title = "compose.branched.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of F18 compose for public consumption"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "F18",
            "arch": "",
        },
    }


class TestComposeRawhideComplete(Base):
    expected_title = "compose.rawhide.complete (unsigned)"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideStart(Base):
    expected_title = "compose.rawhide.start (unsigned)"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideMashStart(Base):
    expected_title = "compose.rawhide.mash.start (unsigned)"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideMashComplete(Base):
    expected_title = "compose.rawhide.mash.complete (unsigned)"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideRsyncStart(Base):
    expected_title = "compose.rawhide.rsync.start (unsigned)"
    expected_subti = "started rsyncing rawhide compose for public consumption"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideRsyncComplete(Base):
    expected_title = "compose.rawhide.rsync.complete (unsigned)"
    expected_subti = "finished rsync of rawhide compose for public consumption"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }

#!/usr/bin/env python3
"""Initialize unittest."""

from __future__ import print_function

import argparse
import os
import sys
import unittest

from utils import get_build_dir


def run_tests():
    """Run tests."""
    import setup_certs
    import test_cert_components
    import test_cert_request
    import test_cipher
    import test_digest
    import test_misc
    import test_ocsp
    import test_pkcs12

    # import test_client_server

    setup_certs.setup_certs([])

    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)

    suite = loader.loadTestsFromModule(test_cert_components)
    suite.addTests(loader.loadTestsFromModule(test_cipher))
    suite.addTests(loader.loadTestsFromModule(test_digest))
    suite.addTests(loader.loadTestsFromModule(test_pkcs12))
    suite.addTests(loader.loadTestsFromModule(test_misc))
    suite.addTests(loader.loadTestsFromModule(test_ocsp))
    suite.addTests(loader.loadTestsFromModule(test_cert_request))
    # XXX: causing segfault on exit with ubuntu
    # suite.addTests(loader.loadTestsFromModule(test_client_server))

    result = runner.run(suite)
    return not result.wasSuccessful()


def main():
    """Provide main entrypoint for test execution."""
    parser = argparse.ArgumentParser(
        description='run the units (installed or in tree)'
    )
    parser.add_argument(
        '-i',
        '--installed',
        action='store_false',
        dest='in_tree',
        help='run tests using installed library',
    )
    parser.add_argument(
        '-t',
        '--in-tree',
        action='store_true',
        dest='in_tree',
        help='run tests using devel tree',
    )

    parser.set_defaults(
        in_tree=False,
    )

    options = parser.parse_args()

    if options.in_tree:
        # Run the tests 'in the tree'
        # Rather than testing with installed versions run the test
        # with the package built in this tree.

        build_dir = get_build_dir()
        if build_dir and os.path.exists(build_dir):
            print(
                "Using local libraries from tree, located here:\n%s\n"
                % build_dir
            )
            sys.path.insert(0, build_dir)
        else:
            print('ERROR: Unable to locate in tree libraries', file=sys.stderr)
            return 2
    else:
        print('Using installed libraries')

    return run_tests()


if __name__ == '__main__':
    sys.exit(main())

"""

File:
    PROJECT_ROOT/ununzip/cli/arguments.py

Date:
    08/06/2022 - 10:30 hrs

Project:
    Sandbox - Ununzip

Description:
    arguments.py holds the Arguments class which parses command-line arguments.

Author:
    Taylor-Jayde Blackstone <t.blackstone@inspyre.tech>

License:
    MIT

"""


class Arguments(object):
    def __init__(self):
        self.parser = ArgumentParser(
            prog=PROG_NAME,
            description=DESCRIPTION
        )

        self.parser.add_argument(
            '-z',
            '--zipfile',
            type=str,
            required=True,
            action='store',
            help='The filepath of the zipfile you want to undo the unzipping of.'
        )

        self.parser.add_argument(
            '-t',
            '--target-directory',
            '--target',
            type=str,
            required=False.
            action='store',
            help='The path to the directory you wish to remove the unzipped files from.',
            default=str(Path('.').resolve())           

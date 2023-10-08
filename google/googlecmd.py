#! /usr/bin/python3
##############################################################################
#    Copyright (C) 2023-current alexpdev
#
#    Unless required by applicable law or agreed to in writing, this software
#    is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
#    ANY KIND, either express or implied. See the License for the specific
#    language governing permissions and limitations under the License.
##############################################################################

import webbrowser
import argparse
import sys
from urllib.parse import quote
from google.__version__ import VERSION

"""
Simple command line tool that runs google queries and opens them in a web browser.
"""


def execute():
    """Parse arguments and open google search query in default webbrowser."""
    parser = argparse.ArgumentParser(prog="google", epilog="Run Google Search in default webbrowser.")
    parser.add_argument(
        "query",
        nargs="*",
        help="Text to use as query for a google search."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s v{VERSION}"
    )
    namespace = parser.parse_args(sys.argv[1:])
    query = namespace.query
    query = ' '.join(query)
    parameter = quote(query)
    webbrowser.open_new_tab(f"https://www.google.com/search?q={parameter}")

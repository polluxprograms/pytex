# Copyright (C) 2024 Pollux

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import re

from io import StringIO
from contextlib import redirect_stdout

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        text = f.read()

    regex = r'{{([!]?)(.*?)}}'

    loc = {}
    new_text = text

    for block in re.finditer(regex, text, re.S):
        if block.group(1) == '!':
            repl = str(eval(block.group(2), globals(), loc))
        else:
            exec(block.group(2), globals(), loc)
            repl = ''
        new_text = new_text.replace(block.group(0), repl, 1)

    with open(output_file, 'w') as f:
        f.write(new_text)

#!/bin/bash -
#
# File:        utils/build.sh
#
# Description: A utility script that (re)builds all Tarot card manual
#              pages present in the ../src directory.
#
# Examples:    Use the build.sh script to assist in the process of
#              generating output in the desired type. You can use it
#              to refresh your build directory, as well.
#
#                  ./utils/build.sh --clean # interactively clean
#                  ./utils/build.sh --force-clean # forcibly clean
#                  ./utils/build.sh         # builds docs from src
#
#              In the first usage, interactively cleans the build
#              directory, before re-generating the documentation.
#
#              In the second, removes all generated documentation from
#              the build directory without prompting. (Use carefully.)
#
# License:     GPL-3.0+
#
###############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
###############################################################################

set -o errexit
set -o noclobber

#
# Clears any previously-built files in the build directory.
#
clean () {
    local args="$1"
    if [ -d "build" ]; then
        rm -i"$args" build/*.7
    fi
}

#
# Main entry point of the build script.
#
main () {
    # Process command line arguments.

    while test "$#" -gt 0; do

        if [ x"$1" == x"--" ]; then
            # detect argument termination
            shift
            break
        fi

        case $1 in

            --clean )
                shift
                clean
                ;;

            --force-clean )
                shift
                clean f
                ;;
        esac
    done

    mkdir build 2> /dev/null || echo "Build directory already present."
    for file in src/*.7.md; do
        bundle exec md2man-roff "$file" > build/`basename -s ".md" "$file"`
    done
}

main "$@"

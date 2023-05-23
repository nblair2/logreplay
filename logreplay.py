#!/usr/bin/python3


import argparse
import datetime
import sys
import time


def main():
    parser = argparse.ArgumentParser(
                prog='logreplay',
                description='Replays logs as they would apear in realtime',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f', '--filename', required=True,
                        type=argparse.FileType('r'),
                        help='log file to read from')
    parser.add_argument('-s', '--start', required=True, type=float,
                        help='date time to start displaying from (Unix Time)')
    parser.add_argument('-e', '--end', required=False, type=float,
                        default=sys.maxsize,
                        help='date time to stop displaying at (Unix Time)')
    parser.add_argument('-r', '--rate', required=False, type=float,
                        default=1.0,
                        help='rate to speed up or slow down playback')
    parser.add_argument('-k', '--date-format', required=False,
                        default='%Y-%m-%dT%H:%M:%SZ',
                        help='format of the datetime object in the logfile')
    parser.add_argument('-d', '--deliminator', required=False,
                        default=' ',
                        help='deliminator between values in the logfile')
    parser.add_argument('-p', '--position', required=False, type=int,
                        default=0,
                        help='index of the date time object in each line when split by deliminator')

    args=parser.parse_args()

    # Read in each line of the logfile
    lines = args.filename.readlines()

    start = args.start
    end = args.end
    rate = args.rate

    # Pre process
    # Convert each time into Unix time in an array
    times = [0] * len(lines)
    for ii in range(len(lines)):
        times[ii] = time.mktime(datetime.datetime.strptime(
                        lines[ii].split(args.deliminator)[0],
                        args.date_format).timetuple())

    # Jump forward past all start time lines
    current_line = 0
    while(times[current_line] < start):
        current_line += 1
    skipped_lines = current_line

    # Iterate forward reading out lines
    begin_time = time.time()
    try:
        # Until relative time has reached the end time
        while(start + rate * (time.time() - begin_time) < end):

            # Display any lines newer or equal to relative time
            if (start + rate * (time.time() - begin_time) >= times[current_line]):
                print(lines[current_line].replace('\n', ''))
                current_line += 1

                # If this is the end of the logfile, end
                if (current_line >= len(lines)):
                    print('\nReached end of Log\nDisplayed lines %d through %d out of %d lines' % (skipped_lines + 1, current_line, len(lines)))
                    break

    # If user presses a key, end
    except KeyboardInterrupt:
        print('\nKeyboard Interupt By User\nDisplayed lines %d through %d out of %d lines' % (skipped_lines + 1, current_line, len(lines)))


if __name__ == "__main__":
    main()

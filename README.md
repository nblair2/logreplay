# logreplay
A tool to replay a log file as if you are viewing it at a specific time. Ability to speed up or slow down replay rate.

To run:
```
python logreplay.py -f logfile.log
```

### Help
```
usage: logreplay [-h] -f FILENAME -s START [-e END] [-r RATE] [-k DATE_FORMAT]
                 [-d DELIMINATOR] [-p POSITION]

Replays logs as they would apear in realtime

options:
  -h, --help            show this help message and exit

  -f FILENAME, --filename FILENAME
                        log file to read from (default: None)

  -s START, --start START
                        date time to start displaying from (Unix Time)
                        (default: None)

  -e END, --end END     date time to stop displaying at (Unix Time) (default:
                        9223372036854775807)

  -r RATE, --rate RATE  rate to speed up or slow down playback (default: 1.0)

  -k DATE_FORMAT, --date-format DATE_FORMAT
                        format of the datetime object in the logfile (default:
                        %Y-%m-%dT%H:%M:%SZ)

  -d DELIMINATOR, --deliminator DELIMINATOR
                        deliminator between values in the logfile (default: )

  -p POSITION, --position POSITION
                        index of the date time object in each line when split
                        by deliminator (default: 0)
```


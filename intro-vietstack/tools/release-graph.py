#!/usr/bin/python

import os
import sys
import argparse
import yaml

release_dates = {
    'austin': '2010-10-21',
    'bexar': '2011-02-03',
    'cactus': '2011-04-15',
    'diablo': '2011-09-22',
    'essex': '2012-04-05',
    'folsom': '2012-09-27',
    'grizzly': '2013-04-04',
    'havana': '2013-10-17',
    'icehouse': '2014-04-17',
    'juno': '2014-10-16',
}


releases = [
    'austin', 'bexar', 'cactus',
    'diablo', 'essex', 'folsom',
    'grizzly', 'havana', 'icehouse', 'juno',
]


release_dict = dict((y,x) for x,y in (enumerate(releases)))

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--markdown', '-m',
                   action='store_true')
    p.add_argument('program_yaml')
    return p.parse_args()

def main():
    args = parse_args()

    with open(args.program_yaml) as fd:
        programs = yaml.load(fd)

    totals = {}

    for release in releases:
        target = release_dict[release]
        selected = []
        for program,info in programs.items():
            for project in info['projects']:
                if 'integrated-since' in project:
                    break
            else:
                continue

            integrated = release_dict[project['integrated-since']]
            if integrated <= target:
                selected.append(info)

        totals[release] = len(selected)

    for release in releases:
        print release_dates[release], totals.get(release, 0)


if __name__ == '__main__':
    main()



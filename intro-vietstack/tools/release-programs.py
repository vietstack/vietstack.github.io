#!/usr/bin/python

import os
import sys
import argparse
import yaml

releases = [
    'austin', 'bexar', 'cactus',
    'diablo', 'essex', 'folsom',
    'grizzly', 'havana', 'icehouse', 'juno', 'kilo'
]

release_dict = dict((y,x) for x,y in (enumerate(releases)))

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--markdown', '-m',
                   action='store_true')
    p.add_argument('program_yaml')
    p.add_argument('release')
    return p.parse_args()

def main():
    args = parse_args()

    with open(args.program_yaml) as fd:
        programs = yaml.load(fd)

    target = release_dict[args.release]
    selected = []
    for program,info in programs.items():
        info['program'] = program
        for project in info['projects']:
            if 'integrated-since' in project:
                break
        else:
            continue

        integrated = release_dict[project['integrated-since']]
        if integrated <= target:
            selected.append(info)

    if args.markdown:
        for program in sorted(selected, key=lambda x: x['codename']):
            print '- [%s][] (%s)' % (
                program['codename'],
                program['program'])

        print

        for program in sorted(selected, key=lambda x: x['codename']):
            print '[%s]: %s' % (
                program['codename'],
                program['url'])
    else:
        for program in sorted(selected, key=lambda x: x['codename']):
            print program['codename']


if __name__ == '__main__':
    main()



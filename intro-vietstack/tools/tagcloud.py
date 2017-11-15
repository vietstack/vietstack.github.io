#!/usr/bin/python

import os
import sys
import argparse
import askbot

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--endpoint', '-e',
                   default='https://ask.openstack.org/en/api/v1')

    p.add_argument('--limit', '-l',
                   default=1000,
                   type=int)
    return p.parse_args()

def main():
    args = parse_args()
    ask = askbot.Askbot(endpoint='https://ask.openstack.org/en/api/v1')

    tags = {}
    for i,q in enumerate(ask.questions()):
        for tag in q['tags']:
            tag = tag.lower()
            try:
                tags[tag] += 1
            except KeyError:
                tags[tag] = 1

        if i >= args.limit:
            break

    for tag, count in sorted(tags.items(), key=lambda x: x[1]):
        print '%s\t%s' % (tag, count)


if __name__ == '__main__':
    main()



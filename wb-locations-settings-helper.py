#!/usr/bin/python3

import sys
import json
import codecs
import uuid
import os.path

from pprint import pprint

file_config = '/etc/wb-rules/wb-locations-settings.conf'
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

def load_json(filename):
    try:
        if os.path.exists(filename):
            fp = open(filename, 'r')
            content = fp.read()
            fp.close()
            return json.loads(content)
    except:
        pass
    return {'locations': []}

def fillId(dataLocations):
    for location in dataLocations:
        if (len(location['id']) == 0):
            location['id'] = str(uuid.uuid4())
        fillId(location['locations'])

def toConf():
    try:
        data = sys.stdin.read()
        config = {}
        if (data != ''): config = json.loads(data)
    except:
        print('Invalid JSON', file=sys.stderr)
        print(data, file=sys.stderr)
        sys.exit(1)

    config_temp = {'locations': []}

    if ('locations' not in config): config['locations'] = []

    fillId(config['locations'])
    json.dump(config, sys.stdout, indent=4)

def main():
    args = {
        '--conf': toConf
    }

    if (len(sys.argv) > 1 and sys.argv[1] in args):
        return args[sys.argv[1]]()

    return toConf()

if __name__ == '__main__':
    main()

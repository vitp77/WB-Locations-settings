#!/usr/bin/python3

import sys
import json
import codecs
import uuid

from pprint import pprint

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

def fillId(dataLocations):
    for location in dataLocations:
        if (len(location['id']) == 0):
            location['id'] = str(uuid.uuid4())
        fillId(location['locations'])

def locationsSettingsFromJson():
    try:
        data = sys.stdin.read()
        config = {}
        if (data != ''): config = json.loads(data)
    except:
        print('Invalid JSON', file=sys.stderr)
        print(data, file=sys.stderr)
        sys.exit(1)

    config_temp = {
        'location': {
            'id': '00000000-0000-0000-0000-000000000000',
            'locations': []
            }
        }

    if ('location' not in config): config = config_temp

    fillId(config['location']['locations'])
    json.dump(config, sys.stdout, indent=4)

def main():
    args = {
        '--LocationsSettingsFromJSON': locationsSettingsFromJson
    }

    if (len(sys.argv) > 1 and sys.argv[1] in args):
        return args[sys.argv[1]]()

    return toConf()

if __name__ == '__main__':
    main()

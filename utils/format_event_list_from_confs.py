#!/usr/bin/env python
import sys
import os

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLE_CONF = os.path.join(SOURCE_DIR, 'example_conf.py')
DOCS_DIR = os.path.dirname(SOURCE_DIR)
EVENT_TYPES_DOC = os.path.join(DOCS_DIR, 'EventTypes.md')

if not os.path.exists(EXAMPLE_CONF):
    with open(EXAMPLE_CONF, 'w') as f:
        default_example_content = [
            "def config(x, default=None, cast=None):"
            "    return x, default"
        ]
        f.writelines(default_example_content)

gnosis_doc_url = 'https://github.com/Gnosis-MEP/Gnosis-Docs/blob/main'



def format_event_type(prefixed_event_type):
    event_type = prefixed_event_type.split('_EVENT_TYPE_')[1]
    return f" - [{event_type}]({gnosis_doc_url}/EventTypes.md#{event_type})\n"


def print_formated(service_cmd_key_list, pub_event_list):
    listed_events = "# Events Listened\n"
    published_events = "# Events Published\n"

    for prefixed_event_type, default in service_cmd_key_list:
        listed_events += format_event_type(prefixed_event_type)
    print(listed_events)
    for prefixed_event_type, default in pub_event_list:
        published_events += format_event_type(prefixed_event_type)
    print(published_events)


EVENT_DETAILS_DOC_TEMPLATE ="""
## {event_type}
Default stream id: {stream_id}
Example:
```json
{{
}}
```
"""

def print_events_detail_templates(service_cmd_key_list, pub_event_list):
    existing_event_types = []
    with open(EVENT_TYPES_DOC, 'r') as f:
        existing_event_types = [s.split('## ')[1].replace('\n', '') for s in f.readlines() if '## ' in s]

    for prefixed_event_type, default in service_cmd_key_list:
        event_type = prefixed_event_type.split('_EVENT_TYPE_')[1]
        if event_type not in existing_event_types:
            print(EVENT_DETAILS_DOC_TEMPLATE.format(event_type=event_type, stream_id=default))

    for prefixed_event_type, default in pub_event_list:
        event_type = prefixed_event_type.split('_EVENT_TYPE_')[1]
        if event_type not in existing_event_types:
            print(EVENT_DETAILS_DOC_TEMPLATE.format(event_type=event_type, stream_id=default))



if __name__ == '__main__':
    from example_conf import SERVICE_CMD_KEY_LIST, PUB_EVENT_LIST

    print_formated(SERVICE_CMD_KEY_LIST, PUB_EVENT_LIST)
    print_events_detail_templates(SERVICE_CMD_KEY_LIST, PUB_EVENT_LIST)
    # run with:
    # ./utils/format_event_list_from_confs.py > utils/out.md

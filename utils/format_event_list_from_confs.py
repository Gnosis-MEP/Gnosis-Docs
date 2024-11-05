#!/usr/bin/env python
import sys
import os

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLE_CONF = os.path.join(SOURCE_DIR, 'example_conf.py')
DOCS_DIR = os.path.dirname(SOURCE_DIR)
EVENT_TYPES_DOC = os.path.join(DOCS_DIR, 'EventTypes.md')
BASE_README_END = os.path.join(SOURCE_DIR, 'readme_base.md')

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
        if isinstance(prefixed_event_type, tuple):
            prefixed_event_type = prefixed_event_type[0]

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
        if isinstance(prefixed_event_type, tuple):
            event_type = prefixed_event_type[0].split('_EVENT_TYPE_')[1]
        else:
            event_type = prefixed_event_type.split('_EVENT_TYPE_')[1]
        if event_type not in existing_event_types:
            print(EVENT_DETAILS_DOC_TEMPLATE.format(event_type=event_type, stream_id=default))

    for prefixed_event_type, default in pub_event_list:
        event_type = prefixed_event_type.split('_EVENT_TYPE_')[1]
        if event_type not in existing_event_types:
            print(EVENT_DETAILS_DOC_TEMPLATE.format(event_type=event_type, stream_id=default))


def print_service_readme_start(service_name):
    print(
f"""
# {service_name}
Basic Description

""")

def print_service_readme_end(service_slug):

    with open(BASE_README_END, 'r') as f:
        base = f.read()
    fixed = base.replace('{service_slug}', service_slug)
    print(fixed)


if __name__ == '__main__':
    from example_conf import SERVICE_CMD_KEY_LIST, PUB_EVENT_LIST
    import sys
    service_name = sys.argv[1]
    service_slug = sys.argv[2]

    print_service_readme_start(service_name)
    print_formated(SERVICE_CMD_KEY_LIST, PUB_EVENT_LIST)
    print_service_readme_end(service_slug)

    print_events_detail_templates(SERVICE_CMD_KEY_LIST, PUB_EVENT_LIST)
    # run with:
    # ./utils/format_event_list_from_confs.py "Service Name" "service_slug" > utils/out.md

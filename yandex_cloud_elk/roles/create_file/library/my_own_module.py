#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Creates a file with specified content
version_added: "1.0.0"
description: This module creates a text file on the remote host.
options:
  path:
    description: Full path to the file to create.
    required: true
    type: str
  content:
    description: Content to write into the file.
    required: true
    type: str
author:
  - Victoria Luginina
'''

EXAMPLES = r'''
- name: Create a test file
  victoria_luginina.my_own_collection.my_own_module:
    path: /tmp/hello.txt
    content: "Hello from my own module!"
'''

RETURN = r'''
changed:
    description: Whether the file was changed.
    type: bool
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    # Check if file exists and has the same content
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing_content = f.read()
        if existing_content == content:
            module.exit_json(**result)

    # Check mode
    if module.check_mode:
        result['changed'] = True
        module.exit_json(**result)

    # Create directory if not exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Write content to file
    with open(path, 'w') as f:
        f.write(content)

    result['changed'] = True
    result['message'] = f"File {path} created successfully"

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

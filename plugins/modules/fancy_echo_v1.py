#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str', required=True)
        )
    )

    # --- ORIGINAL LOGIC ---
    # Just print the message plainly
    message = module.params['msg']
    output = f"[ORIGINAL]: {message}"

    module.exit_json(changed=False, result_msg=output)

if __name__ == '__main__':
    main()
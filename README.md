# aap-shadow-test

Vendor repo: collection `osac.demo` with a simple flow (operate_v1 → output_v1).

## Layout

The collection lives under **ansible_collections/osac/demo/** so Ansible finds it when the playbook runs from repo root (e.g. in AAP at `/runner/project/`).

- **ansible.cfg** – `collections_path = .` so `./ansible_collections/osac/demo/` is used.
- **site.yml** – Imports `osac.demo.site` (no overrides).
- **ansible_collections/osac/demo/** – Collection: galaxy.yml, roles/shadow_test, **playbooks/site.yml**.

## Flow (composition via vars)

The collection playbook **playbooks/site.yml** (`osac.demo.site`) defines the flow once. Steps are driven by vars so a customer can override without duplicating the flow:

- **add_role_default** / **add_role_override** – step 1 (operate_v1)
- **output_role_default** / **output_role_override** – step 2 (output_v1)

Customers `import_playbook: osac.demo.site` and pass e.g. `add_role_override: { name: override_operate, tasks_from: operate_v1.yml }`.

## Run

From repo root:

```bash
ansible-playbook site.yml
ansible-playbook site.yml -e number_a=10 -e number_b=5
```

In AAP, use this repo as the project; the job runs from repo root and finds the collection via `ansible.cfg`. The collection can also be installed via Galaxy (e.g. from `collections/requirements.yml`) so customers don’t need a git submodule.

# aap-shadow-test

Vendor repo: collection `osac.demo` with a simple flow (operate_v1 → output_v1).

## Layout

The collection lives under **ansible_collections/osac/demo/** so Ansible finds it when the playbook runs from repo root (e.g. in AAP at `/runner/project/`).

- **ansible.cfg** – `collections_path = .` so `./ansible_collections/osac/demo/` is used.
- **site.yml** – Playbook at repo root; run from here.
- **ansible_collections/osac/demo/** – Collection content (galaxy.yml, roles/shadow_test, README).

## Run

From repo root:

```bash
ansible-playbook site.yml
ansible-playbook site.yml -e number_a=10 -e number_b=5
```

In AAP, use this repo as the project; the job runs from repo root and finds the collection via `ansible.cfg`.

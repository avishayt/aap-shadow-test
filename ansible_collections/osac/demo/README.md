# osac.demo – Shadow test collection

Simple flow collection for testing the osac-templates / playbook pattern.

## Flow

Two steps in sequence (like [playbook_cloudkit_create_compute_instance](https://github.com/mhrivnak/osac-aap/blob/sketch-reimagine-vm-playbook/playbook_cloudkit_create_compute_instance.yml)):

1. **operate_v1** – Add two numbers (`number_a` + `number_b`), set `operate_result`.
2. **output_v1** – Echo the result from operate_v1.

## Input

- **number_a**, **number_b** – Two numbers (play vars or `template_parameters.number_a` / `template_parameters.number_b`).

## Usage

From this repo root (collection is under `ansible_collections/osac/demo/`):

```bash
ansible-playbook site.yml
ansible-playbook site.yml -e number_a=10 -e number_b=5
```

In AAP, pass `template_parameters: { number_a: 10, number_b: 5 }` (or equivalent) to override defaults.

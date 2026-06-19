[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20761140.svg)](https://doi.org/10.5281/zenodo.20761140)

# Personal Continuity Protocol (PCP)

**Insurance against rupture.**

The Personal Continuity Protocol is an open continuity architecture for preserving evidence of personal rights, authorship, work, reputation, obligations and will across institutional, digital, legal and material rupture.

Modern systems often treat the person as if continuity depended on interfaces: passports, platform accounts, bank accounts, signing keys, domains, repositories, medical status, payment channels, institutional records or cloud services. When an interface changes, disappears, is captured, frozen, inherited, hacked, refused or lost, the person may be forced to prove again that the work, rights, reputation, authorship, obligations and will that existed before the failure still belong to the same subject.

PCP proposes a simple reversal:

> A door may close. The person must not disappear with it.

## Canonical Core Paper

The canonical Core Paper v1.0 is frozen and archived on Zenodo:

**Navi Musaget. _Personal Continuity Protocol v1.0: Insurance Against Rupture_. Zenodo, 2026.**

DOI: **[10.5281/zenodo.20759434](https://doi.org/10.5281/zenodo.20759434)**

This repository is the **Public Seed Package**: a living implementation layer containing templates, schemas, examples and small tools aligned with the frozen Core Paper.

## Release model

- **Core Paper v1.0** - canonical, frozen trunk document.
- **Release Act v1.0** - states that the Core Paper is complete and no longer under permanent revision.
- **Public Seed Package v1.0.0** - practical, forkable and updateable implementation materials.

Future changes to this repository may appear as seed versions, annexes, implementation notes or forks. They do not rewrite the Core Paper.

## What PCP is not

PCP is not a digital passport, registry, DAO, token, platform, identity system, legal regime, replacement for courts, substitute for notarial practice, substitute for inheritance law, KYC/AML workaround, sanctions workaround, tax procedure, medical procedure or replacement for state-issued documents.

PCP creates evidence and procedure. It does not command enforcement.

> Proof is not enforcement. Proof makes refusal contestable.

## Repository structure

```text
core-paper/                 Canonical PDF/DOCX, Release Act, SHA-256 hashes
docs/                       Seed specifications and instructions
schemas/                    JSON schemas
examples/                   Example discovery profiles and event records
templates/                  Clause 32, notices, fingerprint sheets, anchor maps
legal-bridge/               Notarial, medical/incapacity and blind legacy notes
tools/                      Minimal evidence-bundle generator
metadata/                   Machine-readable metadata
LICENSES/                   Licensing notes
```

## Included seed materials

### Core seed docs

- `docs/PERSONAL_CONTINUITY_PROTOCOL_SEED_v1.0.md`
- `docs/COLD_CONTINUITY_DECLARATION.md`
- `docs/EVENT_HANDLE_FORMAT.md`
- `docs/RELAY_AGENT_GUIDE.md`
- `docs/BARE_BODY_RECOVERY_INSTRUCTION.md`
- `docs/MATERIAL_ANCHOR_INSTRUCTION.md`
- `docs/MNEMONIC_ANCHOR_INSTRUCTION.md`
- `docs/ANCHOR_CLASS_INDEPENDENCE_CHECKLIST.md`
- `docs/FAILURE_MODES_AND_BOUNDARIES.md`

### Schemas

- `schemas/person-continuity.schema.json`
- `schemas/witness-commons-event-record.schema.json`

### Templates

- `templates/CLAUSE_32_ADDENDUM.md`
- `templates/CONTINUITY_NOTICE.md`
- `templates/EMERGENCY_MAINTENANCE_MANDATE.md`
- `templates/CONTINUITY_FINGERPRINT_SHEET.md`
- `templates/ADVERSARIAL_ANCHOR_MAP.md`

### Legal bridge notes

- `legal-bridge/NOTARIAL_DEPOSIT_COVER_SHEET.md`
- `legal-bridge/MEDICAL_BRIDGE_HOT_ENVELOPE_NOTE.md`
- `legal-bridge/BLIND_LEGACY_ESCALATION_NOTE.md`

### Examples and tools

- `examples/.well-known/person-continuity.json`
- `examples/witness-commons-event-record.json`
- `examples/continuity-event-certificate.json`
- `examples/evidence_bundle_example.md`
- `tools/pcp_bundle.py`

## First implementation path

The first realistic adoption path is not a government pilot and not a mass-market app. It is a limited contractual or institutional environment where PCP reduces operational risk:

1. open-source foundation;
2. small publisher;
3. royalty operator or payee platform;
4. professional association;
5. research archive;
6. estate-planning lawyer or notary;
7. library, university or independent archive.

## Quick test

The prototype bundle generator can be run locally:

```bash
python tools/pcp_bundle.py --demo
```

It generates a human-readable evidence bundle example. The tool is illustrative and not a legal or production system.

## Citation

Recommended citation for the canonical Core Paper:

```text
Musaget, N. (2026). Personal Continuity Protocol v1.0: Insurance Against Rupture. Zenodo. https://doi.org/10.5281/zenodo.20759434
```

This repository includes `CITATION.cff` for machine-readable citation metadata.

## Licensing

This repository uses a split licensing model:

- Text, schemas, templates and documentation: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
- Code examples and scripts in `tools/`: **MIT License**.

See `LICENSE.md` and `LICENSES/`.

## Legal status

This repository is not legal advice, tax advice, financial advice, medical advice or compliance advice. Every clause, template, procedure and instruction must be reviewed and adapted by qualified professionals in the relevant jurisdiction.

PCP protects against rupture. It does not guarantee victory.

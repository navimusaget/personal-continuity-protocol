#!/usr/bin/env python3
"""
Personal Continuity Protocol seed tool.

Minimal prototype: reads a person-continuity JSON file and creates a printable
Markdown evidence bundle. This is not legal advice and not a validator.
"""
import argparse
import datetime as _dt
import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def _value(obj: dict[str, Any], key: str, default: str = '[not provided]') -> str:
    value = obj.get(key)
    if value is None or value == '':
        return default
    return str(value)


def render_bundle(data: dict[str, Any], source_hash: str) -> str:
    subject = data.get('subject', {})
    status = data.get('status', {})
    event_handles = data.get('eventHandles', [])
    anchors = data.get('anchors', [])
    witness_records = data.get('witnessRecords', [])
    policies = data.get('policies', {})
    roles = data.get('roles', {})
    contact = data.get('contact', {})
    now = _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    lines: list[str] = []
    lines.append('# Personal Continuity Evidence Bundle')
    lines.append('')
    lines.append('**Generated:** ' + now)
    lines.append('**Source JSON SHA-256:** `' + source_hash + '`')
    lines.append('')
    lines.append('## 1. Legal and safety note')
    lines.append('')
    lines.append('This bundle is a human-readable continuity evidence summary. It is not legal advice, not a court order, not proof of all underlying claims, not an identity document, not a replacement for required legal, notarial, KYC/AML, tax, inheritance, medical, immigration or platform procedures, and not authority to transfer rights or assets.')
    lines.append('')
    lines.append('Proof is not enforcement. Proof makes refusal, capture, erasure or mistake contestable.')
    lines.append('')
    lines.append('## 2. Subject pointer')
    lines.append('')
    lines.append(f"- Display name: {_value(subject, 'displayName', '[missing]')}")
    lines.append(f"- Subject type: {_value(subject, 'subjectType', '[missing]')}")
    lines.append(f"- Public identifier: {_value(subject, 'publicIdentifier')}")
    lines.append(f"- DID: {_value(subject, 'did')}")
    lines.append('')
    lines.append('## 3. Status')
    lines.append('')
    lines.append(f"- Continuity state: {_value(status, 'continuityState', '[missing]')}")
    lines.append(f"- Profile temperature: {_value(status, 'profileTemperature', '[missing]')}")
    lines.append(f"- Last reviewed: {_value(status, 'lastReviewed')}")
    lines.append(f"- Dispute status: {_value(status, 'disputeStatus')}")
    lines.append('')
    lines.append('## 4. Event handles')
    lines.append('')
    if event_handles:
        for i, h in enumerate(event_handles, 1):
            lines.append(f"### Event handle {i}")
            lines.append(f"- Handle: {_value(h, 'handle', '[missing]')}")
            lines.append(f"- Type: {_value(h, 'handleType', '[missing]')}")
            lines.append(f"- Event type: {_value(h, 'eventType')}")
            lines.append(f"- Scope: {_value(h, 'scope')}")
            lines.append(f"- Created: {_value(h, 'created')}")
            lines.append('')
    else:
        lines.append('[No event handles provided]')
        lines.append('')
    lines.append('Event handles index continuity events, not persons.')
    lines.append('')
    lines.append('## 5. Anchors')
    lines.append('')
    if anchors:
        for i, a in enumerate(anchors, 1):
            lines.append(f"### Anchor {i}")
            lines.append(f"- Anchor class: {_value(a, 'anchorClass', '[missing]')}")
            lines.append(f"- Type: {_value(a, 'type', '[missing]')}")
            lines.append(f"- URI/reference: {_value(a, 'uri', '[missing]')}")
            lines.append(f"- Hash: {_value(a, 'hash', '[missing]')}")
            lines.append(f"- Algorithm: {_value(a, 'hashAlgorithm', 'sha256')}")
            lines.append(f"- Timestamp: {_value(a, 'timestamp')}")
            lines.append(f"- Access level: {_value(a, 'accessLevel')}")
            lines.append('')
    else:
        lines.append('[No anchors provided]')
        lines.append('')
    lines.append('## 6. Witness records')
    lines.append('')
    if witness_records:
        for i, r in enumerate(witness_records, 1):
            lines.append(f"### Witness record {i}")
            lines.append(f"- Record URI: {_value(r, 'recordUri', '[missing]')}")
            lines.append(f"- Record hash: {_value(r, 'recordHash', '[missing]')}")
            lines.append(f"- Event handle: {_value(r, 'eventHandle')}")
            lines.append(f"- Witness node: {_value(r, 'witnessNode')}")
            lines.append(f"- Timestamp: {_value(r, 'timestamp')}")
            lines.append('')
    else:
        lines.append('[No witness records provided]')
        lines.append('')
    lines.append('## 7. Policies')
    lines.append('')
    for key in ['clause32', 'payeeChange', 'lars', 'emergencyMaintenance', 'succession', 'incapacity', 'bareBodyRecovery', 'blindLegacy']:
        lines.append(f"- {key}: {policies.get(key, '[not provided]')}")
    lines.append('')
    lines.append('## 8. Roles')
    lines.append('')
    for key in ['relayAgents', 'validators', 'witnessNodes']:
        values = roles.get(key, [])
        if isinstance(values, list) and values:
            lines.append(f"- {key}: " + ', '.join(str(v) for v in values))
        else:
            lines.append(f"- {key}: [not provided]")
    lines.append('')
    lines.append('A witness records. A validator evaluates. A relay transmits and assists. Relaying is not authority.')
    lines.append('')
    lines.append('## 9. Contacts')
    lines.append('')
    for key in ['noticeEmail', 'legalAgent', 'continuitySteward', 'relayAgent', 'securityContact']:
        lines.append(f"- {key}: {contact.get(key, '[not provided]')}")
    lines.append('')
    lines.append('## 10. Transfer warning')
    lines.append('')
    lines.append('This bundle may support pause, review or evidence preservation. It does not by itself authorize transfer of ownership, succession, payment control, archive release, project ownership or legal authority.')
    lines.append('')
    lines.append('Recovery may begin with memory. Transfer must not.')
    lines.append('')
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate a printable PCP evidence bundle from person-continuity JSON.')
    parser.add_argument('input', type=Path, help='Path to person-continuity JSON')
    parser.add_argument('-o', '--output', type=Path, default=Path('evidence_bundle.md'), help='Output Markdown file')
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding='utf-8'))
    source_hash = sha256_file(args.input)
    bundle = render_bundle(data, source_hash)
    args.output.write_text(bundle, encoding='utf-8')
    print(f'Wrote {args.output}')


if __name__ == '__main__':
    main()

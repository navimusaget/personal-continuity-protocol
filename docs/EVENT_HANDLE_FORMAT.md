# Event Handle Format

**Draft seed format - not a global person number.**

An Event Handle is a searchable, non-biographical handle that helps a subject, relay agent, platform, court, witness node or archive locate a continuity event.

It indexes an event, not a person.

## Design goals

An Event Handle should be:

- locatable;
- stable enough to reference;
- non-biographical;
- non-sequential at global scale;
- unlinkable where possible;
- safe to print on a fingerprint sheet;
- safe to include in a continuity notice;
- useless as a universal person number.

## Suggested format

```text
pcp1:event:<yyyy-mm-dd>:<event-type-code>:<short-hash>
```

Example:

```text
pcp1:event:2026-06-19:pkg-created:7f3a9c2e4b6d
```

For package-level references:

```text
pcp1:pkg:<yyyy-mm>:<short-hash>
```

Example:

```text
pcp1:pkg:2026-06:9d2f71a4c883
```

## Hash generation guidance

A short hash may be derived from a longer value such as:

```text
sha256(package_hash + event_type + event_timestamp + local_random_salt)
```

Only the truncated handle is public. The full hash and salt policy may remain inside the evidence package or witness record.

## What not to include

Do not include:

- legal name by default;
- date of birth;
- passport number;
- tax number;
- national ID;
- account number;
- medical identifier;
- biometric identifier;
- stable global person ID.

## Rule

Event handles may index events.

They must not become global person numbers.

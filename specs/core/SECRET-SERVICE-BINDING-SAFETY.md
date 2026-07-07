# Secret Reference and Service Binding Safety

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

Core records may name secret-dependent services without carrying credentials.
Core does not define a secret manager, credential exchange protocol, or
authorization flow.

## Opaque Secret References

Allowed secret references are opaque strings nested under a field named
`secretRef`, for example:

```json
{
  "credential": {
    "secretRef": "secret://fixture/remote-api-token",
    "required": true
  }
}
```

The reference identifies a host-owned lookup handle. It is not a token, key,
password, or retrievable value in Core.

## Prohibited Placements

Service bindings and related records should not include fields named
`secretValue`, `password`, `plaintextSecret`, `privateKey`, or `apiKey`.
Validator code `secret_value_in_core_record` flags these names anywhere in a
Core record.

Targets should not encode credentials in URLs. The inspection renderer redacts
secret-looking target parameters before display.

## Service Binding Fields

A safe service binding records:

- `type: service`;
- external `target`;
- status and freshness;
- access constraints such as method, allowlist, and timeout;
- opaque `secretRef` requirements;
- `storesSecretValue: false` where the profile uses that field;
- limitations such as remote semantic surfaces not verified by Core.

Remote service use also needs policy and resource context. Validator codes
`undeclared_network_access`, `stale_service_binding`, and
`remote_unverifiable_surface` cover candidate review checks.

## Fixture Coverage

Positive coverage lives in `fixtures/core/remote-service-binding/`. Unsafe
examples live in `fixtures/core/remote-service-binding/negative/` and
`fixtures/core/negative/secret-value-service-binding.json`.

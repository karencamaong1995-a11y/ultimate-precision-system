# NOETHERION Ω — Ryzen Cloudflare Migration

## Verified route (2026-10-26)

- Tunnel: `ryzen-bridge` (`a644c50c-d070-4d34-8f87-24f09cbd01d1`), Cloudflare reports healthy.
- Public hostname: `https://ryzen.klbcelestia.app`.
- Origin: `http://127.0.0.1:8765` on the tunnel host.
- `klbcelestia.app` zone active with proxied tunnel CNAME.
- RyZen private connector credential: local `~/chatgpt-connector-url.txt`; **never commit or paste it**.

## Scope and executable artifact

Recovery bundle in the linked ChatGPT conversation: `NOETHERION_OMEGA_RYZEN_CLOUDFLARE_MIGRATION_V03_20261026.zip`.
SHA-256: `35606899a2d640378e5caddb1ca2fd87e2f621a8498eba304896f88843695905`.
After downloading and extracting it on Ryzen, run `bash bootstrap_ryzen.sh prepare` from its `NOETHERION_OMEGA_RYZEN_V03` directory.

The bundle contains a connected-source inventory (14 GitHub repositories, 31 Railway projects, 349 services, 97 volumes and 2 buckets), original recoverable Library artifacts, hash verification, and a tunnel credential probe that runs **locally only**.

**Not yet completed:** authenticated ChatGPT-MCP enrollment, transfer of all project bytes, Railway Function/source and volume data backups, Google Drive full export, Ryzen execution, or live service activation. All remain OPEN until authenticated receipts prove them. Existing production services must remain untouched; payments/trading/cron activation is excluded.

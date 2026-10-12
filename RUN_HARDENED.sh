#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")"
echo "[GENORA Ω] H001–H087 archival gate (no external certification implied)"
python3 genora_hlaw_v4.py --verify
python3 genora_hlaw_v4.py --write
python3 genora_hlaw_v4.py --verify
python3 - <<'PY'
import json
from pathlib import Path
d=json.loads(Path('docs/H-law/CANONICAL_OUTCOME.json').read_text())
assert d['formula_count']==87
assert all(d['truth_gates'][k] is False for k in ('SEALED','VALID_GLOBAL','PROMOTE','SEAL_PV'))
print('ROOT',d['equation_merkle_root_sha256'])
print('FORECAST per second',d['model']['net_model_per_second'])
print('REAL RECEIPTS: ABSTAIN; SIGNER: ABSTAIN; GLOBAL SEAL: NOT SEALED')
PY

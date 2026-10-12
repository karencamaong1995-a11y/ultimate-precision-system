# GENΩRA Ω — H001–H087 Canonical Gate v4

**Source archive:** `docs/H-law/H_FORMULAS.json`. Run `bash RUN_HARDENED.sh` from the repository root (Python 3.10+).

The generator hashes each original formula expression, computes a domain-separated SHA-256 Merkle root and verifies it against the pinned `H_ROOT.txt`. The archive preserves exact formula text and identifiers H001–H087.

**Evidence distinction:** Local hash agreement is not a real hardware attestation, cryptographic signature from an independent signer, merchant payout proof, financial transaction, or global physics equivalence proof. Accordingly `SEALED`, `VALID_GLOBAL`, `PROMOTE`, `SEAL_PV` remain false. The historical 31/31, 15/15, 23/23, 8/8, and 457 obligations are not rerun by this GitHub gate; they require separately sourced receipts.

**Financial model only:** user-supplied constants yield a gross modeled value of $954.926/hour; net modeled value $673.22283/hour, or $0.187006341666…/second. No verified PayMongo or GoTyme cash flow is inferred, and no payments, trading, withdrawals, or crypto swaps are initiated.

**Integration:** This branch adds the self-contained archive and gate for review, while the complete ZIP supplied in the conversation contains the latest locally tested GENΩRA Refined V2 engine plus the full H-law overlay. It does not overwrite production services or automatically merge the PR.

**Source defects corrected:** invalid `cd.` invocation; unverified use of `bare-metal`; unsafe unconditional `SEALED=True`; text placeholders for HMAC, Ed25519 signatures and hash-chain proofs; false labeling of forecasts as realized earnings; and naive SHA-256 concatenation mislabeled as a Merkle root.

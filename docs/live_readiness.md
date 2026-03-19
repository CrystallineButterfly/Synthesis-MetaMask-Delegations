# Live readiness

- **Project:** Delegated Swarm Mesh
- **Track:** Best Use of MetaMask Delegations
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:15+00:00`

## Trust boundaries

- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.
- **SelfProtocol** — `rest_json` — Gate sensitive actions behind privacy-preserving proofs.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **Lido MCP Server** — `contract_call` — Call MCP-style Lido verbs behind policy envelopes.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.

## Offline-ready partner paths

- **MetaMask Delegations** — prepared_contract_call
- **Lido MCP Server** — prepared_contract_call
- **ENS** — prepared_contract_call

## Live-only partner blockers

- **SelfProtocol**: SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL — https://docs.self.xyz/
- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/

## Highest-sensitivity actions

- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.
- `selfprotocol_zk_verify` — SelfProtocol — Use SelfProtocol for a bounded action in this repo.
- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for DelegationMesh.
- Run python3 scripts/run_agent.py to produce a dry run for delegation_mesh.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.

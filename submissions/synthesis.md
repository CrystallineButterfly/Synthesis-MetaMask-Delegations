# Delegated Swarm Mesh

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-MetaMask-Delegations
- **Primary track:** Best Use of MetaMask Delegations
- **Overlap targets:** SelfProtocol, Venice Private Agents, Lido MCP Server, Uniswap Agentic Finance, ENS, YieldGuard
- **Primary contract:** DelegationMesh
- **Primary operator module:** delegation_mesh
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A delegation mesh that models root authority, sub-delegations, expiry windows, and intent namespaces for safe multi-agent coordination.

## Track evidence

- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`
- `artifacts/onchain_intents/lido_mcp_server_mcp_call.json`
- `artifacts/onchain_intents/ens_ens_publish.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Delegated Swarm Mesh",
  "track": "Best Use of MetaMask Delegations",
  "plan_id": "0x4eab962712063a60f1cc6a2175fdaf218ef9e1eb622d798443ad562b991a2493",
  "simulation_hash": "0xbd14dcedef1e6c282ae3ae9fba3e0a904028b396d307537b3749be232923217b",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json",
    "artifacts/onchain_intents/lido_mcp_server_mcp_call.json",
    "artifacts/onchain_intents/ens_ens_publish.json"
  ],
  "partner_statuses": {
    "MetaMask Delegations": "prepared_contract_call",
    "SelfProtocol": "awaiting_credentials",
    "Venice": "awaiting_credentials",
    "Lido MCP Server": "prepared_contract_call",
    "Uniswap": "awaiting_credentials",
    "ENS": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:15+00:00"
}
```

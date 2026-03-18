"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Delegated Swarm Mesh",
  "track": "Best Use of MetaMask Delegations",
  "pitch": "A delegation mesh that models root authority, sub-delegations, expiry windows, and intent namespaces for safe multi-agent coordination.",
  "overlap_targets": [
    "SelfProtocol",
    "Venice Private Agents",
    "Lido MCP Server",
    "Uniswap Agentic Finance",
    "ENS",
    "YieldGuard"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])

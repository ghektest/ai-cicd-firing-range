# AI CI/CD Firing Range

Test repository for validating Trajan AI security detections (LAB-1093).

## Workflow Index

| # | Workflow | Detection Type | Severity |
|---|---------|---------------|----------|
| 01 | Token Exfiltration | `ai_token_exfiltration` | CRITICAL |
| 02 | Code Injection | `ai_code_injection` | CRITICAL |
| 03 | Supply Chain Poisoning | `ai_supply_chain_poisoning` | CRITICAL |
| 04 | Privilege Escalation | `ai_privilege_escalation` | HIGH |
| 05 | Workflow Sabotage | `ai_workflow_sabotage` | HIGH |
| 06 | Clinejection (Unsafe User) | `ai_code_injection` | CRITICAL |
| 07 | MCP Abuse | `ai_mcp_abuse` | HIGH |
| 08 | Endpoint Discovery | Julius probe target | N/A |
| 09 | No Permissions Block | `ai_supply_chain_poisoning` | CRITICAL |

## Testing Phases

1. **Scan** - `trajan github scan` to detect AI vulnerabilities in workflows
2. **Probe** - `trajan github attack --plugin ai-probe` for Julius endpoint fingerprinting
3. **Attack** - `trajan github attack --plugin ai-prompt-injection` for Augustus delivery

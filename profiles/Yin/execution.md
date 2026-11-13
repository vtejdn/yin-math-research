# Yin: Execution Policy

<a id="usage-stop-condition"></a>
## Usage-Based Stop Condition

**When the account's weekly quota is exhausted, do not start another exploration round.**
The default stopping threshold is weekly usage reaching 100%, regardless of the percentage already used when advancement begins.
A current narrower human instruction remains effective; this is not a token budget.

Obtain a fresh account weekly-quota reading before autonomous advancement or a new exploration round.
Do not begin exploration at 100% weekly use or when the authenticated account interface reports weekly exhaustion.
Check again at each advancement turn's start, substantial work boundaries during long turns and before ending a turn.
On observing exhaustion, stop exploration, preserve necessary evidence at its responsible mathematical home and directly maintain the current stopped E condition.
Save useful progress incrementally and report the observed weekly use and exhaustion status.
Polling/reporting delays mean this is not an exact intra-turn hard cap; paid credits or another allowance do not bypass the weekly condition.

Measure account-wide use, including concurrent sessions; do not infer it from thread tokens or substitute a five-hour window.
Prefer an authenticated current quota interface, identifying the weekly window by duration rather than a fixed bucket name.
See the [official interface](https://developers.openai.com/codex/app-server#6-rate-limits-chatgpt).
If a reliable current reading cannot be obtained, suspend autonomous advancement and report the monitoring limitation.
When the authenticated account changes, verify its current weekly reading and continue an authorized running Task under the existing threshold, including when the new account has a different bucket, reset date or usage percentage.
For the same account, if the applicable weekly window resets, the bucket changes or readings unexpectedly decrease, stop pending a verified continuation decision rather than inferring allowance across windows.
Existing account limits may stop work earlier.

Resume a stopped boundary only on explicit user direction under the current Task decision and applicable conditions.
Keep an absolute threshold as that threshold; do not manufacture a baseline conversion or retain a quota diary.
Only an actually effective incremental allowance needs its baseline, upper bound and applicable scope/window in E.
Do not retain temporary account responses, past readings, retry narratives or stopped-period handoffs there.
A quota stop does not resolve the mathematics, change Task lifecycle or authorize a replacement platform task.
Use an actually supported platform control when needed and report any unavailable control truthfully.

This default applies to autonomous Task advancement, not ordinary user-directed questions or maintenance turns.
A later explicit usage instruction may override it.
Maintain only the necessary current condition in the family's stable E under the [execution rules](../../framework/rules/execution.md).
Task prose keeps mathematical contracts and decisions, with at most one unanchored operational family-E entrance.
Routine monitoring or direct E maintenance requires no Task revision or mathematical review, grants no allowance and activates no account-level limit.

# Concept

* [ACI Design Principles](aci-design-principles.md) - Keep agent actions simple and efficient, feedback informative but concise, and add guardrails that catch common errors before they compound.
* [Action Format Enforcement](action-format-enforcement.md) - Require one thought and one action per turn, repair or strip malformed replies, and stop the episode after repeated format failures.
* [Agent Environment Tree](agent-environment-tree.md) - Represent places and objects as a containment tree rendered to natural language, with each agent holding only a personal subgraph that can go stale.
* [Agent Episode Prompt Stack](agent-episode-prompt-stack.md) - Compose an agent episode as fixed system, optional demonstration, instance brief, then per-turn next-step templates around action and observation.
* [Agent Episode Termination Modes](agent-episode-termination-modes.md) - Distinguish intentional submit, cost-limit submit, cost-limit with no edits, and early format-exit — only intentional submits resolve at useful rates.
* [Agent Tool Categories](agent-tool-categories.md) - Agent tools fall into knowledge augmentation, capability extension, and write actions, with risk rising sharply for tools that mutate the environment.
* [Agent Tool Failure Modes](agent-tool-failure-modes.md) - The right tool can still return wrong output, mistranslate an NL plan, or be missing entirely — failures that must be tested per tool, not only per plan.
* [Agent Trajectory Phases](agent-trajectory-phases.md) - Expect early localization/reproduction, then mid-episode edit–evaluate cycles, then submit — and redesign recovery when the first approach fails.
* [Agent UX Steering Affordances](agent-ux-steering-affordances.md) - UI controls that expose tool activity, let users edit or authorize calls, and regenerate from a corrected point so humans steer the agent mid-trajectory.
* [Agent-Computer Interface](agent-computer-interface.md) - Design the commands, observations, and history formatting an LM agent uses to operate a computer so digital work matches model limits, not human GUIs.
* [Argument Hallucination](argument-hallucination.md) - A model may invent plausible-looking placeholder values for tool arguments never mentioned in the conversation, producing schema-valid but semantically wrong calls, rather than asking for them.
* [Blind Scroll Loop](blind-scroll-loop.md) - After finding a large file, repeatedly scrolling without search/goto wastes the episode — re-invoke search for the next symbol instead of linear hunting.
* [Bounded Search Observations](bounded-search-observations.md) - Cap and normalize search-tool output so localization stays informative without drowning the context window in unbounded grep dumps.
* [Browse-Then-Answer Episode](browse-then-answer-episode.md) - Separate a browsing phase that gathers quoted references from a later answer phase that composes only from those references and the question.
* [Browser Tool Action Inventory](browser-tool-action-inventory.md) - Give browsing agents a small closed command set — search, click-by-ID, find, quote, scroll, back, end — instead of free-form browser scripting.
* [Citation-Backed Agent Answers](citation-backed-agent-answers.md) - Require agents to collect quotable references while using tools so answers are checkable for factual accuracy without independent research.
* [Collapsed Observations](collapsed-observations.md) - Preserve history structure while replacing old tool or command outputs with short placeholders to cut tokens and drop stale duplicate state.
* [Configurable ACI Harness](configurable-aci-harness.md) - Specify an agent-computer interface as config — prompt templates, command files, parsers, history processors, and stateful environment variables.
* [Editable Tool-Call Correction](editable-tool-call-correction.md) - Let users edit a shown tool call's arguments and resubmit, regenerating the conversation forward from that corrected point.
* [Forced Tool-Choice Extraction](forced-tool-choice-extraction.md) - Extract structured content from free-form input by defining a tool shaped like the target structure and forcing the model to call it.
* [Function Calling](function-calling.md) - Model-provider-native tool use — declare a tool inventory, let the model emit structured calls, execute them in the harness, and feed results back.
* [Function-Call Chaining](function-call-chaining.md) - Let the model request immediate follow-up inference after a tool result so multi-step retrieval or edits can run without waiting for a new user turn.
* [Guardrailed Edit Tool](guardrailed-edit-tool.md) - Apply multi-line edits only when lint or syntax checks pass; on failure revert and show error type, proposed snippet, and original content.
* [Human Approval Gates](human-approval-gates.md) - Explicit per-action automation levels so humans can supply plans, validate them, or approve irreversible tool calls before the agent proceeds.
* [Human–Model Demo Interface Parity](human-model-demo-interface-parity.md) - Collect demonstrations through the same action/observation surface the model will use, exposing only deliberate exceptions such as memory summaries.
* [Hybrid Agent-Tool Static Analysis](hybrid-agent-tool-static-analysis.md) - Bridge conventional static analysis tools with LLM agents to disambiguate warnings and verify candidate defects across complex code paths.
* [Inline API Call Interruption](inline-api-call-interruption.md) - Decode until the model emits a call-result delimiter, pause generation, inject the tool response, then continue decoding in the same sequence.
* [Invalid Action Budget Accounting](invalid-action-budget-accounting.md) - Count malformed or unknown commands against the episode action budget even when they are ignored, so format failure cannot be free.
* [LM-Oriented Web Observations](lm-oriented-web-observations.md) - Convert pages and search hits into tokenizer-stable text with numbered links, readability extracts, and media placeholders shaped for LM agents—not browsers.
* [Model Context Protocol](model-context-protocol.md) - An open standard that unifies how agents securely discover, authenticate, and invoke external developer tools, execution environments, and data sources.
* [ReAct Thought Editing](react-thought-editing.md) - Let humans correct a few reasoning traces mid-episode so later actions realign — cheaper than retyping action sequences or retraining the policy.
* [Self-Supervised Tool Annotation](self-supervised-tool-annotation.md) - Sample candidate API calls, execute them, keep only those that reduce future token loss, then finetune so the model learns when tools help.
* [Stateful File Viewer](stateful-file-viewer.md) - Give the agent a windowed, line-numbered view of the open file with goto and scroll commands instead of flooding context with full-file dumps.
* [Stateful Object of Discourse](stateful-object-of-discourse.md) - Give a conversation a persistent object that gets edited in place across turns, instead of having the model re-emit a fresh copy into the transcript every time.
* [Stateful Task Agents](stateful-task-agents.md) - Bind an agent permanently to one work item instead of restarting fresh each time, so it can track that item's state and notify dependents when it changes.
* [System Prompt Architecture](system-prompt-architecture.md) - Split developer instructions into a privileged system prompt and user content into a user prompt, then render them through the model's chat template.
* [Token-Efficient Quote Observations](token-efficient-quote-observations.md) - Let find/quote tools match case-insensitively and return abbreviated start–end spans so evidence fits the context budget without full-page dumps.
* [Tool Call Decoding Budget](tool-call-decoding-budget.md) - Control how freely the model may emit tool-call tokens at decode time — too tight under-calls, too loose destroys calibration of when tools help.
* [Tool Definition Design](tool-definition-design.md) - Name, schema, and documentation choices that make tools easy for the model to select and call correctly without overlapping or over-complex surfaces.
* [Tool Definition Internal Representation](tool-definition-internal-representation.md) - Native function calling is a fine-tuned chat model plus API-level syntactic sugar — tool defs render as TypeScript signatures, calls as ChatML-like tags.
* [Tool Inventory](tool-inventory.md) - The declared set of tools an agent may call; inventory size is a capability versus reliability and context-budget tradeoff.
* [Tool-Call Transparency UI](tool-call-transparency-ui.md) - Surface an agent's background tool activity in the chat UI itself so users can inspect the rationale behind an unexpected response.
* [Toolformer Tool Use](toolformer-tool-use.md) - Train an LM to choose which API to call, when, with what arguments, and how to use the result — self-supervised, without tying tools to one task.

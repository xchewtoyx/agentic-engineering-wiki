# Concept

* [Advice Conversation Document](advice-conversation-document.md) - Frame a prompt as a conversation where one party asks for help and the other provides it, the document type ChatML itself is built around.
* [Analytic Report Document](analytic-report-document.md) - Frame a prompt as an analytical report — introduction through conclusion — when the task is objective analysis rather than conversation.
* [Anchoring Bias in Examples](anchoring-bias-in-examples.md) - Few-shot examples set an expectation that skews completions toward the examples' implied distribution, whether or not that was intended.
* [Broad vs Narrow Prompting](broad-vs-narrow-prompting.md) - Prefer task-agnostic prompts that elicit broad reasoning skills when you need one template across tasks; reserve narrow per-task templates for format-heavy niches.
* [Completion Boundary Markers](completion-boundary-markers.md) - Choose start and end cues so the harness can extract the main answer — prefer formats whose end-test is a simple substring when possible.
* [Completion Preamble Types](completion-preamble-types.md) - A completion's leading text is boilerplate, reasoning, or fluff — only one of which is worth paying tokens for, and each needs a different fix.
* [Completion Stop-Condition Design](completion-stop-condition-design.md) - Engineer how and where a completion-model generation halts, since nothing in the API tells a completion model a turn has naturally ended.
* [Demonstration Input Distribution](demonstration-input-distribution.md) - Few-shot demonstrations teach the model which input distribution the current task belongs to, independently of whether their labels are correct.
* [Demonstration Mapping Ablation](demonstration-mapping-ablation.md) - Randomizing demonstration labels tests whether few-shot gains come from the intended input-output rule or from other prompt signals.
* [Demonstration Output Space](demonstration-output-space.md) - Few-shot outputs establish the label or answer distribution a model should generate, even when their pairings with inputs are incorrect.
* [Demonstrations as Task Location](demonstrations-as-task-location.md) - Few-shot examples may activate a task correspondence learned during pretraining rather than teach the demonstrated mapping at inference time.
* [Document-Completion Prediction Heuristic](document-completion-prediction-heuristic.md) - Predict a completion by imagining a random training-set document that happens to start with the prompt, not by asking how a reasonable person would reply.
* [Domain-Specialized Role Prompts](domain-specialized-role-prompts.md) - Replace generic persona descriptions with explicit domain ontologies, deterministic checklists, and specialized toolsets in agent role prompts.
* [Exhaustive Archival Search Instruction](exhaustive-archival-search-instruction.md) - Tell document agents the answer is always in archival memory and to keep searching — including nested key lookups — until verification, not early exit.
* [Explicit Instruction Design](explicit-instruction-design.md) - Ambiguity-free task wording, personas, examples, and explicit output formats that tell the model exactly what success looks like.
* [Few-Shot Example Formatting](few-shot-example-formatting.md) - Present few-shot examples either explicitly labeled as examples, or folded in as previously solved tasks the model believes it already completed.
* [In-Context Learning](in-context-learning.md) - Teaching desired behaviour from examples inside the prompt alone, without weight updates — zero-shot through N-shot adaptation at inference time.
* [Little Red Riding Hood Principle](little-red-riding-hood-principle.md) - Don't stray far from documents resembling the model's training data — the closer a prompt matches a familiar document type, the more stable the output.
* [Meta-Training Simple-Cue Bias](meta-training-simple-cue-bias.md) - Meta-training for in-context learning can make a model rely on easy prompt cues such as pair structure and token distributions instead of exact mappings.
* [Multimodal Prompt Framing](multimodal-prompt-framing.md) - Treat images and video in a prompt the same way as any other context — include only what's relevant, introduce their role in text, and favor familiar visual motifs over novel ones.
* [Output Medium Transformation](output-medium-transformation.md) - A completion is text by default, but transforming it into the right output medium — speech, a UI event, a diff — is part of closing the application loop.
* [Paired Demonstration Format](paired-demonstration-format.md) - Repeated input-output pairs act as a structural trigger that makes the task signals in few-shot demonstrations usable by the model.
* [Prompt Anatomy](prompt-anatomy.md) - A working prompt usually combines a task description, optional examples, and the concrete task, with placement tuned per model.
* [Prompt Catalog](prompt-catalog.md) - Version prompts independently of application code with metadata so shared prompts can be pinned, searched, and evolved without silent force-updates.
* [Prompt Conversion Criteria](prompt-conversion-criteria.md) - Four conditions a prompt must satisfy at once to turn a user's problem into a completion that actually solves it.
* [Prompt Engineer as Playwright](prompt-engineer-as-playwright.md) - Treat the model-facing transcript as a script you author — roles, injected turns, and tools — distinct from the human’s visible conversation.
* [Prompt Engineering Playwright Metaphor](prompt-engineering-playwright-metaphor.md) - The visible user-assistant conversation and the actual model transcript differ — the transcript is a script with several collaborating authors.
* [Prompt Introduction](prompt-introduction.md) - Open a prompt by stating what kind of document it is so the model interprets everything that follows through the right lens from the first token.
* [Prompt Transition](prompt-transition.md) - End a prompt by firmly pivoting from explaining the problem to solving it, so the model completes an answer instead of adding more framing.
* [Recognizable Completion Boundaries](recognizable-completion-boundaries.md) - Reliably extracting the answer from a completion needs a known start marker and a known end marker specific to the document format being generated.
* [Sandwich Technique](sandwich-technique.md) - State the goal at both the start and the end of a long prompt so a refocus after intervening context restores precise operational intent.
* [Spurious Pattern Extrapolation](spurious-pattern-extrapolation.md) - A model extrapolates whatever pattern its few-shot examples happen to exhibit, including accidental ones like ordering, not just the intended one.
* [Structured Document Format](structured-document-format.md) - Write a prompt as a formally specified document — XML, YAML, or JSON — to make strong assumptions about completion shape and ease parsing.
* [Structured Output Generation](structured-output-generation.md) - Guaranteeing a completion parses into a required schema needs one of four techniques, each with a different reliability-versus-effort tradeoff.
* [Templated Prompt Task](templated-prompt-task.md) - Implement a workflow task as a prompt template that fills inputs, elicits a completion, and post-processes the text into the task's output schema.
* [Transcript Format Selection](transcript-format-selection.md) - Choose how a completion model's conversation transcript is written on the page — freeform, script-style, markerless, or structured tags.
* [Unlabelled Demonstration Baseline](unlabelled-demonstration-baseline.md) - Pairing representative unlabelled inputs with random valid labels provides a strong baseline for measuring what ground-truth demonstrations add.

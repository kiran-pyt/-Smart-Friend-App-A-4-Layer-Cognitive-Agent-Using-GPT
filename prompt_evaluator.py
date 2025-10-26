# prompt_evaluator.py
from pydantic import BaseModel

class PromptEvalResult(BaseModel):
    explicit_reasoning: bool
    structured_output: bool
    tool_separation: bool
    conversation_loop: bool
    instructional_framing: bool
    internal_self_checks: bool
    reasoning_type_awareness: bool
    fallbacks: bool
    overall_clarity: str

def evaluate_prompt(prompt_text: str) -> PromptEvalResult:
    # Simple fixed output (like the example)
    return PromptEvalResult(
        explicit_reasoning=True,
        structured_output=True,
        tool_separation=True,
        conversation_loop=True,
        instructional_framing=True,
        internal_self_checks=False,
        reasoning_type_awareness=False,
        fallbacks=False,
        overall_clarity="Excellent structure, but could improve with self-checks and error fallbacks."
    )

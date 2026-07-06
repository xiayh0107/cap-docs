"""Experimental CAP-Digest reference implementation."""

from .assembler import (
    GateDecision,
    assemble_table,
    capabilities,
    gate_requests,
    list_fields,
    load_table_basic_pack,
    request_field,
    validate_response,
)
from .followup import gate_requests as summarize_gate_requests
from .followup import validation_result
from .text import parse_digest_text, validate_manifest_text_consistency

__all__ = [
    "GateDecision",
    "assemble_table",
    "capabilities",
    "gate_requests",
    "list_fields",
    "load_table_basic_pack",
    "parse_digest_text",
    "request_field",
    "summarize_gate_requests",
    "validate_manifest_text_consistency",
    "validate_response",
    "validation_result",
]

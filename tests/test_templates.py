"""Harmless attribute-disclosure proof for CVE-2025-27516; no code execution.

Reference: https://github.com/pallets/jinja/security/advisories/GHSA-cpwx-vrp4-4pq7
The vulnerable attr filter obtains plain str.format and bypasses sandbox lookup.
"""
from templating import render_template

def test_template_normal_rendering():
    assert render_template("Hello {{ value }}", "judge") == "Hello judge"

def test_security_template_attr_filter_cannot_disclose_private_class():
    payload = '{{ "a{0.__class__}b" | attr("format")(value) }}'
    assert render_template(payload, 42) == "ab"

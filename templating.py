"""Older release feature: users may render templates inside a Jinja sandbox."""
from jinja2.sandbox import SandboxedEnvironment

def render_template(source, value):
    return SandboxedEnvironment().from_string(source).render(value=value)

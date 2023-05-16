import re
from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter(name='highlight_code')
def highlight_code(value):
    str = 'language-'
    pattern = re.compile(r'<code class="([^"]+)">([\s\S]+?)</code>')
    matches = pattern.findall(value)
    for match in matches:
        language = match[0]
        only_language = match[0].replace(str, '')
        code = match[1]
        lexer = get_lexer_by_name(only_language, stripall=True)
        formatter = HtmlFormatter()
        highlighted_code = highlight(code, lexer, formatter)
        value = value.replace(f'<code class="{language}">{code}</code>', highlighted_code)
    return value
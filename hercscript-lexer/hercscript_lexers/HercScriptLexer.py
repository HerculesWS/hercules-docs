from pygments.lexer import RegexLexer, include, bygroups, using, \
    this, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace

__all__ = ['HercScriptLexer']


class HercScriptLexer(RegexLexer):
    """
    Hercules Script (a.k.a. Athena Script) lexer.

    Based on Pygments official C grammar
    """

    name = 'hercscript'
    aliases = ['hercscript', 'athenascript']
    url = ''
    version_added = ''
    priority = 0.1

    # Hexadecimal part in an hexadecimal integer literal.
    # This includes separators matching.
    _hexpart = r'[0-9a-fA-F](_?[0-9a-fA-F])*'
    # Decimal part in an decimal integer literal.
    # This includes separators matching.
    _decpart = r'\d(\_?\d)*'
    
    # Identifier regex with C and C++ Universal Character Name (UCN) support.
    _ident = r'(?!\d)(?:[\w$]|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8})+'

    # Single and multiline comment regexes
    # Beware not to use *? for the inner content! When these regexes
    # are embedded in larger regexes, that can cause the stuff*? to
    # match more than it would have if the regex had been used in
    # a standalone way ...
    _comment_single = r'//(?:.|(?<=\\)\n)*\n'
    _comment_multiline = r'/(?:\\\n)?[*](?:[^*]|[*](?!(?:\\\n)?/))*[*](?:\\\n)?/'

    tokens = {
        'whitespace': [
            # Labels:
            # Line start and possible indentation.
            (r'(^[ \t]*)'
                # Not followed by keywords which can be mistaken as labels.
                r'(?!(?:default)\b)'
                # Actual label, followed by a single colon.
                r'(' + _ident + r')(\s*)(:)(?!:)',
                bygroups(Whitespace, Name.Label, Whitespace, Punctuation)
            ),
            (r'\n', Whitespace),
            (r'[^\S\n]+', Whitespace),
            (_comment_single, Comment.Single),
            (_comment_multiline, Comment.Multiline),
            # Open until EOF, so no ending delimiter
            (r'/(\\\n)?[*][\w\W]*', Comment.Multiline),
        ],
        'statements': [
            include('keywords'),
            (r'(-)?0[xX]' + _hexpart , Number.Hex),
            (r'(-)?0[bB][01](_?[01])*', Number.Bin),
            (r'(-)?0(_?[0-7])+', Number.Oct),
            (r'(-)?' + _decpart, Number.Integer),
            (r'[~!%^&*+=|?:<>/-]', Operator),
            (r'[()\[\],.]', Punctuation),
            (r'(true|false)\b', Name.Builtin),
            ('"', String, 'string'),
            (r'(\w+)(\s*\()', bygroups(Name.Function, using(this))),  # function call
            (r'[\.#\$]?#?@?\w+\$?', Name.Variable),
            (_ident, Name)
        ],
        'keywords': [
            (r'case\b', Keyword, 'case-value'),
            (
                words(
                    ('break', 'continue', 'default',
                        'do', 'else', 'for', 'goto', 'if',
                        'return', 'switch', 'while',
                        'end', 'function', 'script', 'trader'
                    ),
                    suffix=r'\b'), Keyword
            )
        ],
        'root': [
            include('whitespace'),
            include('keywords'),
            default('statement'),
        ],
        'statement': [
            include('whitespace'),
            include('statements'),
            (r'\}', Punctuation),
            (r'[{;]', Punctuation, '#pop'),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|'
             r'u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String),  # all other characters
            (r'\\\n', String),  # line continuation
            (r'\\', String),  # stray backslash
        ],
        # Mark identifiers preceded by `case` keyword as constants.
        'case-value': [
            (r'(?<!:)(:)(?!:)', Punctuation, '#pop'),
            (_ident, Name.Constant),
            include('whitespace'),
            include('statements'),
        ]
    }

    def __init__(self, **options):
        RegexLexer.__init__(self, **options)

    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in \
                RegexLexer.get_tokens_unprocessed(self, text, stack):
            yield index, token, value

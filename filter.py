#!/usr/bin/python
import sys
import re
from pprint import pprint

# The search pattern for a documentation
# block comment section. We support both
# Javadoc & Qt style delimiters. For
# example: `/** ... */` or `/*! .... */
# The search pattern for a documentation
# comment section using single line comments
# where the comment starts with `///` or
# `//!`. Note that at least 2 lines of the
# comments are required and the section ends
# when a non-commented line is reached.
pattern_docComment = r'''
    (?:
        [ \t]*/[*][*!]\n*  # Matches the leading javadoc/QT comment block delimiter
        ([\S\s]*?)         # Captures the contents of the comment block
        [ \t]*[*]+/        # Matches the trailing javadoc/QT comment block delimiter
    )|(
        (?:[ \t]*//[/!][\s\S]*?\n){2,}  # Matches the /// or //! style comments
    )
'''


#
#
#
#
pattern_leadingChars = r'''
    ^[ \t]*  # Any amount of whitespace at the start of line
    (?:
        (?:[*]?)|  # javadoc/QT chars
        (?://[/!]) # /// or //! style chars
    )
    [ \t]*  # Any amount of whitespace after comment chars
'''


#
#
#
pattern_version = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Version: ([\s\S]*?)$
'''
replace_version = r'''\1@version @parblock\n\1        \2\n\1@endparblock'''


#
#
#
pattern_license = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    License: ([\s\S]*?)$
'''
replace_license = r'''\1@par License\n\1@parblock\n\1        \2\n\1@endparblock'''


#
#
#
pattern_date = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Date: ([\s\S]*?)$
'''
replace_date = r'''\1@date @parblock\n\1     \2\n\1@endparblock'''


#
#
#
pattern_authors = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Authors: ([\s\S]*?)$
'''
replace_authors = r'''\1@authors @parblock\n\1        \2\n\1@endparblock'''


#
#
#
pattern_copyright = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Copyright: ([\s\S]*?)$
'''
replace_copyright = r'''\1@copyright @parblock\n\1          \2\n\1@endparblock'''


#
#
#
pattern_seealso = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    See Also: ([\s\S]*?)$
'''
replace_seealso = r'''\1@see @parblock\n\1         \2\n\1@endparblock'''


#
#
#
pattern_throws = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Throws: ([\s\S]*?)
    (?:
        \Z |
        (?=
        (?:{pattern_leadingChars})*  # Capture standard line leading chars
        {pattern_leadingChars}See)
    )
'''
replace_throws = r'''\1@par Exceptions\n\1@parblock\n\1       \2\1@endparblock\n'''

#
#
#
pattern_standards = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Standards: ([\s\S]*?)$
'''
replace_standards = r'''\1@par Standards\n\1@parblock\n\1          \2\n\1@endparblock'''


#
#
#
pattern_deprecated = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Deprecated: ([\s\S]*?)$
'''
replace_deprecated = r'''\1@deprecated @parblock\n\1           \2\n\1@endparblock'''


#
#
#
pattern_bugs = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Bugs: ([\s\S]*?)$
'''
replace_bugs = r'''\1@bug @parblock\n\1     \2\n\1@endparblock'''


#
#
#
pattern_note = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Note: ([\s\S]*?)$
'''
replace_note = r'''\1@note @parblock\n\1     \2\n\1@endparblock'''


#
#
#
pattern_examples = fr'''
    ({pattern_leadingChars})  # Capture standard line leading chars
    Examples: ([\s\S]*?)$
'''
replace_examples = r'''\1@par Examples\n\1@parblock\n\1         \2\n\1@endparblock'''


# The seaerch pattern for a params
# section in a function documentation
# block. This pattern supports both
# block comment and line comment styles.
# The params section is defined to end when
# we encounter the end of the comment
# block of when we encounter another section
# header. This means we have to list all
# the support section headers in the regex.
#
# Example section format:
# ````````
# Params:
#     ...
#     ...
# `````````
pattern_paramsSection = r'''
    (\s*(?:(?:///)|(?:[*]*))\s*Params:\n  # Matches the params section header
    [\s\S\n]*?)                           # Matches the contents of the params section
    (?:$|                                 # Matches the end of the string
        (?=\s*(?:(?:///)|(?:[*]*))\s*Note:)|    # Lookahead for when we see a "Note" section
        (?=\s*(?:(?:///)|(?:[*]*))\s*Returns:)  # Lookahead for when we see a "Returns" section
    )
'''









#
#
#
#
pattern_paramHeader = r'''
    (\s*(?:(?:///)|(?:[*]*)))\s*Params:\n
'''

#
#
#
replace_paramHeader = r'\1\n'

pattern_param = r'''
([\s*]*)([a-zA-Z_][a-zA-Z0-9_]+)\s*=\s*(.*)\n
'''

replace_param = r'''\1 @param \2 \3\n'''

filters = [
    (pattern_docComment, [
        # (pattern_version,    replace_version),
        # (pattern_license,    replace_license),
        # (pattern_date,       replace_date),
        # (pattern_authors,    replace_authors),
        # (pattern_copyright,  replace_copyright),
        # (pattern_seealso,    replace_seealso),
        (pattern_throws,     replace_throws),
        # (pattern_standards,  replace_standards),
        # (pattern_deprecated, replace_deprecated),
        # (pattern_bugs,       replace_bugs),
        # (pattern_note,       replace_note),
        # (pattern_examples,   replace_examples),
    #     (pattern_paramsSection, [
    #         (pattern_param, replace_param),
    #         (pattern_paramHeader, replace_paramHeader),
    #     ]),
    ]),
]



def sub(filters, text):
    # pprint(filters)
    # print("=====================")
    # print(text)
    # print("=======================")
    tmptext = text
    for pattern, replace in filters:
        if type(pattern) is str and type(replace) is str:
            tmptext = re.sub(pattern, replace, tmptext, flags=re.VERBOSE | re.MULTILINE)
            # print(pattern)
            # print(replace)
            # print("++++++++++++++++++++++++")
            # print(tmptext)
            # print("++++++++++++++++++++++++")
        else:
            for match in re.finditer(pattern, text, flags=re.VERBOSE | re.MULTILINE):
                # print("------------------------------------------------")
                subtext = match.expand(r'\1\2')
                # print("------------------------------------------------")
                subtmptext = sub(replace, subtext)
                tmptext = tmptext.replace(subtext, subtmptext)
    return tmptext

if __name__ == '__main__':

    # Open the file and read in the
   # entire contents as text.
    filename = sys.argv[1]
    with open(filename) as f:
        text = f.read()

    # Recursively process the text
    text = sub(filters, text)
    print(text, end="")


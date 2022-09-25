import sys
from lark import Lark
from lark.visitors import *
from lark.reconstruct import Reconstructor

from pprint import pprint

# Open the file and read in the
# entire contents as text.
filename = sys.argv[1]
with open(filename) as f:
    text = f.read()

# Construct the parsers from the grammar files. W have both an input and an
# output grammar so that we can reconstruct the source file based on the
# output grammar. The input grammar correcponds to ddoc style documentation
# comments, while the output grammar corresponds to the doxygen style
# documentation comments. We keep all tokens and have no maybe placeholders
# so the source file can be reconstructed using a Reconstructor instance.
inputParser  = Lark.open('grammarInput.lark',  keep_all_tokens=True, maybe_placeholders=False)
# outputParser = Lark.open('grammarOutput.lark', keep_all_tokens=True, maybe_placeholders=False)

# class Something(Transformer):

#     # TODO: just transform all tokens into the pattern from the output grammar
#     def transformToken(self, token):
#         tokenName = token.type
#         outputValue = outputParser.get_terminal(tokenName).pattern.value
#         return token.update(value=outputValue)

#     # Section header transforms
#     def SECTION_HEADER_DATE(self, token):      return self.transformToken(token)
#     def SECTION_HEADER_VERSION(self, token):   return self.transformToken(token)
#     def SECTION_HEADER_COPYRIGHT(self, token): return self.transformToken(token)

# recon  = Reconstructor(outputParser)
# trans  = Something()

tree = inputParser.parse(text)
# tree = trans.transform(tree)
# pprint(tree)
# output = recon.reconstruct(tree)
# print(output)


print("-------------")
print(tree.pretty())

from pathlib import Path

#Multiline comments - control + /

# file_path = Path(
#     "~/davenport/fall2026/algorithms_CSCI445/"
#     "wk2/ProbabilisticAnalysisAndRandomizedAlgorithms/"
#     "aiDocs/Design_and_Testing_Document.md").expanduser()
#
# #similar to try-with-resources from java
# #with will open the resource, then clean it up after wards, so I don't have to close it
# #as gives the file_path a variable name - in this case "file"
# with file_path.open() as file:
#     contents = file.read()
#     print(contents)


p = Path('..')
print()
print(p.resolve())
print(list(p.glob('des*.pdf')))


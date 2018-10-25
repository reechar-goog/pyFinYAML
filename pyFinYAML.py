import sys

if len(sys.argv) != 3:
  print("ERROR: Usage is python pyFinYAML.py <inputfile> <outputfile>")
  exit()
templateFile = sys.argv[1]
outputFile = sys.argv[2]
f=open(templateFile, "r")
contents = f.read()
try:
  start = contents.index("{{")
  end = contents.index("}}")
except:
  print("ERROR: Could not find template file {{ }}")
  exit()

fileName = contents[start+3:end-1]

f2 = open(fileName, "r")
fileContents = f2.read()
stringedFileContents = "\"" + fileContents.replace("\n","\\n") + "\""

result = contents[:start] + stringedFileContents + contents[end+2:]
f3 = open(outputFile, "w")
f3.write(result)

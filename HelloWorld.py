from junit_xml import TestSuite, TestCase

print( "Goodbye, World!" )

test_case = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
ts = TestSuite("my test suite", test_case)
print(TestSuite.to_xml_string([ts]))
with open('output.xml', 'w') as f:
  TestSuite.to_file(f, [ts], prettyprint=false)


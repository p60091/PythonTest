from junit_xml import TestSuite, TestCase

print( "Goodbye, World!" )
test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
ts = TestSuite("my test suite", test_case)
print(TestSuite.to_xml_string([ts]))


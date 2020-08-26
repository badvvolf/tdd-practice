from core import TestCase, WasRun

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod" == test.log)

TestCaseTest("testTemplateMethod").run()

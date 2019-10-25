from ETC import ETC
import sys, traceback
#TODO(Mike): import test data

usage = '''
            \tUsage: python ETC_UT.py [test_code, ...]
            \t\t [test_code, ...]
            \t\t     test_code:   The ID of a unit test to run. Default all.
        '''

class ETCUnitTester():

    def __init__(self):
        #TODO(Mike): thread test data into ETC
        self.etc = ETC()

    '''
        Runs specified unit tests
            @testList - a list of test codes to run. If empty runs all tests
    '''
    def runTests(self, testList):
        curTest = 2

        # run specified tests
        while len(testList) > curTest:
            try:
                # run test x
                func = getattr(self, '_test' + testList[curTest], None)
                if not func:
                    print('Error: No unit test corresponding to %s found' % testList[curTest])
                else:
                    func()
            except Exception as e:
                print("Error while processing unit test %s" % testList[curTest])
                traceback.print_tb(e.__traceback__)
            curTest += 1
        
        # default: run all tests
        if curTest == 2:
            func = getattr(self, '_test' + testList[curTest], None)
            while func:
                try:
                    # run test x
                    func()
                except Exception as e:
                    print("Error while processing unit test %s" % testList[curTest])
                    traceback.print_tb(e.__traceback__)
                curTest += 1
                func = getattr(self, '_test' + testList[curTest], None)

    #TODO(Mike): define test
    def _test1(self):
        pass

    #TODO(Mike): define test
    def _test2(self):
        pass

    #TODO(Mike): define test
    def _test3(self):
        pass


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print(usage)

    unitTester = ETCUnitTester()
    unitTester.runTests(sys.argv[2:])

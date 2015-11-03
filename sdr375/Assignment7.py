#__author__ = 'SeansMBP'
#Runs the code for all 4 parts
import Question1
import Question2
import Question3
import Question4

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Assignment7:
    @staticmethod
    def main():

        Question1.q1()
        Question2.q2()
        Question3.q3()
        Question4.q4()


if __name__ == '__main__':
    try:
        Assignment7.main()
    except MyError as e:
        print 'My exception occurred, value:', e.value

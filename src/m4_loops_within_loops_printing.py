"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in PRINTING-TO-CONSOLE problems.  ***

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.


###############################################################################
# TODO: 2.  [Note: same _TODO_ as its matching one in module m1.]
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################

import testing_helper
import time


def main():
    """Calls the   TEST   functions in this module."""
    run_test_shape()


def run_test_shape():
    """Tests the    shape    function."""
    print()
    print("--------------------------------------------------")
    print("Testing the   SHAPE   function:")
    print("--------------------------------------------------")

    print()
    print("Test 1 of shape: r=7")
    shape(7)

    print()
    print("Test 2 of shape: r=4")
    shape(4)

    print()
    print("Test 3 of shape: r=2")
    shape(2)


def shape(r):
    """
    Prints a shape with r rows that looks like this example where r=7:
    1234567!7654321++
     123456!654321-+
      12345!54321--++
       1234!4321---+
        123!321----++
         12!21-----+
          1!1------++

    Another example, where r=4:
    1234!4321++
     123!321-+
      12!21--++
       1!1---+

    Preconditions:  r is a positive number.
    For purposes of "lining up", assume r is a single digit.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    ###########################################################################
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:  15 minutes.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(
    arguments, expected, test_results, format_string, suffix=""
):
    testing_helper.print_expected_result_of_test(
        arguments, expected, test_results, format_string, suffix
    )


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    testing_helper.print_actual_result_of_test(
        expected, actual, test_results, precision
    )


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The  IF  statement helps prevent   main   from running
# when we are doing special testing within a testing framework.
# The   try .. except   helps prevent error messages on the console
# from being intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise

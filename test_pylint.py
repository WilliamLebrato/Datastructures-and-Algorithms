import pylint
import sys

sys.argv = ["pylint", "red_black_tree"]
pylint.run_pylint()
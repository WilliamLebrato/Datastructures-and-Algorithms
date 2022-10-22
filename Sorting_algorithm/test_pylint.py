from heapsort import heapsort
from insertionsort import insertionsort
from quicksort import quicksort
import pylint.lint

func_list = ["heapsort","insertionsort","quicksort"]
opt = int(input("Choose, 0 - 2: "))
pylint_opts = ['--disable=line-too-long', func_list[opt]]
pylint.lint.Run(pylint_opts)

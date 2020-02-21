import argparse
from example1 import word_count
from basic2 import the_most_common_words
from basic3 import quicksort
from basic4 import merge_sort
from dop1 import fibonacci

parser = argparse.ArgumentParser()
parser.add_argument('--w', dest='words', default='', type=str, help="Write words to count", nargs="+")
parser.add_argument('--fw', dest='filename_for_words', default='', type=str,
                    help="Write a name of a .txt file for using the WordCount function")
parser.add_argument('--fn', dest='filename_for_nums', default='', type=str,
                    help="Write a name of a .txt file for using functions for sorting")
parser.add_argument('--nums', dest='nums_list', default=0, type=float, help="Write numbers to sort", nargs='+')
parser.add_argument('--fib', dest='fibonacci_count', default=0, type=int,
                    help="Write a number for using the Fibonacci function")
parser.add_argument('--com', action='store_true', help="If you want to choose the most common words from the sentence")
parser.add_argument('--qs', action='store_true', help="For using a quick sort")
parser.add_argument('--ms', action='store_true', help="For using the merge sort")

args = parser.parse_args()
words = list(args.words)
filename_for_words = args.filename_for_words
filename_for_nums = args.filename_for_nums
nums_list = args.nums_list
fibonacci_count = args.fibonacci_count

if filename_for_words:
    with open("D:\STUDY\Python\XD\{0}.txt".format(filename_for_words)) as f:
        words = f.read().split()
if filename_for_nums:
    with open("D:\STUDY\Python\XD\{0}.txt".format(filename_for_nums)) as f:
        nums_list = f.read().split()
        nums_list = list(map(int, nums_list))
if words:
    word_count(words)
    if args.com:
        the_most_common_words(words)
elif nums_list:
    if args.qs:
        quicksort(nums_list)
    else:
        merge_sort(nums_list)
    print(nums_list)
elif fibonacci_count:
    fibonacci(fibonacci_count)
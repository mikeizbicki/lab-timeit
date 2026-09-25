'''
This file contains two techniques for checking if a string is a palindrome.
They have different runtimes depending on which data structures are used.

Palindrome checking is a classic "leetcode easy" problem for interviews.
See: <https://leetcode.com/problems/valid-palindrome/>.
'''

import copy
from collections import deque


def check_palindrome_1(container):
    '''
    check whether the input container reads the same forwards as it does backwards

    >>> check_palindrome_1('abcdcba')
    True
    >>> check_palindrome_1('abcd')
    False

    >>> check_palindrome_1(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    True
    >>> check_palindrome_1(['a', 'b', 'c', 'd'])
    False

    >>> check_palindrome_1(deque(['a', 'b', 'c', 'd', 'c', 'b', 'a']))
    True
    >>> check_palindrome_1(deque(['a', 'b', 'c', 'd']))
    False
    '''
    for i in range(len(container)//2):
        left = container[i]
        right = container[len(container)-1-i]
        if left != right:
            return False
    return True


def check_palindrome_2(container):
    '''
    check whether the input container reads the same forwards as it does backwards

    >>> check_palindrome_2('abcdcba')
    True
    >>> check_palindrome_2('abcd')
    False

    >>> check_palindrome_2(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    True
    >>> check_palindrome_2(['a', 'b', 'c', 'd'])
    False

    >>> check_palindrome_2(deque(['a', 'b', 'c', 'd', 'c', 'b', 'a']))
    True
    >>> check_palindrome_2(deque(['a', 'b', 'c', 'd']))
    False
    '''

    # this line converts the input container into an equivalent deque;
    # converting from one form of a container into another has the runtime
    # of performing a copy on the container you are converting into
    container_copy = deque(container)
    
    for i in range(len(container)//2):
        left = container_copy.popleft()
        right = container_copy.pop()
        if left != right:
            return False
    return True


def check_palindrome_3(container):
    '''
    check whether the input container reads the same forwards as it does backwards

    >>> check_palindrome_3(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    True
    >>> check_palindrome_3(['a', 'b', 'c', 'd'])
    False

    >>> check_palindrome_3(deque(['a', 'b', 'c', 'd', 'c', 'b', 'a']))
    True
    >>> check_palindrome_3(deque(['a', 'b', 'c', 'd']))
    False
    '''
    # the copy.copy command copies the original container keeping the type;
    # in python, strings are *immutable* (they can never be changed);
    # this algorithm requires modifying the container_copy object,
    # and so it cannot work on strings
    container_copy = copy.copy(container)
    
    for i in range(len(container)//2):
        # lists and deques have difference interfaces for removing the leftmost elem
        # In lists, this operation takes time Theta(n) and so Guido wanted it to
        # be a bit awkward to use so that programmers wouldn't do it on accident.
        # The code below uses the appropriate function depending on the container.
        if isinstance(container_copy, deque):
            left = container_copy.popleft()
        else:
            left = container_copy.pop(0)

        # removing the rightmost element takes time O(1) in both lists and deques
        # python was therefore designed to use the same function .pop() for both objs
        # and the code below is the same as check_palindrome_2
        right = container_copy.pop()
        if left != right:
            return False
    return True

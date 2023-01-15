## 0x04. Python - More Data Structures: Set, Dictionary

### What you should learn from this project

```
At the end of this project you are expected to be able to explain to
anyone, without the help of Google:
```

* Why Python programming is awesome (don’t forget to tweet today,
  with the hashtag #pythoniscool :))
* What are set and how to use them
* What are the most common methods of set and how to use them
* When to use sets versus lists
* How to iterate into a set
* What are dictionary and how to use them
* When to use dictionaries versus lists or sets
* What is a key in a dictionary
* How to iterate into a dictionary
* What is a lambda function
* What is map, reduce and map functions

**Exercises**

**0. Squared simple**

     Write a function that computes the square value of all integers of
     a matrix.

* Prototype: def square_matrix_simple(matrix=[]):
  matrix is a 2 dimensional array
* Returns a new matrix:
* Same size as matrix
* Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allow to use regular loops, map, etc.

**1. Search and replace**

     Write a function that replaces all occurrences of an element by
     another in a new list.

* Prototype: def search_replace(my_list, search, replace):
  my_list is the initial list
* search is the element to replace in the list
  replace is the new element
* You are not allowed to import any module

**2. Unique addition**

     Write a function that makes the addition of all unique integers
     in a list (only one time each integer).
* Prototype: def uniq_add(my_list=[]):
* You are not allowed to import any module

**3. Present in both**

     Write a function that returns a set of common elements in two sets.

* Prototype: def common_elements(set_1, set_2):
* You are not allowed to import any module

**4. Only differents**

     Write a function that returns a set of all elements present in only one set.

* Prototype: def only_diff_elements(set_1, set_2):
* You are not allowed to import any module

**Write a function that returns the number of keys in a dictionary.

**5. Number of keys**

     Write a function that returns the number of keys in a dictionary.

* Prototype: def number_keys(a_dictionary):
* You are not allowed to import any module

**6. Print sorted dictionary**

     Write a function that prints a dictionary by ordered keys.

* Prototype: def print_sorted_dictionary(a_dictionary):
* You can assume that all keys are string
* Keys should be sorted by alphabetic order
* Only sort keys of the first level (don’t sort keys of a
  dictionary inside the main dictionary)
* Dictionary values can have any type
* You are not allowed to import any module

**7. Update Dictionary**

     Write a function that replace or add key/value in a dictionary.

* Prototype: def update_dictionary(a_dictionary, key, value):
* key argument will be always a string
* value argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* You are not allowed to import any module

**8. Simple delete by key**

     Write a function that deletes a key in a dictionary.

* Prototype: def simple_delete(a_dictionary, key=""):
* key argument will be always a string
* If a key doesn’t exist, the dictionary won’t change
* You are not allowed to import any module

**9. Multiply by 2**

     Write a function that returns a new dictionary with all values
     multiplied by 2

* Prototype: def multiply_by_2(a_dictionary):
* You can assume that all values are only integers
* Returns a new dictionary
* You are not allowed to import any module

**10. Best score**

    Write a function that returns a key with the biggest integer value.

* Prototype: def best_score(a_dictionary):
* You can assume that all values are only integers
* If no score found, return None
* You can assume all students have a different score
* You are not allowed to import any module

**11. Multiply by using map**

      Write a function that returns a list with all values multiplied
      by a number without using any loops.

* Prototype: def mutiply_list_map(my_list=[], number=0):
* Returns a new list:
* Same length as my_list
* Each value should be multiplied by number
* Initial list should not be modified
* You are not allowed to import any module
* You have to use map
* Your file should be max 3 lines

**12. Roman to Integer**

      Technical interview preparation:
      You are not allowed to google anything
      Whiteboard first

      Create a function def roman_to_int(roman_string):
      that converts a Roman number to an integer.

* You can assume the number will be between 1 to 3999.
  def roman_to_int(roman_string) must return an integer
* If the roman_string is not a string or None, return 0

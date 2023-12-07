{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f96c485d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c74c57d4",
   "metadata": {},
   "source": [
    "**1. Accessing the list : by index number, starting from 0 to len-1**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "173f7244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 6, 8, 10]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9c1fdce3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(l[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "807dd3af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "print(l[1:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4813bbb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 6]\n"
     ]
    }
   ],
   "source": [
    "print(l[0:4: 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d0d58be6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "print(l[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b50232c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "print(l[::])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ea59c77f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 8, 6, 4, 2]\n"
     ]
    }
   ],
   "source": [
    "print(l[4::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4d9da63f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 8, 6, 4, 2]\n"
     ]
    }
   ],
   "source": [
    "print(l[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "351ddc2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 6, 2]\n"
     ]
    }
   ],
   "source": [
    "print(l[4::-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69d37f95",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "7b407997",
   "metadata": {},
   "source": [
    "**2. Insert into list:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "07cd17cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 19, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "l.insert(3, 19)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "6f14f1a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 8, 10, 17, 19]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "bb5b120f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19, 67]\n"
     ]
    }
   ],
   "source": [
    "#append() -> add the element at last of list\n",
    "l.append(67)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "37237a31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19, 67, 44, 55, 66]\n"
     ]
    }
   ],
   "source": [
    "#extend() -> adds the whole list in original list at last\n",
    "l.extend([44, 55, 66])\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "299002b7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "e8088623",
   "metadata": {},
   "source": [
    "**3. Update/Modify in List: as list is mutable/changeable**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "15407449",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 17, 19, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "l[2] = 17\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37a964ed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "b74a9a37",
   "metadata": {},
   "source": [
    "**4. Reverse and sort the list:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4f2c7bfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 8, 19, 17, 4, 2]\n"
     ]
    }
   ],
   "source": [
    "l.reverse()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2f6cb251",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l.sort()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5308d05e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "97b01cd3",
   "metadata": {},
   "source": [
    "**5. Deletion in list:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "0b55803c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 10, 17]\n"
     ]
    }
   ],
   "source": [
    "#pop() -> if index given, then deletes that element, else deletes lats element. it returns the deleted element\n",
    "l.pop()\n",
    "l.pop(2)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "6289613f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 10, 17]\n"
     ]
    }
   ],
   "source": [
    "#remove() -> deletes by element \n",
    "l.remove(4)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "c2c1666f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 17]\n"
     ]
    }
   ],
   "source": [
    "#del -> it can deletes the element by its index, range of index or whole list from existance\n",
    "del l[0]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b2d3e3fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 8, 10, 17, 19]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "fe50ad3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "del l[1:3]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "67a76442",
   "metadata": {},
   "outputs": [],
   "source": [
    "del (l)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a293abf6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'l' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [58], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43ml\u001b[49m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'l' is not defined"
     ]
    }
   ],
   "source": [
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "c269f694",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 8, 10, 17, 19]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "95088772",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "#clear() -> empties the list; the structure of list remains in the existence\n",
    "l.clear()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e09f448b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "342953dc",
   "metadata": {},
   "source": [
    "**6. List reference and its copy**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "efd23f69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 8, 10, 17, 19]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "ffc6eccc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n",
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "# '=' in list creates reference to the original list. any change in any list will create the changes in all list wih the same reference list\n",
    "l2 = l\n",
    "print(l)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "96c356cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 89, 10, 17, 19]\n",
      "[2, 4, 89, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l[2] = 89\n",
    "print(l)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "327761d1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "03bcee37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 8, 10, 17, 19]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "084c885e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 17, 19]\n",
      "[2, 4, 8, 10, 3, 19]\n"
     ]
    }
   ],
   "source": [
    "#using copy() -> we make a copy of original list, changes will not reflect\n",
    "l2 = l.copy()\n",
    "l2[4] = 3\n",
    "print(l)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b63c79b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "a2189cb2",
   "metadata": {},
   "source": [
    "**7. List Comprehension: it is used to select the specific items from the list based on a condition. It works only on iterable objects like list, tuple, range(), etc**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "11fc5fbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'mango']\n"
     ]
    }
   ],
   "source": [
    "#normally, by this way we can do the work\n",
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "newlist = []\n",
    "\n",
    "for x in fruits:\n",
    "  if \"a\" in x:\n",
    "    newlist.append(x)\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "4dec49db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'mango']\n"
     ]
    }
   ],
   "source": [
    "#by list comprehension (of one line code) -> becomes easy to implement\n",
    "#if there is only one condition -> use if after for\n",
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "\n",
    "newlist = [x for x in fruits if \"a\" in x]\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "8e8d9a18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hello', 'hello', 'hello']\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "\n",
    "newlist = [\"hello\" for x in fruits if \"a\" in x]\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "96e305cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'not available', 'not available', 'mango']\n"
     ]
    }
   ],
   "source": [
    "#if there is 2 or more condition use, if-else before for\n",
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "\n",
    "newlist = [x if \"a\" in x else \"not available\" for x in fruits]\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "cf6c0e28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "newlist = [x for x in range(10) if x<5]\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f3e7aeb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "41167d1b",
   "metadata": {},
   "source": [
    "**8. count() -> returns the count of a specific elementt**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "ad1225ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 8, 10, 2, 17, 2, 3, 2, 19]\n"
     ]
    }
   ],
   "source": [
    "l = [2, 4, 8, 10, 2, 17, 2, 3, 2, 19]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "236f0c58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(l.count(2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d4bba02",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "197e4618",
   "metadata": {},
   "source": [
    "**9. index() -> return sthe index of first occurence of a specific element**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "be27bd99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "print(l.index(2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "984214c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(l.index(17))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "76d80610",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "90 is not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [92], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43ml\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mindex\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m90\u001b[39;49m\u001b[43m)\u001b[49m)\n",
      "\u001b[1;31mValueError\u001b[0m: 90 is not in list"
     ]
    }
   ],
   "source": [
    "print(l.index(90))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f58f85a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25b9ce2b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

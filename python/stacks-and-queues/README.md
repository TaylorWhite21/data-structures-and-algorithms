# Stacks and Queues
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Challenge
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
Implement the following methods:
  enqueue
    Arguments: animal
      animal can be either a dog or a cat object.
  dequeue
    Arguments: pref
      pref can be either "dog" or "cat"
    Return: either a dog or a cat, based on preference.
      If pref is not "dog" or "cat" then return null.

## Approach & Efficiency
I took a TDD approach and designed my tests before I wrote my code. It made it 1000% easier.

enqueue:
Big(O):
Space: O(n)
Time: O(1)

dequeue:
Big(o):
Space: O(n)
Time: O(n)

## API
Stack:
Pop
Push

Queue:
Enqueue
Dequeue

#!/usr/bin/env python3
"""Demo of inheritance and polymorphism with animals."""


class Animal:
    """Base class for all animals."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """A dog, which is an Animal."""

    def speak(self):
        """Return the sound of a dog."""
        return "Woof"


class Cat(Animal):
    """A cat, which is an Animal."""

    def speak(self):
        """Return the sound of a cat."""
        return "Meow"


if __name__ == "__main__":
    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    dog = Dog()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))

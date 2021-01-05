# old mac donald

def verse(animal, sound):
    L1 = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    print(L1)
    print("And on that farm he had a",animal,",Ee-igh, Ee-igh, Oh!")
    sound2 = sound + ", " + sound
    print("With a", sound2, "here and a", sound2, "there.")
    print("Here a",sound,",there a ",sound,", everywhere a ",sound2,".")
    print(L1)

verse("cow","moo")
verse("dog","woof")
verse("duck","quack")
verse("cat","meow")
verse("pig","oink")

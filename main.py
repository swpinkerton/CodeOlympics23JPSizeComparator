import fractions
import random

object_sizes = {
    "Apple": 0.075,
    "Banana": 0.2,
    "Chair": 0.5,
    "Table": 1.5,
    "Computer": 0.4,
    "Phone": 0.15,
    "Car": 4.7,
    "Bicycle": 1.8,
    "Book": 0.25,
    "Cup": 0.1,
    "Plant": 0.5,
    "Shoe": 0.28,
    "Shirt": 0.75,
    "Pants": 1.1,
    "Jacket": 1.2,
    "Television": 1.2,
    "Refrigerator": 1.8,
    "Oven": 0.75,
    "Toaster": 0.25,
    "Clock": 0.25,
    "Desk": 1.0,
    "Drawer": 0.6,
    "Keyboard": 0.45,
    "Mouse": 0.1,
    "Lamp": 0.5,
    "Bed": 2.0,
    "Pillow": 0.5,
    "Blanket": 2.2,
    "Mirror": 1.0,
    "Picture": 0.5,
    "Vase": 0.5,
    "Fork": 0.2,
    "Knife": 0.2,
    "Spoon": 0.2,
    "Bowl": 0.2,
    "Plate": 0.28,
    "Glasses": 0.15,
    "Curtains": 1.8,
    "Towel": 1.0,
    "Soap": 0.1,
    "Toothbrush": 0.2,
    "Toothpaste": 0.2,
    "Razor": 0.15,
    "Scissors": 0.15,
    "Pencil": 0.15,
    "Pen": 0.15,
    "Eraser": 0.05,
    "Marker": 0.15,
    "Glue": 0.1,
    "Tape": 0.05,
    "Stapler": 0.2,
    "Envelope": 0.25,
    "Monitor": 0.5,
    "Speaker": 0.3,
    "Couch": 2.0,
    "Rug": 2.0,
    "Coffee table": 1.2,
    "Dresser": 1.2,
    "Bathtub": 1.5,
    "Sink": 0.6,
    "Toilet": 0.7,
    "Shower": 1.0,
    "Tissue box": 0.15,
    "Trash can": 0.5,
    "Air conditioner": 1.5,
    "Laptop": 0.3,
    "Printer": 0.4,
    "Scanner": 0.4,
    "Projector": 0.4,
    "Whiteboard": 1.2,
    "Microphone": 0.15,
    "Headphones": 0.25,
    "Drum": 1.0,
    "Guitar": 1.0,
    "Bass": 1.2,
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait Clock Tower": 601,
    "Ping An Finance Center": 599,
    "Goldin Finance 117": 596,
    "Lotte World Tower": 555,
    "One World Trade Center": 541,
    "Guangzhou CTF Finance Centre": 530,
    "Tianjin CTF Finance Centre": 530,
    "Changsha IFS Tower T1": 452,
    "Wuhan Greenland Center": 438,
    "Empire State Building": 381,
    "Petronas Twin Towers": 379,
    "Zifeng Tower": 450,
    "Jin Mao Tower": 421,
    "International Commerce Centre": 484,
    "Central Plaza": 374,
    "The Shard": 310,
    "Bank of China Tower": 367,
    "Eiffel Tower": 324,
    "Taipei 101": 508,
    "Tuntex Sky Tower": 348,
    "Gran Torre Santiago": 300,
    "Sky Tower": 328,
    "Al Hamra Tower": 412,
    "Elite Residence": 380,
    "Almas Tower": 360,
    "The Marina Torch": 348,
    "Emirates Park Towers Hotel & Spa": 327,
    "Trump International Hotel and Tower": 423,
    "Aura": 272,
    "John Hancock Center": 343,
    "Oryx Tower": 300,
    "The Address Downtown Dubai": 302,
    "The Index": 326,
    "The Address The BLVD": 306,
    "Eton Place Dalian Tower 1": 383,
    "Eton Place Dalian Tower 2": 307,
    "Lakhta Center": 462,
    "Lotus Riverside": 140,
    "Plaza 66 Tower 1": 288,
    "Rose Tower": 333,
    "The Address Dubai Mall": 302,
    "The Bow": 236,
    "The Pinnacle": 258,
    "Vattanac Capital": 187,
    "World Financial Center": 492,
    "Zabeel Tower One": 235,
    "Zabeel Tower Two": 235
}


def object (index):
    keys = list(object_sizes.keys())
    object = keys[index]
    return (object)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(object(1))
    unit = str(input("m(metres) or ft(feet)\n"))
    height = float(input("please enter your measurement - numbers only\n"))
    fraction1 = 0
    fraction2 = 0
    while (fraction1 > 100 or fraction1 < 0.001 or fraction2 > 100 or fraction2 < 0.001 ):
        object1 = object(random.randint(0,123))
        object2 = object(random.randint(0,123))

        if (unit == "ft"):
            mult = 3.2808
        else:
            mult = 1

        fraction1 = height/object_sizes[object1]*mult
        fraction2 = height/object_sizes[object2]*mult

    print("%.3f%s is %.3f of %s and %.3f of %s" %(height, unit, fraction1, object1, fraction2, object2))

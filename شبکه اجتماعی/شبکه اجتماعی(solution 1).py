class Person:

    objects = dict()
    find_counter = 1
    def __init__(self,username, gender, age, id) -> None:
        self.username= username
        self.gender= gender
        self.age= age
        self.id = id
    
    def __str__(self) -> str:
        return f"{self.username} {self.gender} {self.age} {self.id}"


    def add(self):
        Person.objects.update({self.id:self})
        print(f"User {self.id} added successfully")

    def find(id):
        found_user = Person.objects.get(id)
        if found_user:
            print(Person.find_counter,found_user)
        else:
            persons_with_similar_id = sorted(list(filter(lambda x:x.startswith(id) ,Person.objects.keys())))
            if len(persons_with_similar_id):
                for person_id in persons_with_similar_id[:10]:
                    print(Person.find_counter,Person.objects[person_id])
            else:
                print(Person.find_counter, 'No user found')
        Person.find_counter+=1


for i in range(100000):
    try:
        command = input().split()
        if command[0]== "Add":
            p = Person(*command[1:])
            p.add()
        elif command[0]=="Find":
            Person.find(command[1])
       
    except:
        break

    # command = input().split()
    # if command[0]== "Add":
    #     p = Person(*command[1:])
    #     p.add()
    # elif command[0]=="Find":
    #     Person.find(command[1])
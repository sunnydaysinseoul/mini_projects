# recreate "mad libs"game using STRING CONCATENATION
# noun, verb, adjective 같은거 물어본다음에 마지막에 full sentence로 만들어주는 것

youtuber = "shane's kpop videos"
# print(f"subscribe to {youtuber}"); #seems like this is the cleanest way!

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
input ('\n\nPress enter to close the window.')
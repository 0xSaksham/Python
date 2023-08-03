guests = [' Shri Narendra Modi Ji', 
          'Elon Musk', 
          ' Shri Manoj Kumar Gupta', 
          'Andrew Tate',
          'Jordan Peterson',
          'Saksham Gupta']

print("Sorry People, my bigger table is cancelled and I only have 2 seats left")

# Poping the guests I can't invite anymore

guest_not_invited = guests.pop()

print("Sorry, I can't invite you anymore " + guest_not_invited )

guest_not_invited = guests.pop()

print("Sorry, I can't invite you anymore " + guest_not_invited )

guest_not_invited = guests.pop()

print("Sorry, I can't invite you anymore " + guest_not_invited )

guest_not_invited = guests.pop()

print("Sorry, I can't invite you anymore " + guest_not_invited )

#Guests still invited

print("You are still Invited sir: " + guests[0] + " & " + guests[1])

#Deleting the list

del(guests[1])
del(guests[0])

print(guests)

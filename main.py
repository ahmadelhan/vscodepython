def login():
        dbStore = open("data.txt", "r")
        userID = input("Enter UID: ")
        userPwd = input("Enter pass: ")
        
        if not len (userID or userPwd)<1:
            dList = []
            fList = []
            for i in dbStore:
                storedUID,storedPwd = i.split(", ")
                storedPwd = storedPwd.strip()
                dList.append(storedUID)
                fList.append(storedPwd)
            info = dict(zip(dList, fList))
            
            try:
                if info[userID]:
                    try: 
                        if userPwd == info[userID]:
                            print("Logged in.")
                            return True
                        else:
                            print("Incorrect credentials.")
                    except:
                        print("UID / Pass are incorrect.")
                else:
                    print("UID does not exist.")
            except:
                print("An error occured.")
            return False

max_attempts = 3
for _ in range (3):
    print("Please Login to continue...", 
          f"\nAttempts remaining: {max_attempts}")
    if login():
        break
    else:
        print("Incorrect details entered. Please try again.")
        max_attempts -= 1
print("Login failed. Exiting...")
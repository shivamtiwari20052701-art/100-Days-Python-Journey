
with open("DAY24/mail_merge_project/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
     letter = file.read()
with open("DAY24/mail_merge_project/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        name=name.strip()#removes \n
        
        personalized_letter=letter.replace("[name]",name)#Replace the [name] placeholder with names 

        with open(f"DAY24/mail_merge_project/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt",mode="w") as file:
            file.write(personalized_letter)
            

        


greeting = input("Hello, possible pirate! What's the password?") #no closing " after 'password?'
if greeting == "Arrr!": #no point checking with list as only 1 condition, so replaced [ ] with == for 1 condition 'Arrr'
	print("Go away, pirate.")
else: #elif needds condition. in this case we can just keep it as 'else' as we're checking if they say 'Arrr' or not
	print("Greetings, hater of pirates!") #print was not inside else block, tabbed once and kept space


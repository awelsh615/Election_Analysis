my_votes=int(input('How many votes did you get?'))
total_votes=int(input('What is the total number of votes?'))

#percentage_votes=(my_votes/total_votes)*100
#print('I received '+str(percentage_votes)+"% of the total votes.")

print(f'I received {my_votes/total_votes *100:.2f}% of the total votes.')
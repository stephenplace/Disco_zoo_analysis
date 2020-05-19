from animal_pos import animal_dict_12 as animal_dict
from itertools import combinations
import Disco_functions as af
import csv

output_list = []

def main():
	
	#all possible pairings in dict
	animal_pairings = list(combinations(animal_dict, 2)) 
	
	#loop through animal_pairings
	for pairing in animal_pairings:
		
		#return a list of possible layout choices, eg. [1,2,3,4][6,7,8] through [22,23,24,25][18,19,20]
		layout_choices = af.list_two_animal_positions(animal_dict[pairing[0]],animal_dict[pairing[1]])
		
		#list of possible animal positions
		animal_1 = animal_dict[pairing[0]]
		animal_2 = animal_dict[pairing[1]]
		
		temp_list, pairing_win_list = [],[]
		
		#loop through layout_choices
		for layout in layout_choices:
			#chosen animal position based on layout loop
			chosen_animal_1 = animal_dict[pairing[0]][layout[0]]
			chosen_animal_2 = animal_dict[pairing[1]][layout[1]]
			wins = 0
		
			#loop for number of games played per layout choices
			for game_number in range(1,101):
			
				#reset before each game
				combo_board = [0]*25
				empty_list,a1pick,a2pick = [],[],[]
				move = []
			
				#loop through ten turns
				for turn in range(1,11):
				
					#reset probability boards each turn before calculations
					animal_1_prob_board,animal_2_prob_board = [0]*25,[0]*25
					
					#produce probability board before making a choice for this turn
					af.produce_prob_boards(animal_1,animal_2,
						animal_1_prob_board,animal_2_prob_board,
						a1pick,a2pick,empty_list)
						
					'''
					#make choice
					'''
					my_choice = af.get_most_probable_position(a1pick,a2pick,
						animal_1_prob_board,animal_2_prob_board) + 1
					'''
					#add to lists of moves selected
					'''
					af.check_choice(my_choice,chosen_animal_1,a1pick,
						chosen_animal_2,a2pick,empty_list)
					'''
					#add to moves and win condition
					#add flag to distinguish move sets for winners and those for losers
					'''
					move.append(my_choice)
					win = bool(set(chosen_animal_1) == set(a1pick)) & bool(set(chosen_animal_2) == set(a2pick))
				#add win after game is over to wins 	
				if win == True:
					wins += 1
					
			win_percent = wins/100
			pairing_win_list.append(win_percent)
			print("\nwin rate:", win_percent)
			print("animal_1:  ",pairing[0]," ",chosen_animal_1)
			print("animal_2:  ",pairing[1]," ",chosen_animal_2)
			
			temp_list = [pairing[0],pairing[1],chosen_animal_1,chosen_animal_2,win_percent]
			output_list.append(temp_list)
		
		print("pairing average win rate:  ", sum(pairing_win_list)/len(pairing_win_list))
		output_list.append(['pairing average win rate',sum(pairing_win_list)/len(pairing_win_list),' ',' ',' '])
		#print(output_list)
		#print('list length', len(pairing_win_list)) #testing
		#break #testing: remove for final product
			
main()

'''write to csv'''
with open('output_12.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['animal_1','animal_2','chosen_1','chosen_2','win_rate'])
	for event in output_list:
		writer.writerow([event[0],event[1],event[2],event[3],event[4]])
		

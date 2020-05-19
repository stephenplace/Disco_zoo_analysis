import random

def list_two_animal_positions(animal_1,animal_2):
    choices = []
    for i in range(len(animal_1)):
        Set1 = set(animal_1[i])
        for j in range(len(animal_2)):
            Set2 = set(animal_2[j])
            if bool(Set1 & Set2) == False:
                choices.append([i,j])
    return choices
	
def produce_prob_boards(a1,a2,a1prob,a2prob,a1pick=[],a2pick=[],El=[]):
    El,a1pick,a2pick = set(El),set(a1pick),set(a2pick)
    for i in range(len(a1)):
        Set1 = set(a1[i])
        for j in range(len(a2)):
            Set2 = set(a2[j])
            if bool((Set1 & Set2) #animals intersect each other -> fails
                    or (Set1 & El) #position in set already empty -> fails	
                    or (Set2 & El) #position in set already empty -> fails
                    or not (a1pick.issubset(Set1)) #position in set already picked -> pass
                    or not (a2pick.issubset(Set2)) #position in set already picked -> pass
					) == False: 
                #unique board positions to add empty_lst
                add_single_animal_to_prob_board(Set1,a1prob) #check name
                add_single_animal_to_prob_board(Set2,a2prob) #check name
				
def get_most_probable_position(a1pick,a2pick,CB1,CB2):
    sum_possibilities = list(map(sum, zip(CB1,CB2)))
    for already_selected in a1pick + a2pick:
        sum_possibilities[already_selected-1] = 0
    m = max(sum_possibilities)
    #fixed'''need to fix to exclude ones already selected'''
    most_prob = [j for j, k in enumerate(sum_possibilities) if k == m]
    return random.choice(most_prob)
	
def add_single_animal_to_prob_board(animal_set,animal_prob_board):
    for i in animal_set:
        animal_prob_board[i-1] += 1
		
def check_choice(choice,chosen_animal_1,a1pick,chosen_animal_2,a2pick,empty_lst=[]):
    if choice in chosen_animal_1:
        a1pick.append(choice)
    elif choice in chosen_animal_2:
        a2pick.append(choice)
    else:
        empty_lst.append(choice)
from django.shortcuts import render, redirect
import random

# Function to show root route and create needed varaible in session
def index(request):
    if 'winners' not in request.session:
        request.session['winners'] = [] # Winneres list
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1,100)
        print("Number is = ",request.session['random_number'])
        request.session['result'] = '' # Result to use i
        request.session['counter'] = 5
        request.session['counter'] = 5
    return render(request,"index.html")

def check_user_number(request):
    request.session['counter'] -= 1
    user_number = int(request.POST['user_number'])
    if (request.session['counter'] == 0):
        request.session['result'] = 'lose'
    elif (request.session['random_number'] > user_number):
        request.session['result'] = 'low'
    elif(request.session['random_number'] < user_number):
        request.session['result'] = 'high'
    else:
        request.session['result'] = 'equal'
    return redirect ("/")

def delete_session(request):
    request.session.clear()
    return redirect ("/")

def add_winner(request):
    winner = {}
    winner['name'] = request.POST['winner_name']
    winner['number_of_attempts'] = 5 - request.session['counter']
    print("winners -->",winner)
    # request.session['winners'].append(winner)
    winners = request.session['winners']
    winners.append(winner)
    request.session['winners'] = winners
    return redirect("/show_winners")

def show_winners(request):
    print(request.session['winners'])
    return render(request,"show_winners.html",{'winners':request.session['winners']})

def back(request):
    save_item = request.session['winners']
    request.session.clear()
    request.session['winners'] = save_item
    return redirect ("/")




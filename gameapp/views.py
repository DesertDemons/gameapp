from django.shortcuts import render, redirect
from .models import Game
from .forms import GamesForm

def game_list(request):
	context = {
		"games": Game.objects.all(),
	}
	return render(request, 'game_list.html', context)

def create(request):
	form = GamesForm()
	if request.method == "POST":
		form = GamesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("game_list")
	context = {
		"form": form,
	}
	return render(request, 'create_game.html', context)

def update(request, Game_id):
	game_obj = Game.objects.get(id=Game_id)
	form = GamesForm(instance=game_obj)
	if request.method == 'POST':
		form = 
from django.shortcuts import render, redirect
from ek_champapp.models import Round, Team_numbers, Team_in_round

# Create your views here.

def base_round(request):
    data = Round.objects.raw('SELECT * FROM ek_champapp_round')  
    return render(request, 'round.html', {'data': data})

def create_round(request):
    return render(request, 'create_round.html')

def store_round(request):
    rdata = Round()
    rdata.round_id = request.POST.get('id')
    rdata.championship_name = request.POST.get('championship_name')
    rdata.round_name = request.POST.get('round_name')
    rdata.round_date = request.POST.get('round_date')
    rdata.race_status = request.POST.get('race_status')
    rdata.driver_changes = request.POST.get('driver_changes')
    rdata.track = request.POST.get('track')
    rdata.base_weight = request.POST.get('base_weight')
    rdata.max_weight = request.POST.get('max_weight')
    rdata.race_duration_time = request.POST.get('race_duration_time')
    rdata.pitlane = request.POST.get('pitlane')
    rdata.save()
    return redirect('/base_round')

def edit_round(request, pk):
    update_r = Round.objects.get(id=pk)
    return render(request, 'edit_round.html', {'update_r': update_r})

def editdata_round(request, pk):
    edata = Round.objects.get(id=pk)
    edata.round_id = request.POST.get('id')
    edata.championship_name = request.POST.get('championship_name')
    edata.round_name = request.POST.get('round_name')
    edata.round_date = request.POST.get('round_date')
    edata.race_status = request.POST.get('race_status')
    edata.driver_changes = request.POST.get('driver_changes')
    edata.track = request.POST.get('track')
    edata.base_weight = request.POST.get('base_weight')
    edata.max_weight = request.POST.get('max_weight')
    edata.race_duration_time = request.POST.get('race_duration_time')
    edata.pitlane = request.POST.get('pitlane')
    edata.save()
    return redirect('/base_round')

def delete_round(request, pk):
    ddata = Round.objects.get(id=pk) 
    ddata.delete() 
    return redirect('/base_round')

def base_teamno(request):
    data = Team_numbers.objects.raw('SELECT * FROM ek_champapp_team_numbers')
    return render(request, 'teamno.html', {'data': data})

def create_teamno(request):
    return render(request, 'create_teamno.html')

def store_teamno(request):
    tdata = Team_numbers()
    tdata.team_number_id = request.POST.get('team_number_id')
    tdata.championship_id = request.POST.get('championship_id')
    tdata.team_id = request.POST.get('team_id')
    tdata.team_number = request.POST.get('team_number')
    tdata.save()
    return redirect('/base_teamno')

def edit_teamno(request, pk):
    update_teamno = Team_numbers.objects.get(id=pk)
    return render(request, 'edit_teamno.html', {'update_teamno': update_teamno})

def editdata_teamno(request, pk):
    edata = Team_numbers.objects.get(id=pk)
    edata.team_number_id = request.POST.get('team_number_id')
    edata.championship_id = request.POST.get('championship_id')
    edata.team_id = request.POST.get('team_id')
    edata.team_number = request.POST.get('team_number')
    edata.save()
    return redirect('/base_teamno')

def delete_teamno(request, pk): 
    ddata = Team_numbers.objects.get(id=pk)
    ddata.delete() 
    return redirect('/base_teamno')

def base_tinround(request):
    data = Team_in_round.objects.raw('SELECT * FROM ek_champapp_team_in_round')
    return render(request, 'tinround.html', {'data': data})

def create_tinround(request):
    return render(request, 'create_tinround.html')

def store_tinround(request):
    tinrdata = Team_in_round()
    tinrdata.id = request.POST.get('id')
    tinrdata.championship = request.POST.get('championship')
    tinrdata.round = request.POST.get('round')
    tinrdata.team_name = request.POST.get('team_name')
    tinrdata.team_number = request.POST.get('team_number')
    tinrdata.start_position = request.POST.get('start_position')
    tinrdata.finish_position = request.POST.get('finish_position')
    tinrdata.position_points = request.POST.get('position_points')
    tinrdata.penalty_points = request.POST.get('penalty_points')
    tinrdata.total_points = request.POST.get('total_points')
    tinrdata.save()
    return redirect('/base_tinround')

def edit_tinround(request, pk):
    update_tinr = Team_in_round.objects.get(id=pk)
    return render(request, 'edit_tinround.html', {'update_tinr': update_tinr})

def editdata_tinround(request, pk):
    edata = Team_in_round.objects.get(id=pk)
    edata.id = request.POST.get('id')
    edata.championship = request.POST.get('championship')
    edata.round = request.POST.get('round')
    edata.team_name = request.POST.get('team_name')
    edata.team_number = request.POST.get('team_number')
    edata.start_position = request.POST.get('start_position')
    edata.finish_position = request.POST.get('finish_position')
    edata.position_points = request.POST.get('position_points')
    edata.penalty_points = request.POST.get('penalty_points')
    edata.total_points = request.POST.get('total_points')
    edata.save()
    return redirect('/base_tinround')

def delete_tinround(request, pk): 
    ddata = Team_in_round.objects.get(id=pk) 
    ddata.delete() 
    return redirect('/base_tinround')

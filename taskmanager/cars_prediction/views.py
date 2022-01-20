import pickle

import pandas as pd
import sklearn
import catboost
import pandas

from django.shortcuts import render, redirect

from .forms import CarForm
from .models import Car


def user_enter(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # form.save()
            work_with_data(form)
            return redirect('prediction')

    form = CarForm()
    data = {
        'form': form,
    }
    return render(request, 'prediction/user_enter.html', data)


def prediction(request):
    file = open("predict.txt", "r")
    l = {
        'l': file.readline(),
    }
    return render(request, 'prediction/prediction.html', l)


def work_with_data(form):
    pkl_filename = "pickle_model1.pkl"
    file = open('C:/Users/Stephan/PycharmProjects/WebApp/taskmanager/cars_prediction/pickle_model.pkl', 'rb')
    pickle_model = pickle.load(file)
    # name_car = form.cleaned_data['name']
    '''enter = [
            form.cleaned_data['mark'],
            form.cleaned_data['year'],
            form.cleaned_data['mileage'],
            # form.cleaned_data['rent'],
            form.cleaned_data['box'],
            form.cleaned_data['drive'],
            form.cleaned_data['rul'],
            form.cleaned_data['condition'],
            form.cleaned_data['owners'],
            form.cleaned_data['PTS'],
            # form.cleaned_data['tamozna'],
            # form.cleaned_data['barter'],
            form.cleaned_data['V'],
            form.cleaned_data['P'],
            form.cleaned_data['toplivo'],
            # form.cleaned_data['garant'],
    ]'''
    '''
    год выпуска
    пробег
    коробка
    привод
    руль
    владельцы
    птс
    объем
    двигателя
    мощность
    топливо
    cостояние
    audi bmw chery chevrolet citroen ford geely haval honda hyundai infiniti kia land_rover lexus vaz
    не требует ремонта
    '''
    data = [form.cleaned_data['year'],
            form.cleaned_data['mileage'],
            form.cleaned_data['box'],
            form.cleaned_data['drive'],
            form.cleaned_data['rul'],
            form.cleaned_data['owners'],
            form.cleaned_data['PTS'],
            form.cleaned_data['V'],
            form.cleaned_data['P'],
            form.cleaned_data['toplivo'],
            form.cleaned_data['condition'],
            ]
    marks = "audi bmw chery chevrolet citroen ford geely haval honda hyundai infiniti kia land_rover lexus vaz".split()
    mark_d = [int(form.cleaned_data['mark'] == marks[i]) for i in range(len(marks))]
    data += mark_d
    data.append(form.cleaned_data['condition'])
    df = pd.DataFrame(data)
    df.to_csv("test.csv", sep=";")
    # score = pickle_model.score(df, [1000])
    # mms = sklearn.preprocessing.MinMaxScaler(feature_range=[0, 1000])
    #result = mms.fit_transform(df)
    # dataFrame = pd.DataFrame(result)
    value = 0
    if form.cleaned_data['mark'] in marks:
        value = pickle_model.predict(df.transpose())
        f = open("predict.txt", "w")
        f.write(str(int(value[0])))
        f.close()
    else:
        f = open("predict.txt", "w")
        f.write("Извините, мы пока не знаем такой марки.")
        f.close()
        return

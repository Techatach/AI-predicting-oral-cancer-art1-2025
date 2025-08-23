from django.shortcuts import render, HttpResponseRedirect
from joblib import load

model = load(r'D:\SP_PublicAd\AI-oral-cancer-prediction\AI-predicting-oral-cancer-using-random-forest\project\modelAI\oral_cancer_model.pkl')

def predictor(request):
    if request.method == 'POST':
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        Tobacco = request.POST['Tobacco']
        Alcohol = request.POST['Alcohol']
        HPV = request.POST['HPV']
        BetelUse = request.POST['BetelUse']
        ChronicSun = request.POST['ChronicSun']
        PoorOral = request.POST['PoorOral']
        Diet = request.POST['Diet']
        FamilyHistoryCancer = request.POST['FamilyHistoryCancer']
        CompromisedImmune = request.POST['CompromisedImmune']
        OralLesions = request.POST['OralLesions']
        Bleeding = request.POST['Bleeding']
        DifficultySwallowing = request.POST['DifficultySwallowing']
        PatchesMouth = request.POST['PatchesMouth']
        TumorSize = request.POST['TumorSize']
        CancerStage = request.POST['CancerStage']
        TreatmentType = request.POST['TreatmentType']
        SurvivalRate = request.POST['SurvivalRate']
        CostTreatment = request.POST['CostTreatment']        
        EconomicBurden = request.POST['EconomicBurden']
        EarlyDiagnosis = request.POST['EarlyDiagnosis']

        y_pred = model.predict([[Age, Gender, Tobacco, Alcohol, HPV,BetelUse, ChronicSun, PoorOral, Diet, FamilyHistoryCancer,CompromisedImmune, OralLesions, Bleeding, DifficultySwallowing, PatchesMouth, TumorSize, CancerStage, TreatmentType, SurvivalRate, CostTreatment, EconomicBurden, EarlyDiagnosis]]) 
        return render(request, 'result.html', {'result':y_pred})
    return render(request, 'form.html')
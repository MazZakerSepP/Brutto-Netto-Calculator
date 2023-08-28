print('Brutto-Nettolohnrechner 2023')
print('____________________________')
stundenlohn = float(input("Bitte gebe deinen Stundenlohn ein: ")) 
stundenzahl = float(input("Bitte gebe deine wöchentlichen Stunden ein: "))
woche  = stundenlohn * stundenzahl
monat = 4 * woche 
jahr = 12 * monat

if  jahr >= 0 and jahr <= 10908: 
    steuer = 0.944
elif  jahr >= 10909 and jahr <= 14999: 
    steuer = 0.85
elif  jahr >= 15000 and jahr <= 18999:
    steuer = 0.78
elif  jahr >= 19000 and jahr <= 24999:
    steuer = 0.745
elif jahr >= 25000 and jahr <= 29999:
    steuer = 0.726
elif jahr >= 30000 and jahr <= 34999:
    steuer = 0.706
elif jahr >= 35000 and jahr <= 39999:
    steuer = 0.687
elif jahr >= 40000 and jahr <= 44999:
    steuer = 0.668
elif jahr >= 45000 and jahr <= 49999:
    steuer = 0.649
elif jahr >= 50000 and jahr <= 54999:
    steuer = 0.629
elif jahr >= 55000 and jahr <= 58999:
    steuer = 0.61
elif jahr >= 59000 and jahr <= 62000:
    steuer = 0.595
else: 
    steuer = 0.58

round_steuer = round(( 1 - steuer) * 100, 2)
stundenlohn_netto = stundenlohn * steuer
round_stundenlohn_netto = round(stundenlohn_netto, 2)
tag_netto = woche * steuer
round_tag_netto = round(tag_netto, 2)
monat_netto = 4 * woche * steuer
round_monat_netto = round(monat_netto, 2)
jahr_netto = 12 * monat * steuer
round_jahr_netto = round(jahr_netto, 2)
print('Dein Steuersatz beträgt ca ' + str(round_steuer)  + '%')
print('Dein Stundenlohn beträgt ' + str(stundenlohn) + '€ Brutto')
print('Dein Stundenlohn beträgt ' + str(round_stundenlohn_netto) + '€ Netto')
print('Du verdienst ca ' + str(woche) + '€ pro Woche Brutto')
print('Du verdienst ca ' + str(round_tag_netto) + '€ pro Woche Netto')
print('Der Monatsverdienst beträgt ' + str(monat) + '€ Brutto')
print('Der Monatsverdienst beträgt ' + str(round_monat_netto) + '€ Netto')
print('Das macht im Jahr ca ' + str(jahr) + '€ Brutto') 
print('Das macht im Jahr ca ' + str(round_jahr_netto) + '€ Netto')
input('Zum Beenden enter drücken...')
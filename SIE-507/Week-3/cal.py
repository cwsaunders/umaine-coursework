age = float(input())
weight = float(input())
heart = int(input())
time = float(input())

cal_men = ((age*0.2017)+(weight*0.09036)+(heart*0.6309)-55.0969)*time/4.184
cal_women = ( (age * 0.074) - (weight * 0.05741) + (heart * 0.4472) - 20.4022 ) * time / 4.184

print('Women: {:.2f} calories'.format(cal_women))
print('Men: {:.2f} calories'.format(cal_men))
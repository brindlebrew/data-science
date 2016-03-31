# Import needed libraries for analysis and load data:
import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/Bryon Martinez/Documents/Data Science/analysis/nesarc_pds.csv', low_memory=False)
# sub1-6 is all for males interviewed; sub1/2 is for father alc. abuse, sub3/4 #is for mother alc. abuse,
# and sub5/6 is for both father and mother alc. abuse.
sub1 = data[(data['SEX'] == 1) & (data['S2DQ1'] == 1) & (data['S2DQ2'] == 2)]
sub2 = sub1.copy()
sub3 = data[(data['SEX'] == 1) & (data['S2DQ1'] == 2) & (data['S2DQ2'] == 1)]
sub4 = sub3.copy()
sub5 = data[(data['SEX'] == 1) & (data['S2DQ1'] == 1) & (data['S2DQ2'] == 1)]
sub6 = sub5.copy()

# sub7-12 is all for females interviewed; sub7/8 is for father alc. abuse, #sub9/10 is for mother alc. abuse,
# and sub11/12 is for both father and mother alc. abuse.
sub7 = data[(data['SEX'] == 2) & (data['S2DQ1'] == 1) & (data['S2DQ2'] == 2)]
sub8 = sub7.copy()
sub9 = data[(data['SEX'] == 2) & (data['S2DQ1'] == 2) & (data['S2DQ2'] == 1)]
sub10 = sub9.copy()
sub11 = data[(data['SEX'] == 2) & (data['S2DQ1'] == 1) & (data['S2DQ2'] == 1)]
sub12 = sub11.copy()

# Gender broken by male: sub13/14 and female: sub15/16 with no history
sub13 = data[(data['SEX'] == 1) & (data['S2DQ1'] == 2) & (data['S2DQ2'] == 2)]
sub14 = sub13.copy()
sub15 = data[(data['SEX'] == 2) & (data['S2DQ1'] == 2) & (data['S2DQ2'] == 2)]
sub16 = sub15.copy()

# Overview for men
print("No Parent History:")
print("Gender Count = ")
sex = sub14['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub14['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub14['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

print("Father History:")
print("Gender Count = ")
sex = sub2['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub2['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub2['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

print("Mother History:")
print("Gender Count = ")
sex = sub4['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub4['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub4['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

print("Father and Mother both History:")
print("Gender Count = ")
sex = sub6['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub6['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub6['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

# Overview for women
print("No Parent History:")
print("Gender Count = ")
sex = sub16['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub16['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub16['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

print("Father History:")
print("Gender Count = ")
sex = sub8['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub8['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub8['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

print("Mother History:")
print("Gender Count = ")
sex = sub10['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub10['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub10['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

print("Father and Mother both History:")
print("Gender Count = ")
sex = sub12['SEX'].value_counts(sort=False, dropna=True)
print(sex)

print("Alc. Dependence in last 12 months percent = ")
alc_ab_12_p = sub12['ALCABDEP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_12_p)

print("Alc. Dependence prior to last 12 months percent = ")
alc_ab_p12_p = sub12['ALCABDEPP12DX'].value_counts(sort=False, normalize=True, dropna=True)
print(alc_ab_p12_p)

sub2['SEX'].
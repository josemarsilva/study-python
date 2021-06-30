#
# filename   :
# Description: Iterable zip(), zip_longest(), count(), combinations()
# Docs       : * https://docs.python.org/3.9/library/itertools.html?highlight=zip#module-itertools
#

print('\n# 1. GroupBy - require data to be sorted\n')

from itertools import groupby, tee

students_grade = [
    {'name': 'Jose',    'grade': 'B'},
    {'name': 'Maria',   'grade': 'A'},
    {'name': 'Joao',    'grade': 'D'},
    {'name': 'Pedro',   'grade': 'C'},
    {'name': 'Paulo',   'grade': 'A'},
    {'name': 'Matheus', 'grade': 'B'},
    {'name': 'Isaias',  'grade': 'D'},
    {'name': 'Tiago',   'grade': 'E'},
]

print(f'students_grade: {students_grade}')
            # [{'name': 'Jose', 'grade': 'B'}, {'name': 'Maria', 'grade': 'A'}, {'name': 'Joao', 'grade': 'D'}, {'name': 'Pedro', 'grade': 'C'}, {'name': 'Paulo', 'grade': 'A'}, {'name': 'Matheus', 'grade': 'B'}, {'name': 'Isaias', 'grade': 'D'}, {'name': 'Tiago', 'grade': 'E'}]

sort_by = lambda item: item['grade']
students_grade.sort(key=sort_by)
print(f'students_grade: {students_grade}')
            # [{'name': 'Maria', 'grade': 'A'}, {'name': 'Paulo', 'grade': 'A'}, {'name': 'Jose', 'grade': 'B'}, {'name': 'Matheus', 'grade': 'B'}, {'name': 'Pedro', 'grade': 'C'}, {'name': 'Joao', 'grade': 'D'}, {'name': 'Isaias', 'grade': 'D'}, {'name': 'Tiago', 'grade': 'E'}]

for student_grade in students_grade:
    print(student_grade)

print('')
students_grade_groupby = groupby(students_grade, sort_by)
print(f'students_grade_groupby: {students_grade_groupby}')  # students_grade_groupby: <itertools.groupby object at 0x0000023EF5243A98>
for x in students_grade_groupby:
    print(f'(x[0], list(x[1])   ): ', x[0], ',', list(x[1]), ')' )
        # A , [{'name': 'Maria', 'grade': 'A'}, {'name': 'Paulo', 'grade': 'A'}] )
        # B , [{'name': 'Jose', 'grade': 'B'}, {'name': 'Matheus', 'grade': 'B'}] )
        # :

print('')
# instanciado denovo para contornar o problema do fim do iterador
students_grade_groupby = groupby(students_grade, sort_by)
print(f'students_grade_groupby: {students_grade_groupby}')  # students_grade_groupby: <itertools.groupby object at 0x0000023EF5243A98>
for groupby_key, groupby_values in students_grade_groupby:
    v1, v2 = tee(groupby_values)
    qtde = len(list(v2))
    print(f'+ {groupby_key} ({qtde}):')
    for d1 in v1:
        print(f'  - ', d1['name'])


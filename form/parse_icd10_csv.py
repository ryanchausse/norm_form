# import csv
# from models import Icd10Codes
#
# with open('codes.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#         _, created = Icd10Codes.objects.get_or_create(
#             category_code=row[0],
#             diagnosis_code=row[1],
#             full_code=row[2],
#             abbreviated_description=row[3],
#             full_description=row[4],
#             category_title=row[5]
#         )

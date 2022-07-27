from django.core.management import BaseCommand

from django.utils import timezone
from core.models.address import State,County,City,ZipCode
import csv


from django.conf import settings



class Command(BaseCommand):
    help = "Loads US postal address from CSV file."
    
    def handle(self, *args, **options):
            start_time = timezone.now()
            with open("list_addresses.csv", "r") as csv_file:
                data = list(csv.reader(csv_file, delimiter=","))

                for row in data[1:]:
                    state_obj, created = State.objects.get_or_create(name = row[0], abb=row[1])
                    county_obj, created = County.objects.get_or_create(state= state_obj, name =row[2])
                    city_obj, created = City.objects.get_or_create(state=state_obj, county=county_obj, name =row[3])
                    zipCode = ZipCode.objects.create(state = state_obj, county=county_obj, city=city_obj, zip_code=row[4])
                    
                    # record = CityStateRecord(
                    #     state = row[0],
                    #     state_abb = row[1],
                    #     county = row[2],
                    #     city = row[3],
                    #     zip_code = row[4],
                    #      )

                #     records.append(record)
                #     if len(records) > 5000:
                #         CityStateRecord.objects.bulk_create(records)
                #         records = []

                # if records:
                #     CityStateRecord.objects.bulk_create(records)
                
            end_time = timezone.now()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
                )
            )
    # A command must define handle()
    # def handle(self, *args, **options):
    #     excel_file = "list_addresses.xlsx"
    #     df = pd.read_excel(excel_file)
    #     # df1 = pd.read_excel(df, 'Sheet1')
    #     # df2 = pd.read_excel(df, 'Sheet2')
    #     engine = create_engine(database_url, echo=False)

    #     df.to_sql(CityStateRecord._meta.db_table, if_exists='replace', con=engine, index=False)
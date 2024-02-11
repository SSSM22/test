import openpyxl
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'add'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']
        try:
            workbook = openpyxl.load_workbook(excel_file_path)
            sheet = workbook.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                username, name, password= row
                User.objects.create_user(username=username, first_name=name, password=password)
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))

            self.stdout.write(self.style.SUCCESS('User creation from Excel completed'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))

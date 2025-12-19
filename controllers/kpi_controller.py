from views.kpi_view import KPIView
from models.kpi_model import KPIReportGenerator

class KPIController:
    def __init__(self, doctor_id):
        self.view = KPIView()
        self.doctor_id = doctor_id
        self.generator = KPIReportGenerator(None) # Pass main_app if needed
        self.view.generate_btn.clicked.connect(self.generate)

    def generate(self):
        start = self.view.start_date.date().toString("yyyy-MM-dd")
        end = self.view.end_date.date().toString("yyyy-MM-dd")
        data = self.generator.generate_report(self.doctor_id, start, end)
        # Logic to populate self.views.content_widget with data
        # (Move logic from KPIWindow.generate_report here)
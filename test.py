import pdfkit
import os

class PDFGenerator:
    def __init__(self, config_path):
        # إعداد مسار wkhtmltopdf
        self.config = pdfkit.configuration(wkhtmltopdf=config_path)

    def generate_pdf(self, file_name, reviewer_data, open_pdf=False):
        # محتوى HTML باستخدام البيانات المدخلة
        html_content = f"""
        <!DOCTYPE html>
        <html lang="ar">
        <head>
            <meta charset="UTF-8">
            <title>بيانات المراجع</title>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    direction: rtl;
                }}
            </style>
        </head>
        <body>
            <h1>معلومات المراجع</h1>
            <p>الأسم: {reviewer_data['الأسم']}</p>
            <p>الوظيفة: {reviewer_data['الوظيفة']}</p>
            <p>رقم الهوية: {reviewer_data['رقم الهوية']}</p>
            <p>تاريخ وجهة الاصدار: {reviewer_data['تاريخ وجهة الاصدار']}</p>
            <p>صفة المراجعة: {reviewer_data['صفة المراجعة']}</p>
            <p>جهة المراجعة: {reviewer_data['جهة المراجعة']}</p>
            <p>وقت الحفظ: {reviewer_data['وقت الحفظ']}</p>
            <p>البحث: {reviewer_data['البحث']}</p>
        </body>
        </html>
        """

        # خيارات إنشاء PDF
        options = {
            'no-stop-slow-scripts': '',
            'debug-javascript': '',
            'disable-smart-shrinking': '',
            'enable-local-file-access': '',
            'zoom': '1.3',
            'disable-javascript': '',
        }

        # توليد PDF
        try:
            pdfkit.from_string(html_content, file_name, configuration=self.config, options=options)
            print("PDF created successfully.")
            
            # فتح PDF تلقائيًا إذا تم تحديد ذلك
            if open_pdf:
                self.open_pdf(file_name)
        except Exception as e:
            print("An error occurred while creating the PDF:", e)

    @staticmethod
    def open_pdf(file_name):
        # فتح ملف PDF تلقائيًا
        os.startfile(file_name)  # يعمل على Windows فقط
        # إذا كنت تستخدم نظام Linux أو macOS، استخدم:
        # os.system(f'xdg-open {file_name}')  # على Linux
        # os.system(f'open {file_name}')      # على macOS

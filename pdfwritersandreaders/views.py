from django.shortcuts import render
from django.http import HttpResponse
from pdfwritersandreaders.core.business.abstracts.PdfGeneratorService import PdfGeneratorService
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics import renderPDF

# Create your views here.
pdfGeneratorService = PdfGeneratorService()

def generate_report(request):
    gv = None
    ctx = {
        "power_energy_update_interval":gv.power_energy_update_interval,
        "comparison_graph_update_interval":gv.comparison_graph_update_interval,
        "hourly_update_interval":gv.hourly_update_interval
    }
    if request.is_ajax():
        if request.POST.has_key('start_date'):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{request.POST.data.get("filename")}.pdf"'
            p = Canvas(response)
            p.drawString(100, 100, "Hello World.")
            p.showPage()
            p.save()
            return response
    return render(request, 'generate_report/reports.html', ctx)

def send_data_pdf(request):
    drawing = Canvas(response)
    drawing.drawString(100, 100, "Hello World.")
    drawing.showPage()
    drawing.save()
    data = request.query_params.get('data')
    page = renderPDF.drawToFile(drawing, 'example.pdf', data)
    return HttpResponse(page, mimetype='application/pdf')

def invoice_to_response(request, invoice):
    response = HttpResponse(mimetype='application/pdf')
    p = Canvas(response, pagesize='A4', pageCompression=0)
    p.showPage()
    p.save()
    return response

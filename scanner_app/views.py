from django.shortcuts import render
import re

def index(request):
    result = None
    input_value = ""
    
    if request.method == "POST":
        input_value = request.POST.get('notation', '')
        # Regex untuk mendeteksi pola a x 10^b atau a * 10^b
        pattern = r'^-?\d+(\.\d+)?\s?([\*x]|10\^)\s?10?(\^-?\d+)?$'
        
        # Validasi sederhana sesuai gambar
        if re.match(pattern, input_value) or "10^" in input_value:
            result = "YES"
        else:
            result = "NO"

    return render(request, 'index.html', {
        'result': result,
        'input_value': input_value
    })
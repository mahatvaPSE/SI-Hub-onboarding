import json
import datetime
import pytz
import requests
from termial import fetchTerminal
import openpyxl

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cnpwX2xpdmVfMVdiMm83MnQxWGkzRXU6YWhHcGhibjdnbGlQM0hDQkllWG1DQndy',
}
#AX2wVoVjNOyzQ3
loca = '/Users/mahatva.garg/Downloads/sihub.xlsx'
wb = openpyxl.load_workbook(loca)
ws1 = wb['Sheet1']
ws2 = wb['Sheet2']
master = 1
for x in range(2,10):
    terminals = []
    cell = 'A' + str(x)
    cell = ws1[cell]
    mid = cell.value

    cell = 'B' + str(x)
    cell = ws1[cell]
    if cell.value:
        terminals.append(cell.value)
        print(cell.value)
    else:
        terminals = fetchTerminal(mid)
        print(terminals)
        cell = 'B' + str(x)
        cell = ws1[cell]
    ap = ''
    for a in range(len(terminals)):
        ap = ap + terminals[a] + " "
    cell.value = str(ap)
    wb.save(loca)
    for term in terminals:
        json_data = {
            'merchant_id': mid,
            'terminal_id': term,
        }
        cell = 'A' + str(master)
        cell = ws2[cell]
        cell.value = mid
        wb.save(loca)
        cell = 'B' + str(master)
        cell = ws2[cell]
        combined_string = f"Merchant ID: {json_data['merchant_id']}, Terminal ID: {json_data['terminal_id']}"
        cell.value = combined_string
        wb.save(loca)

        response = requests.post('https://api-dark.razorpay.com/v1/sihub_merchant_onboard', headers=headers, json=json_data)
        print(response.text)
        if response.text[2:7] == 'error':
            cell = 'C' + str(x)
            cell = ws1[cell]
            cell.value = 'error'
            wb.save(loca)
        else:
            cell = 'C' + str(x)
            cell = ws1[cell]
            cell.value = 'Done'
            wb.save(loca)

        cell = 'C' + str(master)
        cell = ws2[cell]
        json_string = json.dumps(response.text)
        cell.value = json_string
        wb.save(loca)

        cell = 'D' + str(master)
        cell = ws2[cell]
        current_time_utc = datetime.datetime.now(pytz.utc)
        ist_timezone = pytz.timezone("Asia/Kolkata")
        current_time_ist = current_time_utc.astimezone(ist_timezone)
        timestamp_str_ist = current_time_ist.strftime("%Y-%m-%d %H:%M:%S %Z")
        cell.value = timestamp_str_ist
        wb.save(loca)

        master +=1
    terminals = []

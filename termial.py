import requests

url = 'https://admin-dashboard.razorpay.com/admin/api/live/admin/terminal'

headers = {
    'authority': 'admin-dashboard.razorpay.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'PHPSESSID=0cae77fd2af86d1b0460e4eb42fc5317; rzp_api_host=https://api-dark.razorpay.com/v1/; hubspotutk=a64ea6896288f2f84e644de6189e09c1; __hssrc=1; _fbp=fb.1.1698338934318.1786763674; ab_user_id=06873421-7646-462d-b0d5-80c0f66572ac; additional-cache-params={"isMobile":false,"isSafari":false,"countryCode":"IN","isTransparentVideoNotSupported":false,"isBot":false,"host":"razorpay.com","previewAsset":""}; visit_time_stamp=1698389655014; _ga=GA1.1.1719735211.1698389656; _gcl_au=1.1.1607218711.1698389656; firstAttribUtm={"source":"google","medium":"organic"}; lastAttribUtm={"utm_source":"google","utm_medium":"organic"}; clientId=8b6c792d-5e35-4a17-a99b-ece394de068e; isLandingPageUser=true; ajs_user_id=M9gmEmiDvoYaD1; ajs_anonymous_id=ea642756-711b-4c75-9d32-3d6eabfd3969; _hjSessionUser_575141=eyJpZCI6Ijg1YjFmZDFmLWEzY2UtNWVjNi05ZTA1LTBkM2E4YWNjN2ZjYyIsImNyZWF0ZWQiOjE2OTg3MjUwNDkzODgsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1xzil8m|2|fgd|0|1393; commonSessionId=e0c5-dd68-9d61-c0e5; campaignStartTime=Thu%2C%2002%20Nov%202023%2005%3A07%3A49%20GMT; rzp_utm={"attributions":[{"utm_source":"google","utm_campaign":"","utm_medium":"organic","utm_term":"","utm_content":"","utm_adgroup":"","timestamp":"2023-10-27T12:24:16+05:30"},{"utm_source":"google","utm_campaign":"","utm_medium":"organic","utm_term":"","utm_content":"","utm_adgroup":"","timestamp":"2023-11-02T10:37:49%2B05:30"}],"website":"razorpay.com/upi-autopay/","first_page":"razorpay.com/upi-autopay/","final_page":"razorpay.com/upi-autopay/","new_user":false,"fc_source":"google","lc_source":"google"}; cto_bundle=aJFE-l9kYlBiSXVEd1FDY2Z1THZTclElMkZ5clE5M3l5RjNaODVuc09vNWlhbmRjMldPUVlObGJmQ01WbTJ5Z29CWXd0ayUyQmtLJTJGd2Zyd05VUkE4Q1NZQ3RabFQ5YyUyQlZLTjY3aHFkeXJTRHZ5enNQUVhGa2oxcUR5cGZnYiUyQjFhRUw2N1M5TGJ1UiUyQkd3RGhuSDZoTlZ5elQ0QyUyRjVIRkZxNVJCMUhiOTBTVDExWGZVaGE2WkJ4MTd1ZTdQa3pOZ1JoaVdUMTA0TzAlMkZWQUUxWVJGV2xyVXU0USUyRml6JTJCTEElM0QlM0Q; _uetsid=c714da80793d11eebf7f711a169d59c7; _uetvid=08a9e10055d411ee9b8af97e734574a8; _rdt_uuid=1698901674065.e40962b7-06c0-44b5-80bc-577fa252e1d6; _ga_F42RZ69DW8=GS1.1.1698901668.3.1.1698901694.34.0.0; _clsk=16ujdgs|1698909897323|2|1|b.clarity.ms/collect; _ga_8HTFJ5WZ20=GS1.1.1698909904.12.0.1698909904.0.0.0; rzp_usr_session=oTZm1kvhUJeDvoIxCbu3yCgkrmY5iFp0Kolgwr4C; __hstc=227020674.a64ea6896288f2f84e644de6189e09c1.1698338933811.1698923692882.1698979376306.18; __hssc=227020674.1.1698979376306; XSRF-TOKEN=eyJpdiI6IjBLeVB6ZHlYNDE2Y2NQYmxuYk4ySXc9PSIsInZhbHVlIjoianR4U0JhOS9JVG9ZWUdYZ1EvSkVHbURQK2d2WlM0RnlsaFFLMHRpN2Y3cFR5ZUtKaGRWT2JKcDNtbzBFdnFRSUliR0pLMUY2ZFR6bU9MVEpPajhFNHFYbUl5eFZTbHdYTWpMTVIxWHhIWHJvYXdWY0FBMGFDOFRwMVY4dzlXV1MiLCJtYWMiOiJhY2M0Y2JhNTM4MDZkYjdlMGRmM2I1YTQzMGIzM2IwZjUwY2YyNTY3MjczMGM1ZDQzOTA5ZjZiZDIwOGM2NWQ5IiwidGFnIjoiIn0%3D',
    'referer': 'https://admin-dashboard.razorpay.com/admin/entities/live/terminal?merchant_id=IRvvzGVJMxGg8v',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-xsrf-token': 'eyJpdiI6ImZCejV1VzBQL2hLNEI5eEREYmlXdlE9PSIsInZhbHVlIjoidWVnQzNKVXI0NnVyYTk5OFpIaFdleEtaZG9RNEFQeE9aclFoTWZTT1NoMmNGQTcvU3E0eHROZFNFa1BMY0ZlMEpiUUdLc3JMTE5PaU5WVHZIREpuOFFjak45eVRLMHZvK1UwUHVyOG0wb3YxMENPblBxU2Y3R2R4Ris5eVBzc08iLCJtYWMiOiJjNWY0N2UyOTExMGQzMGQ3NmNiMzU0NzFlNjYwNDdiZGRjZWI4MDhiZWViZDI5MDM2ZmUwYjBhYzI1OWVhYTU1IiwidGFnIjoiIn0=',
}
finalTerminals = []
def fetchTerminal(mid):
    finalTerminals = []
    params = {
    'count': 1000,
    'skip': 0,
    'merchant_id': mid,
    'gateway': 'hitachi'
}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        items = data.get('data', {}).get('items', [])

        for item in items:
            currencies = item.get('currency', [])

            if 'INR' in currencies:
                terminal_id = item.get('id')
                finalTerminals.append(terminal_id[5:])
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
    return finalTerminals
# print(fetchTerminal('FESrjk0EtuPZuQ'))


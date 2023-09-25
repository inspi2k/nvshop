import sys
import requests
import urllib.request
import json
import pyautogui

# 1. 검색할 상품 정보 찾기 - MID 추출, keyword 얻기
default_mid = ""

default_store = ""
default_product = ""

default_keyword = ""

get_mid = ""

check_mid = pyautogui.confirm("상품의 MID를 알고계십니까?", "상품 순위 찾기 (Step 1)")
if check_mid == "OK":
    get_mid = pyautogui.prompt("상품의 MID를 입력하세요", "상품 순위 찾기 (Step 2)", default=default_mid)
    if get_mid == "" or get_mid == None:
        pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
        sys.exit(1)
    get_mid = get_mid.strip()
    print("input mid={}".format(get_mid))

elif check_mid == "Cancel":
    get_store = pyautogui.prompt("스토어명을 입력하세요", "상품 순위 찾기 (Step 2-1)", default=default_store)
    if get_store == "" or get_store == None:
        pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
        sys.exit(1)
    get_store = get_store.strip()

    get_product = pyautogui.prompt("상품명을 입력하세요", "상품 순위 찾기 (Step 2-2)", default=default_product)
    if get_product == "" or get_product == None :
        pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
        sys.exit(1)
    get_product = get_product.strip()

    pageIndex = 1
    pageSize = 100
    encText = urllib.parse.quote(get_store)

    headers = {
        'authority': 'search.shopping.naver.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'NNB=XFAKOM3FWBEGG; ASID=3d63aeda00000183d9845de40000005f; autocomplete=use; AD_SHP_BID=18; _ga=GA1.2.1834935952.1667395532; SHP_BUCKET_ID=3; NSCS=1; nid_inf=-1414768515; NID_JKL=FicUSGqv2v1SQhZ86S5KYd02RYYknV1144+ObRT4k5s=; NID_AUT=tClj21DEE4vFWK+w9nNPBu3hDbKtmXdnCP2c/6SJT4dEOkjDxncwG3QryGaHXvNa; nx_ssl=2; _naver_usersession_=zDgBtoiR/jwCgOD7eSV4Yg==; NID_SES=AAABpZRkmxvTsNch089VjaxNIHFLfSw7p10oQTZD55oDBDLmwpK7widsK9FvMAV7MJlib1L/qCeWtdwZYk6MACz2BK2ClK7b2kRGMx6yvK0alZfbyv4Lsqp9VpmBPj0DlnGC5mYZ8/U9FSI+3k6BNf14Yni8d399yEBgMDSSbfbVWk13Ga5ZRBnVlBrCTmZYRPYqllalcsDWYNUUiGvd1jhlCAG/r0EXgZLxK9rspFkJXgMKkSAxmXT2AMeSVVkmhjz6arTrZf/1NGaQINrF4I4ttI0xjRyjd2SX905tXmgBP3ROzlTPPaGDeO0JI7RtEe99zg1rhisCNBJnMBJ9EUswOBMfvm3gmps5CxhBjNSzjToFA7j02qPU5IdYBoPqOPXs1/KDc5rZxuiC/It3gRwA7gPnbEFwYq3AvNr4UxlLHTEFskGpikQkEaZfyF+pwq1Mq2ePM8ZRpQxFlhBIhFx438b59q04mwMKhjKSfKzVtdAYGU8b4JSj3zpVtlPNX4GaAer9eipSQw1319GVneOR79yRpUL938biXG05hP7CY0hs3LrICbQ88uDAoe/XplY2MA==; page_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147; spage_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147',
        'dnt': '1',
        'logic': 'PART',
        'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery='+encText+'&pagingIndex='+str(pageIndex)+'&pagingSize='+str(pageSize)+'&productSet=total&query='+encText+'&sort=rel&timestamp=&viewType=list',
        'sbth': '6bc7553b8fa3e04779448fd212e42bb46f18162e3d9873ba0d1b41409eae93a803b742c0cb6bfdbfc7737fc581f7e8eb',
        'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
        'sec-ch-ua-arch': '"arm"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Whale";v="3.21.192.22", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"13.6.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.22 Safari/537.36',
    }

    params = {
    'eq': '',
    'frm': 'NVSHATC',
    'iq': '',
    'origQuery': get_store,
    'pagingIndex': str(pageIndex),
    'pagingSize': str(pageSize),
    'productSet': 'total',
    'query': get_store,
    'sort': 'rel',
    'viewType': 'list',
    'xq': '',
    }

    response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, headers=headers)

    items = json.loads(response.text)
    # items['shoppingResult']['products']

    print("{}'s product '{}' total={}".format(get_store, get_product, format(int(items['shoppingResult']['total']),",")))
    if items['shoppingResult']['total'] < 1:
        get_mid = ""
        print("can't searching")
        sys.exit(0)
    else:
        # print(len(items['shoppingResult']['products']))
        for item in items['shoppingResult']['products']:
            if get_product in item['productTitle']:
                get_mid = item['id']
                print("mid={}, {}/{}".format(get_mid, item['rank'], items['shoppingResult']['total']))

if get_mid == "":
    print("no mid!")
    sys.exit(1)

print("https://search.shopping.naver.com/gate.nhn?id={}".format(get_mid))

# 2. keyword 순위를 가져와서 mid와 일치하는 순위(rank) 찾기
get_keyword = pyautogui.prompt("키워드를 입력하세요", "상품 순위 찾기 (Step 3)", default=default_keyword)
if get_keyword == "" or get_keyword == None :
    pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
    sys.exit(1)
get_keyword = get_keyword.strip()

pageIndex = 1
pageSize = 40
encText = urllib.parse.quote(get_keyword)
got_it = False

while got_it == False:

    headers = {
            'authority': 'search.shopping.naver.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'NNB=XFAKOM3FWBEGG; ASID=3d63aeda00000183d9845de40000005f; autocomplete=use; AD_SHP_BID=18; _ga=GA1.2.1834935952.1667395532; SHP_BUCKET_ID=3; NSCS=1; nid_inf=-1414768515; NID_JKL=FicUSGqv2v1SQhZ86S5KYd02RYYknV1144+ObRT4k5s=; NID_AUT=tClj21DEE4vFWK+w9nNPBu3hDbKtmXdnCP2c/6SJT4dEOkjDxncwG3QryGaHXvNa; nx_ssl=2; _naver_usersession_=zDgBtoiR/jwCgOD7eSV4Yg==; NID_SES=AAABpZRkmxvTsNch089VjaxNIHFLfSw7p10oQTZD55oDBDLmwpK7widsK9FvMAV7MJlib1L/qCeWtdwZYk6MACz2BK2ClK7b2kRGMx6yvK0alZfbyv4Lsqp9VpmBPj0DlnGC5mYZ8/U9FSI+3k6BNf14Yni8d399yEBgMDSSbfbVWk13Ga5ZRBnVlBrCTmZYRPYqllalcsDWYNUUiGvd1jhlCAG/r0EXgZLxK9rspFkJXgMKkSAxmXT2AMeSVVkmhjz6arTrZf/1NGaQINrF4I4ttI0xjRyjd2SX905tXmgBP3ROzlTPPaGDeO0JI7RtEe99zg1rhisCNBJnMBJ9EUswOBMfvm3gmps5CxhBjNSzjToFA7j02qPU5IdYBoPqOPXs1/KDc5rZxuiC/It3gRwA7gPnbEFwYq3AvNr4UxlLHTEFskGpikQkEaZfyF+pwq1Mq2ePM8ZRpQxFlhBIhFx438b59q04mwMKhjKSfKzVtdAYGU8b4JSj3zpVtlPNX4GaAer9eipSQw1319GVneOR79yRpUL938biXG05hP7CY0hs3LrICbQ88uDAoe/XplY2MA==; page_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147; spage_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147',
            'dnt': '1',
            'logic': 'PART',
            'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery='+encText+'&pagingIndex='+str(pageIndex)+'&pagingSize='+str(pageSize)+'&productSet=total&query='+encText+'&sort=rel&timestamp=&viewType=list',
            'sbth': '6bc7553b8fa3e04779448fd212e42bb46f18162e3d9873ba0d1b41409eae93a803b742c0cb6bfdbfc7737fc581f7e8eb',
            'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
            'sec-ch-ua-arch': '"arm"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version-list': '"Whale";v="3.21.192.22", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '"13.6.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.22 Safari/537.36',
        }

    params = {
    'eq': '',
    'frm': 'NVSHATC',
    'iq': '',
    'origQuery': get_keyword,
    'pagingIndex': str(pageIndex),
    'pagingSize': str(pageSize),
    'productSet': 'total',
    'query': get_keyword,
    'sort': 'rel',
    'viewType': 'list',
    'xq': '',
    }

    response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, headers=headers)

    items = json.loads(response.text)
    # items['shoppingResult']['products']

    if pageIndex == 1:
        print("{}'s total={}".format(get_keyword, format(int(items['shoppingResult']['total']),",")))

    print(".", end="", flush=True)
    if pageIndex % 10 == 0: print("")

    if items['shoppingResult']['total'] < 1:
        get_mid = ""
        print("\nCan't Searching\nPlease retry - {}".format(get_keyword))
        sys.exit(0)
    else:
        for item in items['shoppingResult']['products']:
            if get_mid == item['id']:
                print("\nmid({})'s rank is {:3>}".format(get_mid, format(int(item['rank']),",")),end="")
                print(" ({:3>}p {:>2})".format(pageIndex, (int(item['rank'])-1)%pageSize+1))
                print(item['crUrl'])
                got_it = True
                break
        pageIndex += 1
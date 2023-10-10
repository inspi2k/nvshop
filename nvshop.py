import sys
import math
import requests
import urllib.request
import json
import pyautogui


# 0. 검색할 상품 정보 찾기 위해 MID 추출, keyword 얻기
default_store = "FOL."
default_product = "FOL 보카 여성 청결제"

default_mid = "86868741371"

default_keyword = "여성청결제"

get_mid = ""
result = "\n"

# 1-1. 입력값 받기 (mide / storename, title)
check_mid = pyautogui.confirm("상품의 MID를 알고계십니까?", "상품 순위 찾기 (Step 1)")
if check_mid == "OK":
    get_mid = pyautogui.prompt(
        "상품의 MID를 입력하세요", "상품 순위 찾기 (Step 2)", default=default_mid
    )
    if get_mid == "" or get_mid == None:
        pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
        sys.exit(1)
    get_mid = get_mid.strip()
    print("input mid={}".format(get_mid))

elif check_mid == "Cancel":
    get_store = pyautogui.prompt(
        "스토어명을 입력하세요", "상품 순위 찾기 (Step 2-1)", default=default_store
    )
    if get_store == "" or get_store == None:
        pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
        sys.exit(1)
    get_store = get_store.strip()

    get_product = pyautogui.prompt(
        "상품명을 입력하세요", "상품 순위 찾기 (Step 2-2)", default=default_product
    )
    if get_product == "" or get_product == None:
        pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
        sys.exit(1)
    get_product = get_product.strip()

    # 1-2. storename 의 type 조회
    pageIndex = 1
    pageSize = 40
    encText = urllib.parse.quote(get_store)

    headers = {
        "authority": "search.shopping.naver.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        # 'cookie': 'NNB=XFAKOM3FWBEGG; ASID=3d63aeda00000183d9845de40000005f; autocomplete=use; AD_SHP_BID=18; _ga=GA1.2.1834935952.1667395532; SHP_BUCKET_ID=3; NSCS=1; nid_inf=-1414768515; NID_JKL=FicUSGqv2v1SQhZ86S5KYd02RYYknV1144+ObRT4k5s=; NID_AUT=tClj21DEE4vFWK+w9nNPBu3hDbKtmXdnCP2c/6SJT4dEOkjDxncwG3QryGaHXvNa; nx_ssl=2; _naver_usersession_=zDgBtoiR/jwCgOD7eSV4Yg==; NID_SES=AAABpZRkmxvTsNch089VjaxNIHFLfSw7p10oQTZD55oDBDLmwpK7widsK9FvMAV7MJlib1L/qCeWtdwZYk6MACz2BK2ClK7b2kRGMx6yvK0alZfbyv4Lsqp9VpmBPj0DlnGC5mYZ8/U9FSI+3k6BNf14Yni8d399yEBgMDSSbfbVWk13Ga5ZRBnVlBrCTmZYRPYqllalcsDWYNUUiGvd1jhlCAG/r0EXgZLxK9rspFkJXgMKkSAxmXT2AMeSVVkmhjz6arTrZf/1NGaQINrF4I4ttI0xjRyjd2SX905tXmgBP3ROzlTPPaGDeO0JI7RtEe99zg1rhisCNBJnMBJ9EUswOBMfvm3gmps5CxhBjNSzjToFA7j02qPU5IdYBoPqOPXs1/KDc5rZxuiC/It3gRwA7gPnbEFwYq3AvNr4UxlLHTEFskGpikQkEaZfyF+pwq1Mq2ePM8ZRpQxFlhBIhFx438b59q04mwMKhjKSfKzVtdAYGU8b4JSj3zpVtlPNX4GaAer9eipSQw1319GVneOR79yRpUL938biXG05hP7CY0hs3LrICbQ88uDAoe/XplY2MA==; page_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147; spage_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147',
        "dnt": "1",
        "logic": "PART",
        "referer": "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery="
        + encText
        + "&pagingIndex="
        + str(pageIndex)
        + "&pagingSize="
        + str(pageSize)
        + "&productSet=total&query="
        + encText
        + "&sort=date&timestamp=&viewType=list",
        "sbth": "6bc7553b8fa3e04779448fd212e42bb46f18162e3d9873ba0d1b41409eae93a803b742c0cb6bfdbfc7737fc581f7e8eb",
        "sec-ch-ua": '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
        "sec-ch-ua-arch": '"arm"',
        "sec-ch-ua-bitness": '"64"',
        "sec-ch-ua-full-version-list": '"Whale";v="3.21.192.22", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"macOS"',
        "sec-ch-ua-platform-version": '"13.6.0"',
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.22 Safari/537.36",
    }

    params = {
        "eq": "",
        "frm": "NVSHATC",
        "iq": "",
        "origQuery": get_store,
        "pagingIndex": str(pageIndex),
        "pagingSize": str(pageSize),
        "productSet": "total",
        "query": get_store,
        "sort": "date",
        "viewType": "list",
        "xq": "",
    }

    response = requests.get(
        "https://search.shopping.naver.com/api/search/all",
        params=params,
        headers=headers,
    )

    items = json.loads(response.text)

    msg = "storename = {}\nstopwordQuery = {}\nstrQueryType = {}".format(
        items["shoppingResult"]["query"],
        items["shoppingResult"]["stopwordQuery"],
        items["shoppingResult"]["strQueryType"],
    )
    result += "storename = {}".format(items["shoppingResult"]["query"]) + "\n"
    print(msg)

    if len(items["shoppingResult"]["nluTerms"]) > 0:
        print("")
        result += "\n"
        for i, r in enumerate(items["shoppingResult"]["nluTerms"]):
            # print(r)
            # msg = f'{i}={r}'
            msg = f"{r['keyword']}'s type = {r['type']}"
            result += msg + "\n"
            print(msg)

    if items["shoppingResult"]["total"] < 1:
        get_mid = ""
        print("can't searching")
        pyautogui.alert(result + "\n\n" + "can't searhing")
        sys.exit(0)
    else:
        # 1-3. MID값 찾기
        print("")
        msg = "store = {}'s total={}".format(
            get_store, format(int(items["shoppingResult"]["total"]), ",")
        )
        result += "\n" + msg + "\n"
        print(msg)

        # print(len(items['shoppingResult']['products']))
        for item in items["shoppingResult"]["products"]:
            if get_product in item["productTitle"]:
                get_mid = item["id"]
                msg = "{} product's mid = {}, {}/{}".format(
                    get_product, get_mid, item["rank"], items["shoppingResult"]["total"]
                )
                result += msg + "\n\n"
                print(msg)

if get_mid == "":
    print("no mid!")
    pyautogui.alert(result + "\n\n" + "no mid!")
    sys.exit(0)

# print("https://search.shopping.naver.com/gate.nhn?id={}".format(get_mid))

# 2-1. 입력값 받기 - (keyword)
get_keyword = pyautogui.prompt(
    "키워드를 입력하세요", "상품 순위 찾기 (Step 3)", default=default_keyword
)
if get_keyword == "" or get_keyword == None:
    pyautogui.alert("정상적인 입력으로 다시 시도해주세요")
    sys.exit(1)
get_keyword = get_keyword.strip()

# 2-2. 순위를 가져와서 mid와 일치하는 순위(rank) 찾기
pageIndex = 1
pageSize = 40
encText = urllib.parse.quote(get_keyword)
got_it = False

while got_it == False:
    headers = {
        "authority": "search.shopping.naver.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        # 'cookie': 'NNB=XFAKOM3FWBEGG; ASID=3d63aeda00000183d9845de40000005f; autocomplete=use; AD_SHP_BID=18; _ga=GA1.2.1834935952.1667395532; SHP_BUCKET_ID=3; NSCS=1; nid_inf=-1414768515; NID_JKL=FicUSGqv2v1SQhZ86S5KYd02RYYknV1144+ObRT4k5s=; NID_AUT=tClj21DEE4vFWK+w9nNPBu3hDbKtmXdnCP2c/6SJT4dEOkjDxncwG3QryGaHXvNa; nx_ssl=2; _naver_usersession_=zDgBtoiR/jwCgOD7eSV4Yg==; NID_SES=AAABpZRkmxvTsNch089VjaxNIHFLfSw7p10oQTZD55oDBDLmwpK7widsK9FvMAV7MJlib1L/qCeWtdwZYk6MACz2BK2ClK7b2kRGMx6yvK0alZfbyv4Lsqp9VpmBPj0DlnGC5mYZ8/U9FSI+3k6BNf14Yni8d399yEBgMDSSbfbVWk13Ga5ZRBnVlBrCTmZYRPYqllalcsDWYNUUiGvd1jhlCAG/r0EXgZLxK9rspFkJXgMKkSAxmXT2AMeSVVkmhjz6arTrZf/1NGaQINrF4I4ttI0xjRyjd2SX905tXmgBP3ROzlTPPaGDeO0JI7RtEe99zg1rhisCNBJnMBJ9EUswOBMfvm3gmps5CxhBjNSzjToFA7j02qPU5IdYBoPqOPXs1/KDc5rZxuiC/It3gRwA7gPnbEFwYq3AvNr4UxlLHTEFskGpikQkEaZfyF+pwq1Mq2ePM8ZRpQxFlhBIhFx438b59q04mwMKhjKSfKzVtdAYGU8b4JSj3zpVtlPNX4GaAer9eipSQw1319GVneOR79yRpUL938biXG05hP7CY0hs3LrICbQ88uDAoe/XplY2MA==; page_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147; spage_uid=ieavrlp0Jy0ssl5A4Jwsssssths-304147',
        "dnt": "1",
        "logic": "PART",
        "referer": "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery="
        + encText
        + "&pagingIndex="
        + str(pageIndex)
        + "&pagingSize="
        + str(pageSize)
        + "&productSet=total&query="
        + encText
        + "&sort=rel&timestamp=&viewType=list",
        "sbth": "6bc7553b8fa3e04779448fd212e42bb46f18162e3d9873ba0d1b41409eae93a803b742c0cb6bfdbfc7737fc581f7e8eb",
        "sec-ch-ua": '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="114"',
        "sec-ch-ua-arch": '"arm"',
        "sec-ch-ua-bitness": '"64"',
        "sec-ch-ua-full-version-list": '"Whale";v="3.21.192.22", "Not-A.Brand";v="8.0.0.0", "Chromium";v="114.0.5735.138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"macOS"',
        "sec-ch-ua-platform-version": '"13.6.0"',
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.22 Safari/537.36",
    }

    params = {
        "eq": "",
        "frm": "NVSHATC",
        "iq": "",
        "origQuery": get_keyword,
        "pagingIndex": str(pageIndex),
        "pagingSize": str(pageSize),
        "productSet": "total",
        "query": get_keyword,
        "sort": "rel",
        "viewType": "list",
        "xq": "",
    }

    response = requests.get(
        "https://search.shopping.naver.com/api/search/all",
        params=params,
        headers=headers,
    )

    items = json.loads(response.text)
    # items['shoppingResult']['products']

    if pageIndex == 1:
        print("")
        msg = "keyword = {}'s total = {} ({})".format(
            get_keyword, format(int(items["shoppingResult"]["total"]), ","), format(math.ceil(int(items["shoppingResult"]["total"])/40), ",")
        )
        result += msg + "\n"
        print(msg)

    print(".", end="", flush=True)
    if pageIndex % 10 == 0:
        print("({}p)".format(pageIndex), flush=True)

    if items["shoppingResult"]["total"] < 1:
        get_mid = ""
        print("\nCan't Searching\nPlease retry - {}".format(get_keyword))
        pyautogui.alert(result + "\n\n" + "can't searching!")
        sys.exit(0)
    else:
        for item in items["shoppingResult"]["products"]:
            if get_mid == item["id"]:
                print("")
                msg = "{}-mid's rank is {:3>} ({:3>}p {:>2})\n title is '{}'".format(
                    get_mid, 
                    format(
                        int(item["rank"]),
                        ",",
                    ),
                    pageIndex,
                    (int(item["rank"]) - 1) % pageSize + 1,
                    item["productTitle"],
                )
                result += msg + "\n\n"
                print(msg)
                print("")
                print(item["crUrl"])
                got_it = True
                break
        pageIndex += 1

# 3. 결과값 (window) 출력
pyautogui.alert('\n'+result)

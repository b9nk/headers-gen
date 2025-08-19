# @cleanest in discord for help

import random
import json
from concurrent.futures import ThreadPoolExecutor

os_data = {
    'windows': {
        'versions': ['10.0', '11.0'],
        'archs': ['Win64; x64', 'WOW64']
    },
    'mac': {
        'versions': ['10_15_7', '11_7_10', '12_7_2', '13_6_3', '14_2_1']
    },
    'linux': {
        'distros': ['X11; Linux x86_64', 'X11; Ubuntu; Linux x86_64', 'X11; Linux i686']
    },
    'mobile': {
        'ios': ['15_7', '16_7_5', '17_2_1', '17_3', '17_4'],
        'android': ['10', '11', '12', '13', '14'],
        'devices': ['SM-G991B', 'SM-G996B', 'SM-G998B', 'Pixel 6', 'Pixel 7']
    }
}

browsers = {
    'chrome': {
        'versions': list(range(115, 125)),
        'webkit': list(range(537, 540)),
        'safari': list(range(537, 540))
    },
    'firefox': {
        'versions': list(range(115, 125))
    },
    'safari': {
        'versions': ['16.6', '17.0', '17.1', '17.2', '17.3'],
        'webkit': ['605.1.15', '605.1.16', '605.1.17']
    },
    'edge': {
        'versions': list(range(115, 125))
    }
}

lg = [
    'en-US,en;q=0.9', 'en-GB,en;q=0.8', 'es-ES,es;q=0.9,en;q=0.8',
    'fr-FR,fr;q=0.9,en;q=0.8', 'de-DE,de;q=0.9,en;q=0.8', 'pt-BR,pt;q=0.9,en;q=0.8'
]

en = ['gzip, deflate, br', 'gzip, deflate', 'br, gzip, deflate']
cc = ['keep-alive', 'close']
ca = ['no-cache', 'max-age=0', 'no-store']

def gu():
    browser = random.choice(['chrome', 'firefox', 'safari', 'edge'])
    os_type = random.choice(['windows', 'mac', 'linux'])
    
    if browser == 'chrome':
        version = random.choice(browsers['chrome']['versions'])
        webkit = random.choice(browsers['chrome']['webkit'])
        safari = random.choice(browsers['chrome']['safari'])
        patch = random.randint(0, 9999)
        
        if os_type == 'windows':
            os_ver = random.choice(os_data['windows']['versions'])
            arch = random.choice(os_data['windows']['archs'])
            return f"Mozilla/5.0 (Windows NT {os_ver}; {arch}) AppleWebKit/{webkit}.36 (KHTML, like Gecko) Chrome/{version}.0.0.{patch} Safari/{safari}.36"
        elif os_type == 'mac':
            os_ver = random.choice(os_data['mac']['versions'])
            return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {os_ver}) AppleWebKit/{webkit}.36 (KHTML, like Gecko) Chrome/{version}.0.0.{patch} Safari/{safari}.36"
        else:
            distro = random.choice(os_data['linux']['distros'])
            return f"Mozilla/5.0 ({distro}) AppleWebKit/{webkit}.36 (KHTML, like Gecko) Chrome/{version}.0.0.{patch} Safari/{safari}.36"
    
    elif browser == 'firefox':
        version = random.choice(browsers['firefox']['versions'])
        if os_type == 'windows':
            os_ver = random.choice(os_data['windows']['versions'])
            arch = random.choice(os_data['windows']['archs'])
            return f"Mozilla/5.0 (Windows NT {os_ver}; {arch}; rv:{version}.0) Gecko/20100101 Firefox/{version}.0"
        elif os_type == 'mac':
            os_ver = random.choice(os_data['mac']['versions'])
            return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {os_ver}) Gecko/20100101 Firefox/{version}.0"
        else:
            distro = random.choice(os_data['linux']['distros'])
            return f"Mozilla/5.0 ({distro}; rv:{version}.0) Gecko/20100101 Firefox/{version}.0"
    
    elif browser == 'safari':
        version = random.choice(browsers['safari']['versions'])
        webkit = random.choice(browsers['safari']['webkit'])
        os_ver = random.choice(os_data['mac']['versions'])
        return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {os_ver}) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{version} Safari/{webkit}"
    
    else:
        version = random.choice(browsers['edge']['versions'])
        webkit = random.choice(browsers['chrome']['webkit'])
        safari = random.choice(browsers['chrome']['safari'])
        patch = random.randint(0, 9999)
        os_ver = random.choice(os_data['windows']['versions'])
        arch = random.choice(os_data['windows']['archs'])
        return f"Mozilla/5.0 (Windows NT {os_ver}; {arch}) AppleWebKit/{webkit}.36 (KHTML, like Gecko) Chrome/{version}.0.0.{patch} Safari/{safari}.36 Edg/{version}.0.0.{patch}"

def gm():
    ios_ver = random.choice(os_data['mobile']['ios'])
    android_ver = random.choice(os_data['mobile']['android'])
    device = random.choice(os_data['mobile']['devices'])
    
    if random.choice([True, False]):
        safari_ver = random.choice(browsers['safari']['versions'])
        webkit = random.choice(browsers['safari']['webkit'])
        build = random.randint(10000, 99999)
        device_type = random.choice(['iPhone', 'iPad'])
        
        if device_type == 'iPhone':
            return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit}"
        else:
            return f"Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit}"
    else:
        chrome_ver = random.choice(browsers['chrome']['versions'])
        webkit = random.choice(browsers['chrome']['webkit'])
        safari = random.choice(browsers['chrome']['safari'])
        patch = random.randint(0, 9999)
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/{webkit}.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.0.{patch} Mobile Safari/{safari}.36"

def gh():
    header_type = random.choice(['regular', 'login', 'api', 'mobile'])
    
    if header_type == 'regular':
        return {
            'User-Agent': gu(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': random.choice(lg),
            'Accept-Encoding': random.choice(en),
            'Connection': random.choice(cc),
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': random.choice(ca),
            'DNT': str(random.randint(0, 1))
        }
    elif header_type == 'login':
        return {
            'User-Agent': gu(),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': random.choice(lg),
            'Accept-Encoding': random.choice(en),
            'Content-Type': 'application/json',
            'Connection': random.choice(cc),
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Cache-Control': 'no-cache',
            'DNT': str(random.randint(0, 1))
        }
    elif header_type == 'api':
        return {
            'User-Agent': gu(),
            'Accept': '*/*',
            'Accept-Language': random.choice(lg),
            'Accept-Encoding': random.choice(en),
            'Connection': random.choice(cc),
            'X-Requested-With': 'XMLHttpRequest',
            'DNT': str(random.randint(0, 1))
        }
    else:
        return {
            'User-Agent': gm(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': random.choice(lg),
            'Accept-Encoding': random.choice(en),
            'Connection': random.choice(cc),
            'Upgrade-Insecure-Requests': '1'
        }

def gb(count):
    return [gh() for _ in range(count)]

def fs(count):
    print("generating...")
    with ThreadPoolExecutor(max_workers=12) as executor:
        batch_size = count // 12
        futures = [executor.submit(gb, batch_size) for _ in range(12)]
        
        all_headers = []
        for future in futures:
            all_headers.extend(future.result())
    
    with open("headers.json", 'w') as f:
        json.dump(all_headers, f, indent=2)
    
    print(f"done: {len(all_headers)} headers")

if __name__ == "__main__":
    count = int(input("how many: "))
    fs(count)
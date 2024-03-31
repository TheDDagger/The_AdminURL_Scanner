import requests
from termcolor import colored
import concurrent.futures
import time

def find_admin_login(url):
    start_time = time.time()
    common_admin_paths = get_common_admin_paths()
    found_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(scan_admin_path, url, path): path for path in common_admin_paths}

        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                if future.result():
                    found_count += 1
                    print(colored(f"Admin login found: {url.rstrip('/') + path}", 'yellow'))
            except Exception as e:
                pass

    end_time = time.time()
    duration = end_time - start_time
    print(colored(f"\nTotal admin paths found: {found_count}", 'yellow'))
    print(colored(f"Time taken: {duration:.2f} seconds", 'yellow'))

def scan_admin_path(url, path):
    admin_url = url.rstrip('/') + path
    try:
        response = requests.get(admin_url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

def get_common_admin_paths():
    return [
        '/admin', '/administrator', '/login', '/wp-admin', '/admin/login.php',
        '/admin/login', '/user/login', '/cpanel', '/admin.php', '/wp-login.php',
        '/wp-login', '/admin/', '/administrator/', '/login/', '/wp-admin/',
        '/admin.php/', '/admin/login.php/', '/admin/login/', '/user/login/',
        '/cpanel/', '/admin.asp', '/administrator.asp', '/login.asp',
        '/wp-admin.asp', '/admin/login.asp', '/admin/login.asp', '/user/login.asp',
        '/cpanel.asp', '/admin.php', '/administrator.php', '/login.php',
        '/wp-admin.php', '/admin/login.php', '/admin/login.php', '/user/login.php',
        '/cpanel.php', '/admin.jsp', '/administrator.jsp', '/login.jsp',
        '/wp-admin.jsp', '/admin/login.jsp', '/admin/login.jsp', '/user/login.jsp',
        '/cpanel.jsp', '/admin.html', '/administrator.html', '/login.html',
        '/wp-admin.html', '/admin/login.html', '/admin/login.html', '/user/login.html',
        '/cpanel.html', '/admin.js', '/administrator.js', '/login.js',
        '/wp-admin.js', '/admin/login.js', '/admin/login.js', '/user/login.js',
        '/cpanel.js', '/admin.cgi', '/administrator.cgi', '/login.cgi',
        '/wp-admin.cgi', '/admin/login.cgi', '/admin/login.cgi', '/user/login.cgi',
        '/cpanel.cgi', '/admin.pl', '/administrator.pl', '/login.pl',
        '/wp-admin.pl', '/admin/login.pl', '/admin/login.pl', '/user/login.pl',
        '/cpanel.pl', '/admin/config', '/administrator/config', '/login/config',
        '/wp-admin/config', '/admin/login/config', '/admin/login/config',
        '/user/login/config', '/cpanel/config', '/admin/administrators',
        '/administrator/administrators', '/login/administrators',
        '/wp-admin/administrators', '/admin/login/administrators',
        '/admin/login/administrators', '/user/login/administrators',
        '/cpanel/administrators', '/admin/admin', '/administrator/admin',
        '/login/admin', '/wp-admin/admin', '/admin/login/admin', '/admin/login/admin',
        '/user/login/admin', '/cpanel/admin', '/admin/administrator',
        '/administrator/administrator', '/login/administrator', '/wp-admin/administrator',
        '/admin/login/administrator', '/admin/login/administrator', '/user/login/administrator',
        '/cpanel/administrator', '/admin/administration', '/administrator/administration',
        '/login/administration', '/wp-admin/administration', '/admin/login/administration',
        '/admin/login/administration', '/user/login/administration', '/cpanel/administration',
        '/admin/auth', '/administrator/auth', '/login/auth', '/wp-admin/auth',
        '/admin/login/auth', '/admin/login/auth', '/user/login/auth', '/cpanel/auth',
        '/admin/admin_auth', '/administrator/admin_auth', '/login/admin_auth',
        '/wp-admin/admin_auth', '/admin/login/admin_auth', '/admin/login/admin_auth',
        '/user/login/admin_auth', '/cpanel/admin_auth', '/admin/administrator_auth',
        '/administrator/administrator_auth', '/login/administrator_auth',
        '/wp-admin/administrator_auth', '/admin/login/administrator_auth',
        '/admin/login/administrator_auth', '/user/login/administrator_auth',
        '/cpanel/administrator_auth', '/admin/authenticate', '/administrator/authenticate',
        '/login/authenticate', '/wp-admin/authenticate', '/admin/login/authenticate',
        '/admin/login/authenticate', '/user/login/authenticate', '/cpanel/authenticate',
        '/admin/admin_authenticate', '/administrator/admin_authenticate',
        '/login/admin_authenticate', '/wp-admin/admin_authenticate',
        '/admin/login/admin_authenticate', '/admin/login/admin_authenticate',
        '/user/login/admin_authenticate', '/cpanel/admin_authenticate',
        '/admin/administrator_authenticate', '/administrator/administrator_authenticate',
        '/login/administrator_authenticate', '/wp-admin/administrator_authenticate',
        '/admin/login/administrator_authenticate', '/admin/login/administrator_authenticate',
        '/user/login/administrator_authenticate', '/cpanel/administrator_authenticate',
        '/admin/validate', '/administrator/validate', '/login/validate', '/wp-admin/validate',
        '/admin/login/validate', '/admin/login/validate', '/user/login/validate', '/cpanel/validate',
        '/admin/admin_validate'
    ]

def main():
    url = input("Enter the URL you want to scan: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Add 'http://' if not provided
    find_admin_login(url)

if __name__ == "__main__":
    main()

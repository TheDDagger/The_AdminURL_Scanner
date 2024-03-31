import asyncio
import aiohttp
from termcolor import colored
import time

MAX_CONCURRENT_REQUESTS = 100
TIMEOUT = 5

async def find_admin_login(url):
    start_time = time.time()
    common_admin_paths = get_common_admin_paths()
    found_count = 0
    total_paths = len(common_admin_paths)
    print(colored("Scanning for admin login paths...", 'cyan'))

    async with aiohttp.ClientSession() as session:
        tasks = []
        scanned_paths = []

        for path in common_admin_paths:
            task = asyncio.ensure_future(scan_admin_path(session, url, path, scanned_paths))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        for response in responses:
            if response:
                found_count += 1
                print(colored(f"Admin login found: {url.rstrip('/') + response}", 'green'))

    end_time = time.time()
    duration = end_time - start_time
    print(colored(f"\nTotal admin paths found: {found_count}", 'yellow'))
    print(colored(f"Time taken: {duration:.2f} seconds", 'yellow'))

async def scan_admin_path(session, url, path, scanned_paths):
    admin_url = url.rstrip('/') + path
    scanned_paths.append(path)
    try:
        async with session.get(admin_url, timeout=TIMEOUT) as response:
            if response.status == 200:
                return path
    except aiohttp.ClientError as e:
        print(colored(f"Error scanning path {admin_url}: {e}", 'red'))
    except asyncio.TimeoutError:
        print(colored(f"Timeout scanning path {admin_url}", 'red'))

async def main():
    url = input("Enter the URL you want to scan: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    await find_admin_login(url)

def get_common_admin_paths():
    common_admin_paths = [
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
        '/admin/login/administrator_authenticate', '/admin/login/administrator_authenticate'
    ]
    return common_admin_paths

if __name__ == "__main__":
    asyncio.run(main())

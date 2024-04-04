import asyncio
import aiohttp
import time
import logging
from termcolor import colored

MAX_CONCURRENT_REQUESTS = 100
TIMEOUT = 5

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Common prefixes and suffixes for admin paths
COMMON_PREFIXES = ['', '/', '/admin', '/administrator', '/login', '/wp-admin']
COMMON_SUFFIXES = ['', '/', '/login.php', '/login.asp', '/login.jsp', '/login.html']

async def find_admin_login(url, verbose=False):
    start_time = time.time()
    found_count = 0
    scanned_paths = set()

    if verbose:
        logger.info("Scanning for admin login paths...")

    async with aiohttp.ClientSession() as session:
        while True:
            new_paths = generate_admin_paths(COMMON_PREFIXES, COMMON_SUFFIXES)
            tasks = []

            for path in new_paths:
                if path not in scanned_paths:
                    task = asyncio.ensure_future(scan_admin_path(session, url, path, scanned_paths, verbose))
                    tasks.append(task)

            responses = await asyncio.gather(*tasks)

            for response in responses:
                if response[0]:
                    found_count += 1
                    if verbose:
                        logger.info(f"Admin login found: {url.rstrip('/') + response[1]}")
                elif response[1]:
                    if verbose:
                        logger.error(f"Timeout scanning path {url.rstrip('/') + response[2]}")

            await asyncio.sleep(5)  # Sleep for a while before scanning again

    end_time = time.time()
    duration = end_time - start_time
    if verbose:
        logger.info(f"Total admin paths found: {found_count}")
        logger.info(f"Time taken: {duration:.2f} seconds")


async def scan_admin_path(session, url, path, scanned_paths, verbose):
    admin_url = url.rstrip('/') + path
    scanned_paths.add(path)
    timeout = False
    try:
        async with session.get(admin_url, timeout=TIMEOUT) as response:
            if response.status == 200:
                return True, path, ''
    except aiohttp.ClientError as e:
        if verbose:
            logger.error(f"Error scanning path {admin_url}: {e}")
    except asyncio.TimeoutError:
        timeout = True
    return False, timeout, path


def generate_admin_paths(prefixes, suffixes):
    # Generate admin paths using prefixes and suffixes
    admin_paths = set()
    for prefix in prefixes:
        for suffix in suffixes:
            admin_paths.add(prefix + suffix)
    return admin_paths


async def main():
    url = input("Enter the URL you want to scan: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    verbose_input = input("Do you want verbose output? (y/n): ").strip().lower()
    verbose = verbose_input == 'y' or verbose_input == 'yes'

    await find_admin_login(url, verbose)


if __name__ == "__main__":
    asyncio.run(main())

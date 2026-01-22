#!/usr/bin/env python3
import re

def extract_domains_from_adguard(filename):
    """Extract domains from AdguardDNS format (plain domain list)"""
    domains = set()
    invalid_count = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Domain should be the entire line (already in plain format)
            domain = line.strip()
            
            # Validate domain
            # Skip if it's an IP address
            if re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', domain):
                invalid_count += 1
                continue
            
            # Skip if it has invalid characters
            if not re.match(r'^[a-zA-Z0-9\.\-_]+$', domain):
                invalid_count += 1
                continue
            
            # Skip if too long
            if len(domain) > 253:
                invalid_count += 1
                continue
            
            # Skip if single character
            if len(domain) == 1:
                invalid_count += 1
                continue
            
            # Skip reserved entries
            if domain in ['0.0.0.0', 'localhost', 'broadcasthost', 'local']:
                invalid_count += 1
                continue
            
            domains.add(domain)
    
    return domains, invalid_count

def extract_domains_from_hosts(filename):
    """Extract domains from hosts file format (0.0.0.0 domain.com)"""
    domains = set()
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Skip comments, headers, and localhost entries
            if line.startswith('#') or line.startswith('127.0.0.1') or \
               line.startswith('255.255.255.255') or line.startswith('::1') or \
               line.startswith('fe80::') or line.startswith('ff') or not line:
                continue
            
            # Extract domain from hosts format
            match = re.match(r'^0\.0\.0\.0\s+(.+)$', line)
            if match:
                domain = match.group(1).strip()
                domains.add(domain)
    
    return domains

def main():
    print("Merging AdguardDNS with SELO blocklist...\n")
    
    # Extract domains from both files
    print("Reading seloblocklist.txt...")
    selo_domains = extract_domains_from_hosts('seloblocklist.txt')
    print(f"  Found {len(selo_domains)} domains")
    
    print("\nReading AdguardDNS.txt...")
    adguard_domains, invalid_adguard = extract_domains_from_adguard('AdguardDNS.txt')
    print(f"  Found {len(adguard_domains)} valid domains")
    print(f"  Skipped {invalid_adguard} invalid entries")
    
    # Find new domains from AdguardDNS
    new_domains = adguard_domains - selo_domains
    print(f"\nNew domains from AdguardDNS: {len(new_domains)}")
    print(f"Duplicates already in SELO: {len(adguard_domains) - len(new_domains)}")
    
    # Combine all domains
    all_domains = selo_domains.union(adguard_domains)
    sorted_domains = sorted(all_domains)
    
    print(f"\nTotal unique domains after merge: {len(sorted_domains)}")
    
    # Write merged file
    with open('seloblocklist.txt', 'w', encoding='utf-8') as f:
        f.write('# Title: SELO Block List\n')
        f.write('#\n')
        f.write('# This hosts file is a merged collection of hosts from:\n')
        f.write('# - oisd (https://oisd.nl/)\n')
        f.write('# - StevenBlack (https://github.com/StevenBlack/hosts)\n')
        f.write('# - AdguardDNS (https://filters.adtidy.org/)\n')
        f.write('#\n')
        f.write('# Duplicates and invalid entries have been removed\n')
        f.write('#\n')
        f.write(f'# Total unique domains: {len(sorted_domains)}\n')
        f.write('# Generated: ' + str(__import__('datetime').datetime.now()) + '\n')
        f.write('#\n')
        f.write('# ===============================================================\n\n')
        
        f.write('127.0.0.1 localhost\n')
        f.write('127.0.0.1 localhost.localdomain\n')
        f.write('127.0.0.1 local\n')
        f.write('255.255.255.255 broadcasthost\n')
        f.write('::1 localhost\n')
        f.write('::1 ip6-localhost\n')
        f.write('::1 ip6-loopback\n')
        f.write('fe80::1%lo0 localhost\n')
        f.write('ff00::0 ip6-localnet\n')
        f.write('ff00::0 ip6-mcastprefix\n')
        f.write('ff02::1 ip6-allnodes\n')
        f.write('ff02::2 ip6-allrouters\n')
        f.write('ff02::3 ip6-allhosts\n')
        f.write('0.0.0.0 0.0.0.0\n\n')
        
        f.write('# Start combined domains\n\n')
        
        for domain in sorted_domains:
            f.write(f'0.0.0.0 {domain}\n')
    
    print("\n✓ Merge complete!")
    print(f"\nSummary:")
    print(f"  SELO original domains: {len(selo_domains)}")
    print(f"  AdguardDNS valid domains: {len(adguard_domains)}")
    print(f"  New domains added: {len(new_domains)}")
    print(f"  Final total: {len(sorted_domains)}")
    print(f"\nOutput saved to: seloblocklist.txt")

if __name__ == '__main__':
    main()

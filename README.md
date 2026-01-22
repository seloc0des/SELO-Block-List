# SELO Block List

A comprehensive Pi-hole blocklist combining the best of oisd and StevenBlack hosts files, optimized for maximum ad, tracker, and malware blocking.

## 📊 Statistics

- **Total Unique Domains:** 348,524
- **Format:** Hosts file (`0.0.0.0 domain.com`)
- **Duplicates:** 0
- **Invalid Entries:** 0
- **Last Updated:** 2026-01-22

## 🎯 What This Blocks

This blocklist combines multiple trusted sources to block:
- **Advertisements** - Banner ads, pop-ups, video ads
- **Tracking & Analytics** - Cross-site trackers, analytics scripts
- **Malware & Phishing** - Known malicious domains
- **Telemetry** - Unwanted data collection

## 📦 Source Lists

This blocklist is a cleaned and deduplicated merge of:
- **[oisd](https://oisd.nl/)** - Comprehensive domain blocklist (209,864 domains)
- **[StevenBlack](https://github.com/StevenBlack/hosts)** - Unified hosts file (69,987 domains)
- **[AdguardDNS](https://filters.adtidy.org/)** - Adguard DNS filter (137,528 domains)

After deduplication: **348,524 unique domains**

## 🚀 How to Use with Pi-hole

### Method 1: Web Interface

1. Log into your Pi-hole admin panel
2. Navigate to **Adlists** (or **Group Management → Adlists**)
3. Add this URL:
   ```
   https://raw.githubusercontent.com/seloc0des/SELO-Block-List/main/seloblocklist.txt
   ```
4. Click **Add**
5. Go to **Tools → Update Gravity**
6. Click **Update** to apply the blocklist

### Method 2: Command Line

```bash
pihole -a adlist add https://raw.githubusercontent.com/seloc0des/SELO-Block-List/main/seloblocklist.txt
pihole -g
```

## ✅ Compatibility

- ✓ Pi-hole
- ✓ AdGuard Home
- ✓ Any DNS-based blocker supporting hosts format
- ✓ System hosts file (`/etc/hosts`)

## 🔄 Update Frequency

This list is manually curated and updated periodically to ensure quality and accuracy. Pi-hole will automatically check for updates based on your gravity update schedule.

## 📝 Format

Standard hosts file format:
```
0.0.0.0 example-ad-domain.com
0.0.0.0 tracking-domain.net
```

## ⚠️ Troubleshooting

If a legitimate site is blocked:
1. Check Pi-hole's **Query Log** to identify the blocked domain
2. Add the domain to your **Whitelist**
3. Update gravity: `pihole -g`

## 📄 License

This blocklist is provided as-is for personal and commercial use. The source lists maintain their original licenses.

## 🤝 Contributing

Found a domain that should be blocked or whitelisted? Open an issue with details.

## 🔗 Links

- [Pi-hole Documentation](https://docs.pi-hole.net/)
- [oisd Blocklist](https://oisd.nl/)
- [StevenBlack Hosts](https://github.com/StevenBlack/hosts)

---

**Made with ❤️ for a cleaner, faster internet**

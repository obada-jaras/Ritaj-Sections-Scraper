# 📚 Ritaj Sections Scraper

A lightweight Python script that monitors **specific course sections** at Birzeit University's Ritaj portal and sends Telegram notifications when enrollment spots become available.

> ⚠️ **Note**: This is a quick proof-of-concept project focused specifically on course section monitoring. While the **[Ritaj Marks Scraper](https://github.com/obada-jaras/Ritaj-Marks-Scraper)** handles Telegram integration, Ritaj authentication, and threading in a more robust way, this project provides the core functionality for scraping and monitoring course enrollment availability.

## 🎯 What It Does

- **Monitors** specific courses (NLP, Compiler) for available enrollment spots
- **Checks** enrollment numbers every 3 seconds
- **Notifies** via Telegram when sections have openings or are near capacity
- **Runs** continuously until manually stopped

## ⚙️ Technical Overview

### Structure
- **`main.py`**: Core async scraper using SeleniumBase
- **`config.py`**: Configuration with hardcoded credentials *(not recommended)*

### Key Features
- Async/await pattern for non-blocking operations
- SeleniumBase for browser automation
- Direct Telegram Bot API integration
- XPath-based element selection

### Current Limitations
- **Hardcoded credentials** in config file
- **Specific course selectors** only (NLP & Compiler)
- **No error recovery** mechanisms
- **Fixed Telegram chat ID**
- **No user management** system

## 🚀 Quick Setup

```bash
# Clone and install
git clone https://github.com/obada-jaras/Ritaj-Sections-Scraper.git
cd Ritaj-Sections-Scraper
pip install seleniumbase python-telegram-bot

# Configure
# Edit config.py with your credentials and bot token

# Run
python main.py
```

## 🔧 Recommended Enhancements

This project could benefit from significant improvements:

- [ ] **Security**: Remove hardcoded credentials, use environment variables
- [ ] **Flexibility**: Make course monitoring configurable rather than hardcoded
- [ ] **Architecture**: Implement proper error handling and logging
- [ ] **User Management**: Support multiple users like the main project
- [ ] **Database**: Persist data instead of runtime-only tracking
- [ ] **Code Quality**: Add proper structure, documentation, and tests

## 🤝 Collaboration Opportunity

**Consider merging with [Ritaj Marks Scraper](https://github.com/obada-jaras/Ritaj-Marks-Scraper)!** 

The marks scraper project offers:
- ✅ Multi-user support with Telegram bot interface
- ✅ Secure credential management
- ✅ Proper error handling and session management
- ✅ Clean architecture with separation of concerns
- ✅ Comprehensive documentation

This sections monitoring functionality would be a perfect addition to that project's feature set.

## 📬 Contact & Contributions

Interested in improving this project or discussing a merge with the main Ritaj scraper?

- **LinkedIn**: [Connect with me](https://www.linkedin.com/in/obada-tahayna/)
- **GitHub**: [@obada-jaras](https://github.com/obada-jaras)
- **Issues**: Feel free to open issues or pull requests

---

**⚡ Quick Start Tip**: If you're looking for a more robust solution, start with the **[Ritaj Marks Scraper](https://github.com/obada-jaras/Ritaj-Marks-Scraper)** instead! 
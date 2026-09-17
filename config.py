
import os
from dotenv import load_dotenv

load_dotenv()

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Model settings
LLM_MODEL = "gpt-3.5-turbo" 

# Job search settings
DEFAULT_JOB_COUNT = 5
JOB_PLATFORMS = ["LinkedIn", "Indeed", "Glassdoor", "ZipRecruiter", "Monster"]


COLORS = {
    # Primary palette
    "primary": "#0E6E78",      # Deep harbor teal for main elements and headers
    "secondary": "#12909E",    # Medium teal for secondary elements
    "tertiary": "#79C6CE",     # Light teal for tertiary elements

    # Accent colors
    "accent": "#BE3E6E",       # Berry for highlighting
    "accent1": "#33788A",      # Slate teal for subtler accents
    "accent2": "#3FA98F",      # Seafoam for highlighting information
    "accent3": "#BE3E6E",      # Berry for call-to-action buttons

    # Functional colors
    "success": "#2E9E77",      # Sea green for success messages
    "warning": "#DFA126",      # Golden amber for warnings
    "error": "#D64545",        # Bright red for errors
    "info": "#1178A8",         # Information blue

    # Background and text - BASIC PROFESSIONAL STYLE
    "background": "#F3F8F8",   # Light teal-gray for backgrounds
    "card_bg": "#FFFFFF",      # White for card backgrounds
    "text": "#FFFFFF",         # White for text on dark backgrounds
    "text_dark": "#0C2A2E",    # Deep teal-black for text on light backgrounds
    "text_light": "#3C5257",   # Dark teal-gray for secondary text
    "text_red": "#E05A5A",     # Red color for high-contrast text
    "panel_bg": "#E9F4F4"      # Light teal background for panels
}

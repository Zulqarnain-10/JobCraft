
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
    "primary": "#5A189A",      # Deep violet for main elements and headers
    "secondary": "#7B2CBF",    # Medium violet for secondary elements
    "tertiary": "#C77DFF",     # Light violet for tertiary elements

    # Accent colors
    "accent": "#9D4EDD",       # Bright violet for highlighting
    "accent1": "#6247AA",      # Slate violet for subtler accents
    "accent2": "#B388EB",      # Lavender for highlighting information
    "accent3": "#7B2CBF",      # Vivid violet for call-to-action buttons

    # Functional colors
    "success": "#2E9E77",      # Sea green for success messages
    "warning": "#DFA126",      # Golden amber for warnings
    "error": "#D64545",        # Bright red for errors
    "info": "#6247AA",         # Information violet

    # Background and text - BASIC PROFESSIONAL STYLE
    "background": "#F7F4FB",   # Light violet-gray for backgrounds
    "card_bg": "#FFFFFF",      # White for card backgrounds
    "text": "#FFFFFF",         # White for text on dark backgrounds
    "text_dark": "#13233B",    # Ink navy for text on light backgrounds
    "text_light": "#4A4458",   # Dark violet-gray for secondary text
    "text_red": "#E05A5A",     # Red color for high-contrast text
    "panel_bg": "#EFE7F9"      # Light violet background for panels
}

import pytest
from playwright.sync_api import Page, expect

def test_google_search_structure(page: Page):
    # Navigate securely to the target platform
    page.goto("https://google.com")
    
    # Asserting web properties leveraging Web-First Assertions
    expect(page).to_have_title("Google")
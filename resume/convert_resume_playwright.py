#!/usr/bin/env python3
"""
HTML to PDF Converter using Playwright (Browser-based)
More reliable for complex CSS and web fonts
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path

async def install_playwright():
    """Install Playwright if not available"""
    try:
        from playwright.async_api import async_playwright
        print("✅ Playwright is already installed")
        return True
    except ImportError:
        print("📦 Installing Playwright...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
            subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
            print("✅ Playwright installed successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to install Playwright: {e}")
            return False

async def convert_with_playwright():
    """Convert HTML to PDF using Playwright (browser-based)"""
    try:
        from playwright.async_api import async_playwright
        
        html_file = Path("resume_enhanced.html").resolve()
        pdf_file = Path("Sharon_Tsang_Resume_Web3_UX_Designer.pdf")
        
        if not html_file.exists():
            print(f"❌ Error: {html_file} not found!")
            return False
        
        print(f"🌐 Converting {html_file} to PDF using browser engine...")
        
        async with async_playwright() as p:
            # Launch browser
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # Navigate to HTML file
            await page.goto(f"file://{html_file}")
            
            # Wait for fonts to load
            await page.wait_for_timeout(3000)
            
            # Generate PDF with professional settings
            await page.pdf(
                path=pdf_file,
                format='A4',
                margin={
                    'top': '0.5in',
                    'right': '0.5in',
                    'bottom': '0.5in',
                    'left': '0.5in'
                },
                print_background=True,
                prefer_css_page_size=True
            )
            
            await browser.close()
        
        print(f"✅ Successfully created: {pdf_file}")
        
        if pdf_file.exists():
            size_kb = pdf_file.stat().st_size / 1024
            print(f"📊 File size: {size_kb:.1f} KB")
            print("🎯 Your professional Web3 UX Designer resume is ready!")
            return True
        else:
            print("❌ PDF file was not created")
            return False
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return False

async def main():
    """Main async function"""
    print("🚀 Sharon's Resume PDF Generator (Playwright)")
    print("=" * 45)
    
    # Install Playwright
    if not await install_playwright():
        print("💡 Installation failed, please try manual conversion")
        return
    
    # Convert to PDF
    success = await convert_with_playwright()
    
    if success:
        print("\n🎉 PDF generation completed successfully!")
        print("📁 Your professional resume is ready!")
        print("💼 Perfect for Web3 and finance job applications!")
        print("📄 File: Sharon_Tsang_Resume_Web3_UX_Designer.pdf")
    else:
        print("\n💥 PDF generation failed.")

if __name__ == "__main__":
    asyncio.run(main())

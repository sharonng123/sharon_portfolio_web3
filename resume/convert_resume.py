#!/usr/bin/env python3
"""
HTML to PDF Converter for Sharon's Resume
"""

import os
import sys
import subprocess
from pathlib import Path

def install_weasyprint():
    """Install WeasyPrint if not available"""
    try:
        import weasyprint
        print("✅ WeasyPrint is already installed")
        return True
    except ImportError:
        print("📦 Installing WeasyPrint...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "weasyprint"])
            import weasyprint
            print("✅ WeasyPrint installed successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to install WeasyPrint: {e}")
            return False

def convert_to_pdf():
    """Convert HTML resume to PDF"""
    try:
        import weasyprint
        
        # File paths
        html_file = Path("resume_enhanced.html")
        pdf_file = Path("Sharon_Tsang_Resume_Web3_UX_Designer.pdf")
        
        # Check if HTML file exists
        if not html_file.exists():
            print(f"❌ Error: {html_file} not found!")
            return False
        
        print(f"📄 Converting {html_file} to PDF...")
        
        # Read HTML content
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert to PDF with professional settings
        html_doc = weasyprint.HTML(string=html_content, base_url='.')
        html_doc.write_pdf(
            pdf_file,
            optimize_images=True,
        )
        
        print(f"✅ Successfully created: {pdf_file}")
        
        # Check file size
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

def main():
    """Main function"""
    print("🚀 Sharon's Resume PDF Generator")
    print("=" * 40)
    
    # Install WeasyPrint if needed
    if not install_weasyprint():
        print("💡 Installation failed, please try manual conversion")
        return
    
    # Convert to PDF
    success = convert_to_pdf()
    
    if success:
        print("\n🎉 PDF generation completed successfully!")
        print("📁 Ready for Web3 and finance job applications!")
        print("💼 File: Sharon_Tsang_Resume_Web3_UX_Designer.pdf")
    else:
        print("\n⚠️ Automatic conversion failed.")

if __name__ == "__main__":
    main()

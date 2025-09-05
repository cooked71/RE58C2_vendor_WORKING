#!/usr/bin/env python3

import sys
import re

def debug_makefile(mk_file, duplicates):
    """Debug function to see what the script finds"""
    try:
        with open(mk_file, 'r') as f:
            lines = f.readlines()
        
        print("=== DEBUG OUTPUT ===")
        print(f"Looking for these duplicates in makefile:")
        for dup in list(duplicates)[:10]:  # Show first 10
            print(f"  - {dup}")
        
        pattern = r'^([\w\/\.@\-\$\(\)]+):\s*\$\(TARGET_COPY_OUT_\w+\)/([\w\/\.@\-]+)\\?$'
        
        for i, line in enumerate(lines):
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                source_path = match.group(1)
                target_path = match.group(2)
                
                if source_path in duplicates or target_path in duplicates:
                    print(f"Line {i+1}: FOUND MATCH - {line}")
                else:
                    print(f"Line {i+1}: no match - {line}")
            elif line and not line.startswith('#'):
                print(f"Line {i+1}: pattern not matched - {line}")
                    
    except FileNotFoundError:
        print(f"Error: Makefile {mk_file} not found")

# Use this instead of clean_makefile for debugging
# debug_makefile(mk_file, duplicates)
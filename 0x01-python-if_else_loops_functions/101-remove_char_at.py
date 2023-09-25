#!/usr/bin/python3

def remove_char_at(s, n):
    """Remove Character at given position"""
    if n < 0 or n >= len(s):
        return s
    return s[:n] + s[n+1:]

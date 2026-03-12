# AIF Engine Use Cases

This document explains how to use the AIF Engine to build powerful CLI tools and autonomous agents.

## 1. Upbit Quant Trading Bot (Bridge Script Architecture)

**Problem:** 
Upbit requires a dynamic JWT token where the payload (query parameters) must be hashed and signed with a Secret Key for every single request. A static CLI cannot handle this out-of-the-box.

**Solution:**
We use a **"Bridge Script Architecture"**. A simple Python script acts as the "brain" (calculating RSI, deciding when to buy/sell, and generating the dynamic JWT), and it uses the generated `aif-upbit` CLI as its "hands" to execute the actual API call.

*   **Spec File:** See `assets/upbit-spec.json`
*   **Bridge Script:** See `assets/upbit_bridge.py`

**How it works:**
1. The Python script calculates the JWT token.
2. It runs `aif-upbit auth login --token <JWT>` to load the token.
3. It immediately runs `aif-upbit buy --market KRW-BTC --price 5000` to execute the trade.

## 2. Social Media Auto-Poster (Upost)

**Problem:**
You want to post identical content to multiple social media platforms (X, LinkedIn) simultaneously from the terminal, without dealing with OAuth flows manually.

**Solution:**
Create a simple `upost-spec.json` that defines the endpoints for the platforms.

*   **Spec File:** See `assets/upost-spec.json`

By referencing these examples, AI agents can learn how to construct complex workflows combining the lightweight AIF CLI with external logic scripts.
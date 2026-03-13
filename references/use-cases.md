# AIF Engine Use Cases

This document explains how to use the AIF Engine to build powerful CLI tools and autonomous agents.

## 1. Upbit Quant Trading Bot (Bridge Script Architecture)

**Problem:** 
Upbit requires a dynamic JWT token where the payload (query parameters) must be hashed and signed with a Secret Key for every single request. A static CLI cannot handle this out-of-the-box.

**Solution:**
We use a **"Hybrid Architecture"**. A simple Python script acts as the "brain" (calculating RSI, deciding when to buy/sell). For simple data retrieval (like checking market prices or account status), the generated `aif-upbit` CLI acts as its "eyes". However, due to Upbit's extremely strict payload hashing requirements for JWT generation on POST requests, the actual buy/sell execution (the "hands") is handled safely by the official `pyupbit` Python SDK.

*   **Spec File:** See `assets/upbit-spec.json` (used for GET requests)
*   **Agent Script:** See `assets/upbit_agent.py`

**How it works:**
1. The Python script runs continuously, checking prices.
2. It uses the `aif-upbit` CLI (or pyupbit directly) to gather market data.
3. When trading conditions are met, it executes the secure trade using the official Python SDK to guarantee 100% reliability against strict payload hashing rules.

## 2. Social Media Auto-Poster (Upost)

**Problem:**
You want to post identical content to multiple social media platforms (X, LinkedIn) simultaneously from the terminal, without dealing with OAuth flows manually.

**Solution:**
Create a simple `upost-spec.json` that defines the endpoints for the platforms.

*   **Spec File:** See `assets/upost-spec.json`

By referencing these examples, AI agents can learn how to construct complex workflows combining the lightweight AIF CLI with external logic scripts.
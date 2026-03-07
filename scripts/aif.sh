#!/usr/bin/env bash
set -e

# Version and repository for the actual AIF Engine releases
VERSION="v1.0.0"
REPO="mommocmoc/aif-engine"
BIN_DIR="$HOME/.local/bin/aif-engine-bin"
BIN_PATH="$BIN_DIR/aif"

# 1. Check if binary is already installed
if [ ! -f "$BIN_PATH" ]; then
    echo "🤖 AIF Engine binary not found. Downloading..."
    mkdir -p "$BIN_DIR"

    # OS and Architecture detection
    OS="$(uname -s)"
    ARCH="$(uname -m)"

    if [ "$ARCH" = "x86_64" ]; then
        ARCH="amd64"
    elif [ "$ARCH" = "aarch64" ]; then
        ARCH="arm64"
    fi

    # Assuming GoReleaser naming convention: aif_Darwin_arm64.tar.gz
    # You might need to adjust this matching exactly what goreleaser outputs.
    FILE_NAME="aif_${OS}_${ARCH}.tar.gz"
    DOWNLOAD_URL="https://github.com/$REPO/releases/download/$VERSION/$FILE_NAME"

    echo "Downloading from $DOWNLOAD_URL ..."
    # Download and extract the binary
    curl -sL "$DOWNLOAD_URL" | tar -xz -C "$BIN_DIR" aif
    chmod +x "$BIN_PATH"
    echo "✅ Download complete: $BIN_PATH"
fi

# 2. Pass all arguments to the actual binary
"$BIN_PATH" "$@"

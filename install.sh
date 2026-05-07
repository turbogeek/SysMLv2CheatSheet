#!/bin/bash

echo "========================================================"
echo "SysML v2 Automated Validation Pipeline Setup"
echo "========================================================"
echo ""

# 1. Check for Git
if ! command -v git &> /dev/null; then
    echo "[ERROR] Git is not installed or not found in PATH."
    echo "Please install Git before proceeding."
    exit 1
fi
echo "[OK] Git is installed."

# 2. Check for Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "[ERROR] Python is not installed or not found in PATH."
    echo "Please install Python 3.10+ before proceeding."
    exit 1
fi
echo "[OK] Python is installed ($PYTHON_CMD)."

# 3. Setup SysML v2 Validator directory
V2_DIR="../sysml-validator"
if [ -d "$V2_DIR" ]; then
    echo "[OK] SysML v2 Validator repository already exists at $V2_DIR."
else
    echo "[INFO] Cloning turbogeek SysML v2 Validator repository..."
    git clone https://github.com/turbogeek/sysmlv2-validator.git "$V2_DIR"
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to clone the repository. Please check your internet connection or Git configuration."
        exit 1
    fi
    echo "[OK] Cloned sysmlv2-validator to $V2_DIR."
fi

# 4. Configure Java via CATIA Magic / Cameo
echo ""
echo "========================================================"
echo "Java Configuration (CATIA Magic / Cameo)"
echo "========================================================"
echo "The validation pipeline requires a Java runtime. It is highly recommended"
echo "to use the JRE bundled with your CATIA Magic / Cameo Systems Modeler installation."
echo ""
echo "Enter the full path to your Cameo installation directory"
echo "Examples:"
echo "  macOS: /Applications/Cameo Systems Modeler.app"
echo "  Linux: /opt/Cameo_Systems_Modeler"
read -p "Path (leave empty to skip): " CAMEO_DIR

if [ -z "$CAMEO_DIR" ]; then
    echo "[INFO] Skipping Cameo Java configuration. Ensure Java is in your PATH."
else
    # Check macOS app bundle structure first, then generic Linux structure
    if [ -f "$CAMEO_DIR/Contents/PlugIns/jre/Contents/Home/bin/java" ]; then
        JRE_PATH="$CAMEO_DIR/Contents/PlugIns/jre/Contents/Home"
    elif [ -f "$CAMEO_DIR/jre/bin/java" ]; then
        JRE_PATH="$CAMEO_DIR/jre"
    else
        echo "[ERROR] Could not find bundled Java in the provided directory."
        echo "Looked for java executable inside $CAMEO_DIR/jre/bin/ or $CAMEO_DIR/Contents/PlugIns/jre/Contents/Home/bin/"
        JRE_PATH=""
    fi

    if [ -n "$JRE_PATH" ]; then
        echo "[OK] Found Cameo bundled Java at $JRE_PATH."
        read -p "Do you want to add JAVA_HOME to your shell profile (~/.bashrc or ~/.zshrc)? (y/n): " SET_JAVA
        if [[ "$SET_JAVA" =~ ^[Yy]$ ]]; then
            PROFILE_FILE=""
            if [ -f "$HOME/.zshrc" ]; then
                PROFILE_FILE="$HOME/.zshrc"
            elif [ -f "$HOME/.bashrc" ]; then
                PROFILE_FILE="$HOME/.bashrc"
            elif [ -f "$HOME/.bash_profile" ]; then
                PROFILE_FILE="$HOME/.bash_profile"
            else
                # Default to .bashrc if nothing exists
                PROFILE_FILE="$HOME/.bashrc"
            fi
            
            echo "" >> "$PROFILE_FILE"
            echo "# SysMLv2 Validation Pipeline Java Configuration" >> "$PROFILE_FILE"
            echo "export JAVA_HOME=\"$JRE_PATH\"" >> "$PROFILE_FILE"
            echo "export PATH=\"\$JAVA_HOME/bin:\$PATH\"" >> "$PROFILE_FILE"
            
            echo "[OK] Added JAVA_HOME to $PROFILE_FILE."
            echo "[INFO] You MUST run 'source $PROFILE_FILE' or restart your terminal for changes to take effect."
        fi
    fi
fi

echo ""
echo "========================================================"
echo "Setup Complete! You are ready to run the validation scripts."
echo "========================================================"

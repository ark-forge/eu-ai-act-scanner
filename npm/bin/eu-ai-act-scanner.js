#!/usr/bin/env node

const { execSync, spawn } = require("child_process");
const path = require("path");

function hasPython() {
  for (const cmd of ["python3", "python"]) {
    try {
      execSync(`${cmd} --version`, { stdio: "pipe" });
      return cmd;
    } catch {}
  }
  return null;
}

function hasPipPackage(pythonCmd) {
  try {
    execSync(`${pythonCmd} -m eu_ai_act_scanner --help`, { stdio: "pipe" });
    return true;
  } catch {
    return false;
  }
}

function main() {
  const pythonCmd = hasPython();
  if (!pythonCmd) {
    console.error(
      "Error: Python 3.9+ is required.\n" +
        "Install Python: https://python.org/downloads/\n" +
        "Then run: pip install eu-ai-act-scanner"
    );
    process.exit(1);
  }

  if (!hasPipPackage(pythonCmd)) {
    console.log("Installing eu-ai-act-scanner Python package...");
    try {
      execSync(`${pythonCmd} -m pip install eu-ai-act-scanner`, {
        stdio: "inherit",
      });
    } catch {
      console.error(
        "Failed to install eu-ai-act-scanner.\n" +
          "Try manually: pip install eu-ai-act-scanner"
      );
      process.exit(1);
    }
  }

  const args = process.argv.slice(2);
  const child = spawn(pythonCmd, ["-m", "eu_ai_act_scanner", ...args], {
    stdio: "inherit",
  });

  child.on("close", (code) => process.exit(code || 0));
}

main();

"""Custom hatch build hook to ensure node_ui dependencies are installed.

This prevents the issue where wheels are published without node_modules/
(see https://github.com/pchalasani/claude-code-tools/issues/58).
"""

import os
import shutil
import subprocess

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """Run npm install in node_ui/ before building if needed."""
        node_ui_dir = os.path.join(self.root, "node_ui")
        node_modules = os.path.join(node_ui_dir, "node_modules")

        if os.path.isdir(node_modules):
            return

        if not shutil.which("npm"):
            raise RuntimeError(
                "npm is required to build this package (node_ui depends on npm "
                "packages). Install Node.js/npm and try again."
            )

        self.app.display_info("Installing node_ui dependencies...")
        result = subprocess.run(
            ["npm", "install", "--no-audit", "--no-fund"],
            cwd=node_ui_dir,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Failed to install node_ui dependencies:\n{result.stderr}"
            )
        self.app.display_info("node_ui dependencies installed successfully.")
